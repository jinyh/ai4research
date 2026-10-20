#!/usr/bin/env python3
"""课程材料只读验收；仅在 .work 写报告。0通过/1阻断/2缺证据/3执行故障。"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from check_links import check_links
from check_slide_alignment import check_alignment, pages_from_markdown

ROOT = Path(__file__).resolve().parent.parent
EXIT = {'passed': 0, 'blocked': 1, 'incomplete': 2, 'error': 3}
SOURCE_FILES = {'handout': 'handout.md', 'teaching_plan': 'teaching-plan.md',
                'slides': 'slides.md', 'task': 'judgment-task.md'}
OPTIONAL_FILES = {'teacher': 'judgment-teacher.md', 'keystone': 'keystone-design-spec.md'}
RULES = ['lessons/review-checklist.md', 'references/material-contracts.md',
         'course/ppt-quality-gates.md', 'lessons/ppt-design-criteria.md',
         'course/syllabus.md', 'course/micro-project.md']
GROUPS = {'handout': ['readability', 'evidence'], 'teaching': ['execution', 'independent_judgment'],
          'alignment': ['research_thread', 'handoff'],
          'visual': ['objects', 'readability', 'sequence'], 'technical': ['file', 'typography']}
PERSONAL_CRITERIA = ['challenge', 'transfer']
GROUPS['pedagogy'] = PERSONAL_CRITERIA


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def timing_rows(text: str) -> list[dict]:
    """只读取教案正式流程的单张时长表，不累加示例/逐页/历史时间。"""
    candidates = []
    rows = None
    time_index, activity_index = 0, 1
    for line in text.splitlines():
        if line.startswith('|'):
            cells = [c.strip().replace('**', '') for c in line.strip().strip('|').split('|')]
            headers = [i for i, c in enumerate(cells) if c in ('时长', '整数分钟')]
            if headers:
                time_index = headers[0]
                activity_index = cells.index('环节') if '环节' in cells else (1 if time_index == 0 else 0)
                rows = []
                candidates.append(rows)
            elif rows is not None and not all(re.fullmatch(r':?-+:?', c) for c in cells):
                if cells[0] in ('合计', '总计'):
                    continue
                raw_time = cells[time_index] if time_index < len(cells) else ''
                match = re.fullmatch(r'(\d+)\s*(?:分钟)?', raw_time)
                rows.append({'minutes': int(match[1]) if match else None,
                             'activity': cells[activity_index] if activity_index < len(cells) else '', 'raw': line})
        else:
            rows = None
    if len(candidates) != 1:
        raise ValueError(f'需一张明确的时长流程表，发现 {len(candidates)} 张；请人工定位现行安排')
    return candidates[0]


def evaluate(root: Path, lesson: str, stage: str, manifest_path: Path,
             candidate_root: Path | None = None) -> dict:
    result = {'schema_version': 'graduate.lesson-check.v1', 'lesson': lesson, 'stage': stage,
              'status': 'incomplete', 'checks': [], 'files': {}, 'review_delta': {},
              'confirmations': {}, 'course_baseline': {},
              'boundary': '仅当前范围与阶段；教师确认、PowerPoint和现场验证分别登记，不代表正式交付'}
    verified = {}

    def add(key, status, observation, *, location='', action='', blocking=False):
        result['checks'].append({'id': key, 'status': status, 'location': location,
                                 'observation': observation, 'action': action, 'blocking': blocking})

    def ref(value, label):
        if not isinstance(value, dict) or not isinstance(value.get('path'), str) or not re.fullmatch(r'[0-9a-f]{64}', str(value.get('sha256', ''))):
            add(label, 'unverified', '缺有效路径或 SHA-256', action='提供实际文件引用')
            return None
        path = (root / value['path']).resolve()
        if not path.is_relative_to(root.resolve()):
            add(label, 'unverified', '证据须位于仓库内部（含 .work）', location=value['path'])
            return None
        if not path.is_file() or digest(path) != value['sha256']:
            add(label, 'unverified', '文件缺失或版本已改变，旧证据失效', location=value['path'], action='重新检查当前文件并更新证据')
            return None
        verified[path] = value['sha256']
        result['files'][label] = value
        return path

    try:
        root = root.resolve()
        material_root = root
        if candidate_root is not None:
            material_root = candidate_root.resolve()
            if material_root == root / '.work' or not material_root.is_relative_to(root / '.work'):
                raise ValueError('candidate-root 必须是 .work 下的独立候选目录')
            result['candidate_root'] = str(material_root.relative_to(root))
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        verified[manifest_path] = digest(manifest_path)
        if manifest.get('schema_version') != 'graduate.lesson-evidence.v1' or manifest.get('lesson') != lesson or manifest.get('stage') != stage:
            raise ValueError('清单 schema_version、lesson 或 stage 与本次请求不一致')
        scope = manifest.get('scope')
        if not isinstance(scope, list) or not scope or len(set(scope)) != len(scope) or set(scope) - set(SOURCE_FILES | OPTIONAL_FILES | {'pptx': ''}):
            raise ValueError('scope 必须是不重复的材料角色列表')
        result['scope'] = scope
        folder = material_root / 'lessons' / f'lesson-{lesson}'
        files = manifest.get('files', {})
        paths = {}
        for role, filename in SOURCE_FILES.items():
            value = files.get(role)
            path = ref(value, role)
            if path and (path != (folder / filename).resolve() or not path.is_relative_to(material_root)):
                add(role + '.identity', 'fail', '课次内容必须指向唯一现行源文件', location=str(path), blocking=True)
            elif path:
                paths[role] = path
        for role in OPTIONAL_FILES:
            if role in scope and role not in files:
                add(role, 'unverified', '范围中的材料没有版本引用')
            if role in files:
                path = ref(files[role], role)
                if path:
                    if path != (folder / OPTIONAL_FILES[role]).resolve() or not path.is_relative_to(material_root):
                        add(role + '.identity', 'fail', '源材料指向错误课次或历史副本', blocking=True)
                    else:
                        paths[role] = path
        for name in RULES:
            entry = manifest.get('rules', {}).get(name)
            path = ref(entry, 'rule:' + name)
            if path and path != (root / name).resolve():
                add('rules.identity', 'fail', '规则引用指向错误文件', blocking=True)

        source_paths = []
        for index, value in enumerate(manifest.get('sources', [])):
            path = ref(value, f'source:{index}')
            if path and path.suffix == '.md':
                source_paths.append(path)
        broken, anchors, local = check_links(list(paths.values()) + source_paths)
        for item in broken:
            add('links', 'fail', item, blocking=True)
        for item in anchors + local:
            add('links', 'unverified', item, action='核对链接目标或来源副本')
        if not broken and not anchors and not local:
            add('links', 'pass', '当前材料内部链接有效')
        pages = []
        if 'slides' in paths:
            md = paths['slides'].read_text()
            pages = pages_from_markdown(md)
            nums = [int(p[0]) for p in pages]
            good = nums == list(range(1, len(pages) + 1)) and bool(pages)
            add('page_order', 'pass' if good else 'fail', f'母稿页序 {nums}', blocking=not good)
            mapping = re.search(r'^## 逐页映射[^\n]*\n(.*?)(?=^## |\Z)', md, re.M | re.S)
            mapped = re.findall(r'^\| P(\d+)\s*\|', mapping[1], re.M) if mapping else []
            if not mapping:
                # L3 uses a mapping block on every page instead of a summary table.
                mapped = [n for n, title, body in pages
                          if re.search(r'^### 页面任务与内容映射\s*$', body, re.M)
                          and re.search(r'^- 页面任务：\S', body, re.M)
                          and re.search(r'^- 讲义位置：handout\.md\s+§\S', body, re.M)]
            good = [int(n) for n in mapped] == nums and bool(nums)
            add('page_mapping', 'pass' if good else 'fail', f'映射记录 {len(mapped)} 条，正文 {len(pages)} 页', blocking=not good)
        if 'teaching_plan' in paths:
            try:
                timing = timing_rows(paths['teaching_plan'].read_text())
                if not timing or any(r['minutes'] is None for r in timing):
                    add('timing', 'fail', '流程包含无法解析的非整数时长', blocking=True)
                else:
                    total = sum(r['minutes'] for r in timing)
                    add('timing', 'pass' if total == 90 else 'fail', f'正式流程合计 {total} 分钟', blocking=total != 90)
                    for row in timing:
                        if re.search(r'个人实践|本人迁移|独立实践', row['activity']) and row['minutes'] > 15:
                            add('practice', 'fail', row['raw'], action='拆分个人实践并插入中点点评', blocking=True)
            except ValueError as error:
                add('timing', 'unverified', str(error), action='明确现行流程表；不推算时长')

        # Semantic review is explicitly authored; structural completeness never proves quality.
        needed = {'alignment'}
        profile = manifest.get('review_profile', 'legacy')
        if profile not in ('legacy', 'personal-projects-v1'):
            raise ValueError('未知 review_profile')
        result['review_profile'] = profile
        if profile == 'personal-projects-v1':
            needed.add('pedagogy')
        if 'handout' in scope:
            needed.add('handout')
        if set(scope) & {'teaching_plan', 'slides', 'task', 'teacher'}:
            needed.add('teaching')
        if stage == 'presentation':
            needed |= {'visual', 'technical'}
            path = ref(files.get('pptx'), 'pptx')
            if path:
                paths['pptx'] = path
                if 'slides' in paths:
                    align = check_alignment(paths['slides'], path)
                    for item in align['failures']:
                        add('ppt_alignment', 'fail', item, blocking=True)
                    for item in align['review']:
                        add('minute_semantics', 'unverified', item, action='在教学评审中按实际页记录语义判定')
                    if not align['failures']:
                        add('ppt_alignment', 'pass', f"实际 {align['pages']} 页屏显与备注检查通过")
                renders = manifest.get('renders', [])
                expected = list(range(1, len(pages) + 1))
                coverage = [r.get('page') for r in renders]
                if not expected or coverage != expected:
                    add('renders.coverage', 'unverified', '渲染页码须与完整母稿顺序逐页对应')
                for render in renders:
                    ref(render, 'render:' + str(render.get('page')))
                    if render.get('pptx_sha256') != files['pptx']['sha256'] or not render.get('renderer') or not render.get('renderer_version'):
                        add('renders.binding', 'unverified', '渲染缺当前 PPT 绑定或实际渲染器版本')
                sheet = manifest.get('contact_sheet', {})
                ref(sheet, 'contact_sheet')
                if sheet.get('pptx_sha256') != files['pptx']['sha256']:
                    add('contact_sheet.binding', 'unverified', '联系表未绑定当前 PPT')

        valid_criteria = set()
        bindings = {key: value['sha256'] for key, value in result['files'].items()
                    if not key.startswith('review:')}
        for index, review_ref in enumerate(manifest.get('reviews', [])):
            path = ref(review_ref, f'review:{index}')
            if not path:
                continue
            review = json.loads(path.read_text())
            if review.get('bindings') != bindings:
                add('review.binding', 'unverified', f'{path.name} 未绑定本轮全部有效材料、规则和呈现证据', action='重新评审并绑定当前证据')
                continue
            if not review.get('reviewer') or not review.get('date'):
                add('review.identity', 'unverified', '评审者或日期缺失')
                continue
            # Independently generated reviews must retain verifiable quotations.
            if review.get('method') == 'independent-session':
                from review_lesson import validate_review
                try:
                    validate_review(review, bindings, result['files'], root,
                                    {(c['group'], c['criterion']) for c in review.get('checks', [])})
                except ValueError as error:
                    add('review.citations', 'unverified', str(error))
                    continue
            for check in review.get('checks', []):
                group, criterion = check.get('group'), check.get('criterion')
                if group not in needed or criterion not in GROUPS[group]:
                    continue
                key = f'{group}.{criterion}'
                if key in valid_criteria:
                    raise ValueError(f'评审项重复：{key}')
                required = ['location', 'observation', 'impact', 'action', 'recheck']
                if any(not isinstance(check.get(k), str) or not check[k].strip() for k in required):
                    add(key, 'unverified', '缺位置、观察、影响、修改动作或复验说明')
                    continue
                status = check.get('status')
                if status not in ('pass', 'partial', 'fail', 'unverified', 'not_applicable') or not isinstance(check.get('blocking'), bool):
                    raise ValueError(f'{key} 评级或 blocking 无效')
                if group in ('visual', 'technical') and check.get('pages') != list(range(1, len(pages) + 1)):
                    add(key, 'unverified', '最终呈现评审须覆盖全部页面')
                    continue
                valid_criteria.add(key)
                add(key, status, check['observation'], location=check['location'], action=check['action'], blocking=check['blocking'] or status == 'fail')
                result['checks'][-1].update(impact=check['impact'], recheck=check['recheck'], reviewer=review['reviewer'])
            # Explicit semantic dispositions only address minute warnings, never other failures.
            for disposition in review.get('minute_dispositions', []):
                for check in result['checks']:
                    if check['id'] == 'minute_semantics' and check['observation'] == disposition.get('observation') and disposition.get('reason'):
                        check['status'] = 'pass' if disposition.get('kind') == 'source_content' else 'fail'
                        check['blocking'] = check['status'] == 'fail'
                        check['action'] = disposition['reason']
        for group in sorted(needed):
            for criterion in GROUPS[group]:
                if f'{group}.{criterion}' not in valid_criteria:
                    add(f'{group}.{criterion}', 'unverified', '缺当前版本的有效逐项评审', action='检查实际材料并填写观察证据')
        result['review_delta'] = manifest.get('review_delta', {})
        for field in ('keep', 'repeat', 'change'):
            if not isinstance(result['review_delta'].get(field), list):
                add('review_delta', 'unverified', f'缺本轮 {field} 差量记录')
        # These are separate from stage acceptance; no implicit approval from agent reports.
        for name in ('teacher', 'powerpoint', 'projection', 'student_trial'):
            value = manifest.get('confirmations', {}).get(name, {'status': 'unverified'})
            if value.get('status') == 'verified':
                proof = ref(value.get('evidence'), 'confirmation:' + name)
                target_hash = files.get('pptx', {}).get('sha256') if name in ('powerpoint', 'projection') else files.get('handout', {}).get('sha256')
                if not proof or value.get('target_sha256') != target_hash:
                    value = {'status': 'unverified', 'reason': '缺当前版本确认依据'}
            result['confirmations'][name] = value
        for path, fingerprint in verified.items():
            if not path.is_file() or digest(path) != fingerprint:
                add('changed_during_check', 'unverified', f'检查过程中证据变化：{path.name}')
        checks = result['checks']
        result['status'] = ('blocked' if any(c['blocking'] for c in checks) else
                            'incomplete' if any(c['status'] in ('unverified', 'partial') for c in checks) else 'passed')
    except Exception as error:
        result['status'] = 'error'
        add('execution', 'error', f'{type(error).__name__}: {error}')
    return result


def course_baseline(root: Path) -> dict:
    report = {}
    for name in ('check_course_consistency.py', 'check_links.py'):
        try:
            proc = subprocess.run([sys.executable, str(root / 'scripts' / name)], cwd=root,
                                  capture_output=True, text=True, timeout=60)
            report[name] = {'exit_code': proc.returncode, 'output': proc.stdout + proc.stderr}
        except (OSError, subprocess.TimeoutExpired) as error:
            report[name] = {'exit_code': 3, 'output': str(error)}
    return report


def write_report(result: dict, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    (output / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    lines = [f"# L{result['lesson']} {result['stage']} 检查", '', f"状态：{result['status']}", '', result['boundary'], '', '## 本轮检查', '']
    for check in result['checks']:
        lines.append(f"- **{check['status']} · {check['id']}** {check['location']}：{check['observation']}；处理：{check['action'] or '无需修订'}")
    lines += ['', '## 独立确认', '', '```json', json.dumps(result['confirmations'], ensure_ascii=False, indent=2), '```', '', '## 修订差量', '', '```json', json.dumps(result['review_delta'], ensure_ascii=False, indent=2), '```', '', '## 全课背景检查（不计入本课阶段状态）', '']
    for name, value in result['course_baseline'].items():
        lines += [f"### {name} · exit {value['exit_code']}", '', '```text', value['output'].strip(), '```', '']
    (output / 'report.md').write_text('\n'.join(lines) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lesson', required=True)
    parser.add_argument('--stage', required=True, choices=['source', 'presentation'])
    parser.add_argument('--evidence', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--candidate-root', type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r'0[1-9]|1[0-6]', args.lesson):
        parser.error('lesson 必须是 01–16')
    output = args.output.resolve()
    if not output.is_relative_to((ROOT / '.work').resolve()):
        parser.error('报告仅可写入仓库 .work/')
    if any((output / name).exists() for name in ('result.json', 'report.md')):
        parser.error('本轮报告已存在，请使用新的输出目录保留原记录')
    result = evaluate(ROOT, args.lesson, args.stage, args.evidence.resolve(), args.candidate_root)
    result['course_baseline'] = course_baseline(ROOT)
    write_report(result, output)
    print(f"[{result['status'].upper()}] L{args.lesson} {args.stage}；报告：{output / 'report.md'}")
    return EXIT[result['status']]


if __name__ == '__main__':
    raise SystemExit(main())
