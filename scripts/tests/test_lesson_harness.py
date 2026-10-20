import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_lesson as harness
from check_slide_alignment import check_alignment, screen_items


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=harness.ROOT / '.work')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.lesson = self.root / 'lessons/lesson-04'
        self.lesson.mkdir(parents=True)
        self.md = '## 逐页映射\n\n| 页码 | 任务 |\n| --- | --- |\n| P01 | 标题 |\n\n## P01｜标题\n\n### 屏显内容\n\n| 对象 | 判断 |\n| --- | --- |\n| **原文** | `核验` |\n\n- 条目\n\n### 来源与事实边界\n原件\n'
        for role, filename in harness.SOURCE_FILES.items():
            text = self.md if role == 'slides' else '# 内容\n'
            if role == 'teaching_plan':
                text = '| 时长 | 环节 |\n| --- | --- |\n| 45 分钟 | 全班分享 |\n| 45 分钟 | 轮转讨论 |\n'
            (self.lesson / filename).write_text(text)
        for rule in harness.RULES:
            path = self.root / rule
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('规则\n')
        self.manifest = {'schema_version': 'graduate.lesson-evidence.v1', 'lesson': '04', 'stage': 'source',
                         'scope': list(harness.SOURCE_FILES), 'files': {}, 'rules': {}, 'reviews': [],
                         'review_delta': {'keep': ['现行主线'], 'repeat': [], 'change': []}}
        self.manifest_path = self.root / 'evidence.json'
        self.refresh()

    def ref(self, path):
        return {'path': str(path.relative_to(self.root)), 'sha256': harness.digest(path)}

    def refresh(self):
        self.manifest['files'].update({r: self.ref(self.lesson / f) for r, f in harness.SOURCE_FILES.items()})
        self.manifest['rules'] = {r: self.ref(self.root / r) for r in harness.RULES}
        self.save()

    def save(self):
        self.manifest_path.write_text(json.dumps(self.manifest, ensure_ascii=False))

    def review(self):
        bindings = {r: v['sha256'] for r, v in self.manifest['files'].items()}
        bindings.update({'rule:' + r: v['sha256'] for r, v in self.manifest['rules'].items()})
        for render in self.manifest.get('renders', []):
            bindings['render:' + str(render['page'])] = render['sha256']
        if 'contact_sheet' in self.manifest:
            bindings['contact_sheet'] = self.manifest['contact_sheet']['sha256']
        groups = ['handout', 'teaching', 'alignment']
        if self.manifest['stage'] == 'presentation':
            groups += ['visual', 'technical']
        checks = [dict(group=g, criterion=c, location='P01 / 正文', observation='测试工件观察',
                       impact='覆盖当前检查项', action='无需修改', recheck='已检查', status='pass',
                       blocking=False, pages=[1]) for g in groups for c in harness.GROUPS[g]]
        path = self.root / 'review.json'
        path.write_text(json.dumps({'reviewer': 'fixture', 'date': '2026-10-20', 'bindings': bindings, 'checks': checks}))
        self.manifest['reviews'] = [self.ref(path)]
        self.save()

    def evaluate(self):
        return harness.evaluate(self.root, '04', self.manifest['stage'], self.manifest_path)

    def pptx(self, body='标题</a:t></a:r></a:p><a:p><a:r><a:t>对象 判断 原文 核验 条目', order=(1,)):
        path = self.lesson / 'slides.pptx'
        ns = 'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
        with zipfile.ZipFile(path, 'w') as z:
            z.writestr('ppt/presentation.xml', f'<p:presentation {ns}><p:sldIdLst>' + ''.join(f'<p:sldId id="{i+255}" r:id="r{i}"/>' for i in order) + '</p:sldIdLst></p:presentation>')
            z.writestr('ppt/_rels/presentation.xml.rels', '<Relationships>' + ''.join(f'<Relationship Id="r{i}" Target="slides/slide{i}.xml"/>' for i in set(order)) + '</Relationships>')
            for i in set(order):
                z.writestr(f'ppt/slides/slide{i}.xml', f'<p:sld {ns}><a:p><a:r><a:t>{body}</a:t></a:r></a:p></p:sld>')
                z.writestr(f'ppt/slides/_rels/slide{i}.xml.rels', f'<Relationships><Relationship Type="x/notesSlide" Target="../notesSlides/notesSlide{i}.xml"/></Relationships>')
                z.writestr(f'ppt/notesSlides/notesSlide{i}.xml', f'<p:notes {ns}><a:p><a:r><a:t>标题 学生动作： [Sources] 讲义映射：</a:t></a:r></a:p></p:notes>')
        return path

    def test_markdown_table_list_formatting(self):
        self.assertEqual(screen_items(self.md.split('## P01｜标题')[1]), ['对象', '判断', '原文', '核验', '条目'])
        result = check_alignment(self.lesson / 'slides.md', self.pptx())
        self.assertEqual(result['failures'], [])
        self.assertEqual(screen_items('### 屏显内容\n我选择 ____，因为 ____。'), ['我选择 ____，因为 ____。'])
        self.assertEqual(screen_items('### 屏显内容\n- *重点* 与 _依据_，~~旧词~~，`logit_diff`'), ['重点 与 依据，旧词，logit_diff'])

    def test_inline_page_mapping_and_missing_entry(self):
        path = self.lesson / 'slides.md'
        inline = self.md[self.md.index('## P01｜'):]
        inline = inline.replace('### 屏显内容', '### 页面任务与内容映射\n\n- 页面任务：核对来源。\n- 讲义位置：handout.md §导读\n\n### 屏显内容')
        path.write_text(inline)
        self.refresh()
        row = next(x for x in self.evaluate()['checks'] if x['id'] == 'page_mapping')
        self.assertEqual(row['status'], 'pass')
        path.write_text(inline.replace('- 讲义位置：handout.md §导读', ''))
        self.refresh()
        row = next(x for x in self.evaluate()['checks'] if x['id'] == 'page_mapping')
        self.assertEqual(row['status'], 'fail')

    def test_missing_content_and_page(self):
        result = check_alignment(self.lesson / 'slides.md', self.pptx(body='标题'))
        self.assertTrue(any('原文' in x for x in result['failures']))
        result = check_alignment(self.lesson / 'slides.md', self.pptx(order=(1, 2)))
        self.assertTrue(any('页数' in x for x in result['failures']))

    def test_wrong_actual_order(self):
        # Actual order is read from presentation.xml, not ZIP member names.
        from check_slide_alignment import read_pptx
        slides = read_pptx(self.pptx(order=(2, 1)))
        self.assertEqual([s['part'] for s in slides], ['ppt/slides/slide2.xml', 'ppt/slides/slide1.xml'])
        (self.lesson / 'slides.md').write_text(self.md.replace('P01', 'P02'))
        self.refresh()
        self.assertEqual(self.evaluate()['status'], 'blocked')

    def test_source_requires_semantic_reviews(self):
        self.assertEqual(self.evaluate()['status'], 'incomplete')
        self.review()
        self.assertEqual(self.evaluate()['status'], 'passed')
        self.assertEqual(self.evaluate()['confirmations']['teacher']['status'], 'unverified')

    def test_stale_file_and_stale_review(self):
        self.review()
        (self.lesson / 'handout.md').write_text('修改后的讲义')
        self.assertEqual(self.evaluate()['status'], 'incomplete')
        self.refresh()
        self.assertEqual(self.evaluate()['status'], 'incomplete')
        self.review()
        self.assertEqual(self.evaluate()['status'], 'passed')

    def test_special_timing_and_individual_practice(self):
        self.review()
        self.assertEqual(self.evaluate()['status'], 'passed')
        path = self.lesson / 'teaching-plan.md'
        path.write_text(path.read_text().replace('全班分享', '个人实践'))
        self.refresh()
        self.review()
        self.assertEqual(self.evaluate()['status'], 'blocked')

    def test_alternative_timing_header_and_total_row(self):
        text = '| 环节 | 整数分钟 | 学生动作 |\n| --- | ---: | --- |\n| 分享 | 50 | 全员 |\n| 讨论 | 40 | 分组 |\n| **合计** | **90** | |'
        self.assertEqual(sum(r['minutes'] for r in harness.timing_rows(text)), 90)

    def test_missing_render_cannot_pass(self):
        self.manifest['stage'] = 'presentation'
        self.manifest['files']['pptx'] = self.ref(self.pptx())
        self.review()
        self.assertEqual(self.evaluate()['status'], 'incomplete')

    def test_complete_presentation_and_stale_render_binding(self):
        self.manifest['stage'] = 'presentation'
        ppt = self.pptx()
        self.manifest['files']['pptx'] = self.ref(ppt)
        image = self.root / 'render.png'
        image.write_bytes(b'fixture image bytes; visual review is independently recorded')
        h = harness.digest(ppt)
        self.manifest['renders'] = [dict(self.ref(image), page=1, pptx_sha256=h, renderer='fixture', renderer_version='1')]
        self.manifest['contact_sheet'] = dict(self.ref(image), pptx_sha256=h)
        self.review()
        self.assertEqual(self.evaluate()['status'], 'passed')
        self.manifest['renders'][0]['pptx_sha256'] = '0' * 64
        self.save()
        self.assertEqual(self.evaluate()['status'], 'incomplete')

    def test_render_order_and_review_coverage(self):
        self.manifest['stage'] = 'presentation'
        self.manifest['files']['pptx'] = self.ref(self.pptx())
        self.manifest['renders'] = []
        self.review()
        path = self.root / 'review.json'
        review = json.loads(path.read_text())
        for check in review['checks']:
            if check['group'] == 'visual':
                check['pages'] = []
        path.write_text(json.dumps(review))
        self.manifest['reviews'] = [self.ref(path)]
        self.save()
        self.assertEqual(self.evaluate()['status'], 'incomplete')

    def test_bad_json_reports_execution_error(self):
        self.manifest_path.write_text('{')
        self.assertEqual(self.evaluate()['status'], 'error')

    def test_check_does_not_write_sources(self):
        self.review()
        before = {p: harness.digest(p) for p in self.lesson.iterdir()}
        self.evaluate()
        self.assertEqual(before, {p: harness.digest(p) for p in self.lesson.iterdir()})

    def test_execution_error_not_pass(self):
        self.review()
        with patch.object(harness, 'check_links', side_effect=RuntimeError('fixture failure')):
            self.assertEqual(self.evaluate()['status'], 'error')

    def test_blocker_not_averaged_away(self):
        self.review()
        path = self.root / 'review.json'
        review = json.loads(path.read_text())
        review['checks'][0].update(status='fail', blocking=False)
        path.write_text(json.dumps(review))
        self.manifest['reviews'] = [self.ref(path)]
        self.save()
        self.assertEqual(self.evaluate()['status'], 'blocked')

    def test_source_minutes_need_review(self):
        result = check_alignment(self.lesson / 'slides.md', self.pptx(body='论文报告实验耗时 5 分钟'))
        self.assertEqual(len(result['review']), 1)
        self.assertFalse(any('课堂计时' in f for f in result['failures']))
        result = check_alignment(self.lesson / 'slides.md', self.pptx(body='课堂 5 分钟'))
        self.assertTrue(any('课堂计时' in f for f in result['failures']))

    def test_partial_review_not_pass(self):
        self.review()
        path = self.root / 'review.json'
        review = json.loads(path.read_text())
        review['checks'][0].update(status='partial', blocking=False)
        path.write_text(json.dumps(review))
        self.manifest['reviews'] = [self.ref(path)]
        self.save()
        self.assertEqual(self.evaluate()['status'], 'incomplete')

    def test_rule_change_invalidates_review(self):
        self.review()
        (self.root / harness.RULES[0]).write_text('新规则')
        self.refresh()
        self.assertEqual(self.evaluate()['status'], 'incomplete')

    def test_review_cannot_omit_criterion(self):
        self.review()
        path = self.root / 'review.json'
        review = json.loads(path.read_text())
        review['checks'].pop()
        path.write_text(json.dumps(review))
        self.manifest['reviews'] = [self.ref(path)]
        self.save()
        self.assertEqual(self.evaluate()['status'], 'incomplete')


if __name__ == '__main__':
    unittest.main()
