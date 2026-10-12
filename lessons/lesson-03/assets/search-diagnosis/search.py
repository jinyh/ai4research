"""Local teaching index, not a scholarly database. AND groups, OR within each group."""
import argparse
import json
from pathlib import Path


def search(rows, groups, field='title'):
    if not groups or any(not group or any(not term.strip() for term in group) for group in groups):
        raise ValueError('each concept group must contain nonempty terms')
    return [row['id'] for row in rows if all(any(term.casefold() in row[field].casefold() for term in group) for group in groups)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--group', action='append', required=True, help='OR terms separated by |; repeat groups for AND')
    parser.add_argument('--field', choices=('title', 'keywords'), default='title')
    args = parser.parse_args()
    rows = json.loads(Path(__file__).with_name('index.json').read_text())
    groups = [value.split('|') for value in args.group]
    print(json.dumps({'provenance': 'local constructed teaching index; not live search', 'field': args.field,
                      'groups': groups, 'hits': search(rows, groups, args.field)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
