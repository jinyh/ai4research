#!/usr/bin/env python3
"""只读比较有界备课试验。候选不自动进入现行材料；未经校准只报告观察。"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import check_lesson as c

CONDITIONS=('task','input_snapshot','sources','model','tools','evaluator','budget')

def read_ref(root, ref):
    p=(root/ref['path']).resolve()
    if not p.is_relative_to(root.resolve()) or not p.is_file() or c.digest(p)!=ref['sha256']:
        raise ValueError('运行记录缺失、越界或哈希失效')
    return json.loads(p.read_text())

def compare(root, experiment):
    runs=experiment['runs']; limits=experiment['limits']
    if not runs or sum(r['kind']=='baseline' for r in runs)!=1:
        raise ValueError('需要恰好一个基线及运行记录')
    if len({r['id'] for r in runs})!=len(runs):raise ValueError('运行身份重复')
    if any(r['kind'] not in ('baseline','candidate','composition') for r in runs):raise ValueError('未知候选类型')
    if any(type(r['round']) is not int or r['round'] not in (1,2) for r in runs):raise ValueError('最多两轮')
    for round_id in (1,2):
        group=[r for r in runs if r['round']==round_id]
        if sum(r['kind']=='candidate' for r in group)>2 or sum(r['kind']=='composition' for r in group)>1:
            raise ValueError('每轮最多两个候选、一个组合')
    if set(limits)!= {'calls','seconds','tokens'} or any(type(v) not in (int,float) or v<=0 for v in limits.values()):
        raise ValueError('须预先声明正数调用、时间和token预算')
    totals={'calls':0,'seconds':0,'tokens':0}; unknown=False; loaded={}
    for run in runs:
        if set(run['conditions'])!=set(CONDITIONS):raise ValueError('比较条件不完整')
        result=read_ref(root,run['result']);loaded[run['id']]=result
        for label,ref in result['files'].items():
            path=(root/ref['path']).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file() or c.digest(path)!=ref['sha256']:
                raise ValueError('被比较结果已经过期：'+label)
        if result.get('status') not in c.EXIT:raise ValueError('未知阶段状态')
        for name in totals:
            value=run['usage'].get(name)
            if value is None:unknown=True
            elif type(value) not in (int,float) or value<0:raise ValueError('资源记录无效')
            else:totals[name]+=value
    baseline=next(r for r in runs if r['kind']=='baseline')
    budget_exceeded=any(totals[k]>limits[k] for k in totals)
    budget_exhausted=any(totals[k]>=limits[k] for k in totals)
    outcomes=[]
    for run in runs:
        if run is baseline:continue
        result=loaded[run['id']]; base=loaded[baseline['id']]
        reason=[]
        if run['conditions']!=baseline['conditions']:reason.append('比较条件不同')
        if budget_exceeded:reason.append('超过试验预算，不能作为预算内采用候选')
        if unknown:reason.append('资源记录不全，不能宣称同总成本优势')
        if result['status']!='passed':reason.append('候选阶段未通过')
        if base['status']=='error':reason.append('基线执行故障，不能用于效果比较')
        if experiment.get('calibration',{}).get('status')!='verified':reason.append('评审者尚未经教师校准')
        else:
            proof=read_ref(root,experiment['calibration']['evidence'])
            if not proof.get('teacher') or proof.get('status')!='verified':reason.append('缺有效教师校准记录')
        b={r['id']:r for r in base['checks']};a={r['id']:r for r in result['checks']}
        targets=experiment.get('targets',[])
        if not targets or any(t not in b or t not in a for t in targets):reason.append('缺预先指定目标的成对证据')
        improved=[t for t in targets if t in b and t in a and b[t]['status'] in ('fail','partial') and a[t]['status']=='pass']
        regressed=[k for k in b if k not in a or (b[k]['status']=='pass' and a[k]['status']!='pass')]
        if not improved:reason.append('未观察到预设目标的明确改善；同为通过需另作盲评，不能靠计数选优')
        if regressed:reason.append('存在退化或缺项：'+','.join(regressed))
        outcomes.append({'id':run['id'],'decision':'retain_baseline' if reason else 'candidate_for_teacher_review',
                         'improved':improved,'reasons':reason})
    return {'status':'incomplete' if unknown else 'passed','totals':totals,'limits':limits,'budget_exceeded':budget_exceeded,
            'stop':unknown or budget_exhausted,'outcomes':outcomes,
            'boundary':'仅比较已登记的运行；资源来自实际运行记录。不同内容版本的前后差异不证明Harness改进。无自动采用、无教师代签。'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--experiment',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(c.ROOT/'.work') or out.exists():p.error('output须为.work下的新目录')
    out.mkdir(parents=True)
    try:result=compare(c.ROOT,json.loads(a.experiment.read_text()))
    except Exception as e:result={'status':'error','error':f'{type(e).__name__}: {e}'}
    (out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (out/'report.md').write_text('# 候选比较\n\n```json\n'+json.dumps(result,ensure_ascii=False,indent=2)+'\n```\n')
    print(result['status']);return c.EXIT[result['status']]
if __name__=='__main__':raise SystemExit(main())
