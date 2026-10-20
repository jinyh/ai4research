#!/usr/bin/env python3
"""只读核对逐页母稿与 PPTX 实际屏显；论文中的分钟数交语义复核。"""
from __future__ import annotations

import argparse
import html
import posixpath
import re
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def normalized(text: str) -> str:
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', text))


def pages_from_markdown(md: str) -> list[tuple[str, str, str]]:
    return re.findall(r'^## P(\d+)｜([^\n]+)\n(.*?)(?=^## P|\Z)', md, re.M | re.S)


def plain(text: str) -> str:
    text = re.sub(r'!?\[([^]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'<br\s*/?>', ' ', text, flags=re.I)
    text = re.sub(r'(`+|\*\*)', '', text)
    text = re.sub(r'\*([^*\n]+)\*', r'\1', text)
    text = re.sub(r'(?<!_)__([^_\n]+)__(?!_)', r'\1', text)
    text = re.sub(r'(?<!\w)_([^_\n]+)_(?!\w)', r'\1', text)
    text = re.sub(r'~~([^~\n]+)~~', r'\1', text)
    return html.unescape(text).strip()


def screen_items(body: str) -> list[str]:
    match = re.search(r'### 屏显内容\n(.*?)(?=\n### |\Z)', body, re.S)
    if not match:
        raise ValueError('缺屏显内容段')
    items = []
    for raw in match[1].strip().splitlines():
        line = raw.strip()
        if not line or line.startswith('```') or re.fullmatch(r'[-*_]{3,}', line):
            continue
        if line.startswith('|') and line.endswith('|'):
            cells = re.split(r'(?<!\\)\|', line[1:-1])
            if all(re.fullmatch(r'\s*:?-+:?\s*', cell) for cell in cells):
                continue
        else:
            line = re.sub(r'^(?:[-*+]\s+(?:\[[ xX]\]\s*)?|\d+[.)]\s+|>\s*)', '', line)
            cells = line.split(' / ')
        items.extend(plain(cell.replace('\\|', '|')) for cell in cells if plain(cell))
    return items


def resolve_part(owner: str, target: str) -> str:
    return target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(owner), target))


def read_pptx(pptx: Path) -> list[dict]:
    with zipfile.ZipFile(pptx) as z:
        pres = ET.fromstring(z.read('ppt/presentation.xml'))
        rels = {x.attrib['Id']: x.attrib['Target'] for x in ET.fromstring(z.read('ppt/_rels/presentation.xml.rels'))}
        result = []
        for index, sid in enumerate(pres.findall('p:sldIdLst/p:sldId', NS), 1):
            name = resolve_part('ppt/presentation.xml', rels[sid.attrib['{' + NS['r'] + '}id']])
            xml = ET.fromstring(z.read(name))
            paragraphs = [''.join(t.text or '' for t in p.findall('.//a:t', NS)) for p in xml.findall('.//a:p', NS)]
            note = ''
            rel_name = posixpath.join(posixpath.dirname(name), '_rels', posixpath.basename(name) + '.rels')
            note_rels = [r for r in ET.fromstring(z.read(rel_name)) if r.attrib.get('Type', '').endswith('/notesSlide')] if rel_name in z.namelist() else []
            if len(note_rels) == 1:
                note_xml = ET.fromstring(z.read(resolve_part(name, note_rels[0].attrib['Target'])))
                note = ''.join(t.text or '' for t in note_xml.findall('.//a:t', NS))
            result.append({'page': index, 'paragraphs': paragraphs, 'notes': note,
                           'hidden': xml.attrib.get('show') == '0', 'part': name})
        return result


def check_alignment(mother: Path, pptx: Path) -> dict:
    pages = pages_from_markdown(mother.read_text(encoding='utf-8'))
    actual = read_pptx(pptx)
    failures, review = [], []
    if len(pages) != len(actual) or not pages:
        failures.append(f'页数：母稿 {len(pages)}，PPT {len(actual)}')
    for index, ((num, title, body), slide) in enumerate(zip(pages, actual), 1):
        tag = f'P{index:02}'
        if slide['hidden']:
            failures.append(f'{tag} 实际 PPT 页被隐藏')
        if int(num) != index:
            failures.append(f'{tag} 母稿页序为 P{num}')
        visible = normalized('\n'.join(slide['paragraphs']))
        if normalized(plain(title)) not in {normalized(p) for p in slide['paragraphs']}:
            failures.append(f'{tag} 标题不匹配：{title}')
        try:
            for item in screen_items(body):
                if normalized(item) not in visible:
                    failures.append(f'{tag} 屏显缺失：{item}')
        except ValueError as error:
            failures.append(f'{tag} {error}')
        for paragraph in slide['paragraphs']:
            if re.search(r'\d+\s*分钟', paragraph):
                if re.search(r'(?:课堂|本环节|本次练习|讨论用时|练习用时|阅读用时|准备用时)\s*[:：]?\s*\d+\s*分钟', paragraph):
                    failures.append(f'{tag} 屏显含明确课堂计时：{paragraph}')
                else:
                    review.append(f'{tag} 分钟语义待核：{paragraph}')
        for marker in (plain(title), '学生动作：', '[Sources]', '讲义映射：'):
            if normalized(marker) not in normalized(slide['notes']):
                failures.append(f'{tag} 备注缺失：{marker}')
    return {'pages': len(actual), 'failures': failures, 'review': review}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mother', type=Path)
    parser.add_argument('pptx', type=Path)
    args = parser.parse_args()
    try:
        result = check_alignment(args.mother, args.pptx)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError) as error:
        print(f'[ERROR] {error}')
        return 3
    for failure in result['failures']:
        print('[FAIL]', failure)
    for item in result['review']:
        print('[REVIEW]', item)
    if not result['failures']:
        print(f"[PASS] {result['pages']} 页标题、屏显逐项与备注映射一致")
        print('本检查不替代事实、视觉与实际教学复核。')
    return 1 if result['failures'] else 2 if result['review'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
