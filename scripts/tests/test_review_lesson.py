import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys
import ast
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import check_lesson as c
import review_lesson as r
import compare_lesson_runs as compare
import test_lesson_harness as fixtures

class IndependentReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        p=self.root/'input.md';p.write_text('标题\n真实原文\n')
        self.refs={'handout':{'path':'input.md','sha256':c.digest(p)}};self.bind={'handout':c.digest(p)}
        self.row=dict(group='handout',criterion='evidence',location='第二行',observation='检查原文',impact='限定主张',status='pass',blocking=False,action='保留',recheck='原文相符',pages=[],citations=[{'ref':'handout','line':2,'quote':'真实原文'}])
    def review(self):return {'bindings':self.bind,'checks':[self.row]}
    def validate(self):r.validate_review(self.review(),self.bind,self.refs,self.root,{('handout','evidence')})
    def test_quote_matches_actual_line(self):self.validate()
    def test_invented_quote_rejected(self):
        self.row['citations'][0]['quote']='不存在的原文'
        with self.assertRaises(ValueError):self.validate()
    def test_wrong_line_rejected(self):
        self.row['citations'][0]['line']=1
        with self.assertRaises(ValueError):self.validate()
    def test_stale_version_rejected(self):
        (self.root/'input.md').write_text('变化')
        with self.assertRaises(ValueError):self.validate()
    def test_self_review_citation_rejected(self):
        self.row['citations'][0]['ref']='review:0'
        with self.assertRaises(ValueError):self.validate()
    def test_missing_check_rejected(self):
        with self.assertRaises(ValueError):r.validate_review({'bindings':self.bind,'checks':[]},self.bind,self.refs,self.root,{('handout','evidence')})
    def test_visual_requires_actual_image(self):
        self.row.update(group='visual',criterion='objects')
        with self.assertRaises(ValueError):r.validate_review(self.review(),self.bind,self.refs,self.root,{('visual','objects')})
    def test_supporting_image_does_not_replace_page_observation(self):
        p=self.root/'original.png';p.write_bytes(b'original')
        self.refs['source:0']={'path':p.name,'sha256':c.digest(p),'review_role':'visual'}
        self.bind['source:0']=c.digest(p)
        self.row['citations']=[{'ref':'source:0','line':0,'quote':''}]
        self.validate()
        self.row.update(group='visual',criterion='objects')
        with self.assertRaises(ValueError):r.validate_review(self.review(),self.bind,self.refs,self.root,{('visual','objects')})
    def test_prefixed_criterion_is_not_silently_repaired(self):
        self.row['criterion']='handout.evidence'
        with self.assertRaises(ValueError):self.validate()

class ReviewExecutionTests(unittest.TestCase):
    setUp = IndependentReviewTests.setUp
    def test_cancelled_call_records_unknown_usage(self):
        folder=self.root/'cancelled'
        with patch.object(r.shutil,'which',return_value='/mock/codex'), \
             patch.object(r.subprocess,'run',side_effect=KeyboardInterrupt):
            with self.assertRaisesRegex(RuntimeError,'中断'):
                r.call_judge('input',[],folder,'test-double')
        attempt=json.loads((folder/'attempts.json').read_text())[0]
        self.assertEqual(attempt['error'],'cancelled')
        self.assertIsNone(attempt['usage'])
        self.assertFalse((folder/'answer.json').exists())
    def test_complete_image_batches_merge_all_pages(self):
        renders=[]
        for page in range(1,10):
            p=self.root/f'{page}.png';p.write_bytes(b'unit-test-image')
            renders.append({'page':page,'path':p.name})
            self.refs[f'render:{page}']={'path':p.name,'sha256':c.digest(p)}
        p=self.root/'contact.png';p.write_bytes(b'unit-test-contact')
        self.refs['contact_sheet']={'path':p.name,'sha256':c.digest(p)}
        manifest={'lesson':'04','stage':'presentation','scope':['handout'],
                  'renders':renders,'contact_sheet':{'path':p.name}}
        p=self.root/'original.png';p.write_bytes(b'unit-test-original')
        self.refs['source:0']={'path':p.name,'sha256':c.digest(p),
                               'review_role':'visual','review_pages':[1,2,3,4]}
        path=self.root/'manifest.json';path.write_text(json.dumps(manifest))
        def judge(prompt,images,folder,model):
            criteria=json.loads(prompt.split('指定检查：')[1].split('\n本批页码：')[0])
            pages=ast.literal_eval(prompt.split('\n本批页码：')[1].split('\n')[0])
            self.assertEqual(self.root/'original.png' in images,folder.name=='pages-1')
            rows=[]
            for key in criteria:
                group,criterion=key.split('.')
                row=dict(self.row,group=group,criterion=criterion,pages=pages)
                if group=='visual':
                    ref='contact_sheet' if folder.name=='sequence' else f'render:{pages[0]}'
                    row['citations']=[{'ref':ref,'line':0,'quote':''}]
                rows.append(row)
            return {'checks':rows},[]
        output=self.root/'complete'
        with patch.object(c,'evaluate',return_value={'status':'incomplete','files':self.refs,'checks':[]}):
            r.run(self.root,path,output,'test-double',judge=judge)
        review=json.loads((output/'review.json').read_text())
        for row in review['checks']:
            if row['group'] in ('visual','technical'):
                self.assertEqual(row['pages'],list(range(1,10)))
        self.assertEqual(json.loads((output/'progress.json').read_text())['completed'],5)
    def execute(self, stage, mutate=False, fail_second=False):
        manifest={'lesson':'04','stage':stage,'scope':['handout'],
                  'renders':[{'page':1,'path':'page.png'}],
                  'contact_sheet':{'path':'contact.png'}}
        path=self.root/'manifest.json';path.write_text(json.dumps(manifest))
        output=self.root/'review'
        calls=[]
        def judge(prompt, images, folder, model):
            calls.append(prompt)
            if fail_second and len(calls)==2:
                if 'source:0' in self.refs:
                    self.assertNotIn('FULL_PAPER_SENTINEL', prompt)
                    self.assertIn('DIRECT_PPT_CHECK', prompt)
                    self.assertIn('都必须引用本批实际图像', prompt)
                raise RuntimeError('image review failed')
            if 'source:0' in self.refs:
                self.assertIn('FULL_PAPER_SENTINEL', prompt)
                self.assertNotIn('DIRECT_PPT_CHECK', prompt)
            rows=[]
            for group, criterion in [('alignment','handoff'),('alignment','research_thread'),
                                     ('handout','readability'),('handout','evidence')]:
                row=dict(self.row);row.update(group=group,criterion=criterion);rows.append(row)
            if mutate:(self.root/'input.md').write_text('changed during review')
            return {'checks':rows},[]
        with patch.object(c,'evaluate',return_value={'status':'incomplete','files':self.refs,'checks':[]}):
            r.run(self.root,path,output,'test-double',judge=judge)
    def test_changed_input_during_review_is_rejected(self):
        with self.assertRaises(ValueError):self.execute('source',mutate=True)
        self.assertFalse((self.root/'review/review.json').exists())
    def test_changed_evaluator_during_review_is_rejected(self):
        original=c.digest;seen=[]
        def changing_digest(path):
            if Path(path)==Path(r.__file__).resolve():
                seen.append(path)
                if len(seen)>1:return '0'*64
            return original(path)
        with patch.object(c,'digest',side_effect=changing_digest):
            with self.assertRaisesRegex(ValueError,'评价定义变化'):
                self.execute('source')
        self.assertFalse((self.root/'review/review.json').exists())
    def test_partial_image_failure_keeps_progress_not_pass(self):
        with self.assertRaises(RuntimeError):self.execute('presentation',fail_second=True)
        progress=json.loads((self.root/'review/progress.json').read_text())
        self.assertEqual(progress['completed'],1)
        self.assertFalse((self.root/'review/evidence.json').exists())
    def test_image_context_keeps_technical_evidence_and_full_bindings(self):
        for index, content in enumerate(('FULL_PAPER_SENTINEL', 'DIRECT_PPT_CHECK')):
            path=self.root/f'source-{index}.md';path.write_text(content)
            self.refs[f'source:{index}']={'path':path.name,'sha256':c.digest(path)}
        self.refs['source:1']['review_role']='technical'
        with self.assertRaises(RuntimeError):
            self.execute('presentation',fail_second=True)

class CandidateTests(unittest.TestCase):
    setUp = fixtures.HarnessTests.setUp
    ref = fixtures.HarnessTests.ref
    refresh = fixtures.HarnessTests.refresh
    save = fixtures.HarnessTests.save
    review = fixtures.HarnessTests.review
    evaluate = fixtures.HarnessTests.evaluate
    def test_candidate_escape_rejected(self):
        self.assertEqual(c.evaluate(self.root,'04','source',self.manifest_path,self.root.parent)['status'],'error')
    def test_optional_profile_requires_transfer(self):
        self.manifest['review_profile']='personal-projects-v1';self.save();self.review()
        out=self.evaluate();self.assertEqual(out['status'],'incomplete')
        self.assertTrue(any(x['id']=='pedagogy.transfer' for x in out['checks']))
    def test_symlink_cannot_impersonate_candidate_source(self):
        candidate=self.root/'.work/candidate';folder=candidate/'lessons/lesson-04';folder.mkdir(parents=True)
        for role,name in c.SOURCE_FILES.items():
            (folder/name).symlink_to(self.lesson/name);self.manifest['files'][role]={'path':str((folder/name).relative_to(self.root)),'sha256':c.digest(self.lesson/name)}
        self.save();self.assertEqual(c.evaluate(self.root,'04','source',self.manifest_path,candidate)['status'],'blocked')

class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        p=self.root/'result.json';p.write_text(json.dumps({'status':'passed','files':{},'checks':[{'id':'pedagogy.transfer','status':'pass'}]}));ref={'path':'result.json','sha256':c.digest(p)}
        conditions={k:'fixed' for k in compare.CONDITIONS}
        self.exp={'limits':{'calls':20,'seconds':100,'tokens':1000},'targets':['pedagogy.transfer'],'runs':[{'id':k,'kind':k,'round':1,'conditions':dict(conditions),'usage':{'calls':1,'seconds':2,'tokens':10},'result':ref} for k in ('baseline','candidate')]}
    def test_tie_retains_parent(self):self.assertEqual(compare.compare(self.root,self.exp)['outcomes'][0]['decision'],'retain_baseline')
    def test_missing_usage_stops(self):
        self.exp['runs'][1]['usage']['tokens']=None;self.assertTrue(compare.compare(self.root,self.exp)['stop'])
    def test_budget_stops(self):
        self.exp['limits']['calls']=1;self.assertTrue(compare.compare(self.root,self.exp)['stop'])
    def test_exact_budget_stops_without_claiming_overrun(self):
        self.exp['limits']['calls']=2
        result=compare.compare(self.root,self.exp)
        self.assertTrue(result['stop'])
        self.assertFalse(result['budget_exceeded'])
    def test_condition_difference_not_adopted(self):
        self.exp['runs'][1]['conditions']['model']='different';self.assertIn('比较条件不同',compare.compare(self.root,self.exp)['outcomes'][0]['reasons'])
    def test_composition_requires_own_result(self):
        self.exp['runs'][1]['kind']='composition';self.exp['runs'][1]['result']['sha256']='0'*64
        with self.assertRaises(ValueError):compare.compare(self.root,self.exp)
    def test_round_limit(self):
        self.exp['runs'][1]['round']=3
        with self.assertRaises(ValueError):compare.compare(self.root,self.exp)
if __name__=='__main__':unittest.main()
