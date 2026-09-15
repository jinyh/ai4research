"""Replay explicitly constructed teaching outputs; no model calls or semantic scoring."""
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent

def load(name):
    return json.loads((ROOT / (name + '.json')).read_text(encoding='utf-8'))

def digest(name):
    return hashlib.sha256((ROOT / (name + '.json')).read_bytes()).hexdigest()

def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def read_events(out):
    path = out / 'events.jsonl'
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

def event(out, kind, **fields):
    events = read_events(out)
    value = {'event_id': len(events) + 1, 'time': datetime.now(timezone.utc).isoformat(), 'event': kind, **fields}
    with (out / 'events.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(value, ensure_ascii=False) + '\n')
    return value

def read_resource(role, resource, out):
    allowed = load('config')['allowed_resources'].get(role, [])
    if resource not in allowed:
        event(out, 'access_denied', role=role, resource=resource,
              boundary='teaching tool interface; not operating-system isolation')
        raise PermissionError(f'{role} cannot read resource {resource}')
    return load(resource)

def replay(out, fault_once=False):
    out.mkdir(parents=True, exist_ok=True)
    config = load('config')
    current = {name: digest(name) for name in ('sources', 'outputs', 'config')}
    identity_path = out / 'input-identity.json'
    if identity_path.exists() and json.loads(identity_path.read_text()) != current:
        raise ValueError('frozen inputs changed; use a new output directory/version')
    save(identity_path, current)
    outputs = read_resource('executor', 'outputs', out)
    read_resource('executor', 'sources', out)
    if len(outputs) != config['budget_jobs'] or len({o['job_id'] for o in outputs}) != len(outputs):
        raise ValueError('queue length or job identities do not match configuration')
    events = read_events(out)
    succeeded = {e['job_id']: e for e in events if e['event'] == 'replayed'}
    attempts = sum(e['event'] == 'attempt_started' for e in events)
    for record in outputs:
        job = record['job_id']
        if job in succeeded:
            continue
        if attempts >= config.get('budget_attempts', 8):
            event(out, 'budget_stop', attempts=attempts)
            raise RuntimeError('attempt budget exhausted')
        attempts += 1
        run_id = f'run-{attempts:03d}'
        event(out, 'attempt_started', run_id=run_id, job_id=job)
        already_failed = any(e['event'] == 'controlled_failure' and e.get('job_id') == job for e in read_events(out))
        if fault_once and job == config['fault_job'] and not already_failed:
            event(out, 'controlled_failure', run_id=run_id, job_id=job,
                  reason='deliberately injected teaching timeout; no network request')
            save(out / 'state.json', {'completed_jobs': sorted(succeeded), 'failed_job': job,
                                      'attempts': attempts, 'next_action': 'human review then resume'})
            return 2
        item = event(out, 'replayed', run_id=run_id, job_id=job, output=record,
                     provenance='saved constructed output replay; no model call')
        succeeded[job] = item
    save(out / 'state.json', {'completed_jobs': sorted(succeeded), 'failed_job': None,
                              'attempts': attempts, 'next_action': 'human annotation review then evaluate'})
    return 0

def evaluate(out):
    events = read_events(out)
    records = {e['job_id']: e['output'] for e in events if e['event'] == 'replayed'}
    expected = {o['job_id']: o for o in load('outputs')}
    if records != expected:
        raise ValueError('evaluation needs all six unchanged outputs; keep incomplete runs in the ledger')
    sources = {s['id']: s for s in read_resource('evaluator', 'sources', out)}
    gold = read_resource('evaluator', 'gold', out)
    annotations = read_resource('evaluator', 'annotations', out)
    gold_by_id = {g['id']: g for g in gold}
    if len(gold_by_id) != len(gold):
        raise ValueError('duplicate gold id')
    for g in gold:
        if not g['source_quote'] or g['source_quote'] not in sources[g['source_id']]['text']:
            raise ValueError('gold reference not found in source')
    expected_keys = {(job, g['id']) for job, o in records.items() for g in gold if g['source_id'] == o['source_id']}
    seen = set()
    totals = {c: {'missing': 0, 'total': 0} for c in ('card', 'free')}
    per_source = {sid: {c: {'missing': 0, 'total': 0} for c in totals} for sid in sources}
    for a in annotations:
        key = a['job_id'], a['gold_id']
        if key not in expected_keys or key in seen or type(a['retained']) is not bool:
            raise ValueError('annotation identity, duplicate or decision error')
        seen.add(key)
        record = records[a['job_id']]
        if a['retained'] and (not a['output_quote'] or a['output_quote'] not in record['text']):
            raise ValueError('retained annotation quote not found in output')
        if not a['retained'] and a['output_quote']:
            raise ValueError('omission must not claim a retained quote')
        for tally in (totals[record['condition']], per_source[record['source_id']][record['condition']]):
            tally['total'] += 1
            tally['missing'] += int(not a['retained'])
    if seen != expected_keys:
        raise ValueError('missing annotation; no silent exclusion')
    for group in [totals, *per_source.values()]:
        for tally in group.values():
            tally['rate'] = tally['missing'] / tally['total']
    summary = {'provenance': 'constructed teaching data; program aggregates supplied human-reference annotations',
               'source_objects': len(sources), 'outputs': len(records), 'aggregation': load('config')['aggregation'],
               'totals': totals, 'per_source': per_source,
               'card_minus_free': totals['card']['rate'] - totals['free']['rate'],
               'mechanism_H1': 'undetermined', 'measurement_A2': 'undetermined',
               'quality_A1': 'not_evaluated', 'range_A3': 'T03 is a retained adverse example',
               'references': {n: digest(n) for n in ('sources', 'outputs', 'gold', 'annotations', 'config')}}
    save(out / 'evaluation.json', summary)
    event(out, 'evaluation_written', report='evaluation.json', human_semantic_review='required')
    return summary

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['replay', 'evaluate', 'access-check'])
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--fault-once', action='store_true')
    parser.add_argument('--role', default='executor')
    parser.add_argument('--resource', default='gold')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    if args.action == 'replay':
        code = replay(args.out, args.fault_once)
        print('controlled failure retained; review then resume' if code else 'six constructed outputs replayed; ledger retained')
        return code
    if args.action == 'evaluate':
        result = evaluate(args.out)
        print(json.dumps({k: result[k] for k in ('totals', 'per_source', 'card_minus_free')}, ensure_ascii=False, indent=2))
    else:
        try:
            read_resource(args.role, args.resource, args.out)
            print('allowed by the teaching tool interface')
        except PermissionError as error:
            print(error)
            return 3
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
