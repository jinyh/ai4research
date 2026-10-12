"""CPU-only execution harness for student record-normalization implementations.

Execution never reads reference.json. This is an interface boundary, not a sandbox.
All inputs and reference checks are public constructed development examples.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def events(out):
    path = Path(out) / 'events.jsonl'
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


def append(out, kind, **data):
    row = {'event_id': len(events(out)) + 1, 'event': kind, **data}
    with (Path(out) / 'events.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(row, ensure_ascii=False) + '\n')


def unique(rows):
    ids = [r['case_id'] for r in rows]
    if not rows or any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        raise ValueError('cases must have unique nonempty identifiers')
    return set(ids)


def execute(inputs, implementation, out, fault_once=False):
    out = Path(out)
    rows = load(inputs)
    unique(rows)
    out.mkdir(parents=True, exist_ok=True)
    identity = {'inputs': digest(inputs), 'implementation': digest(implementation),
                'runner': digest(__file__), 'canonical_inputs': canonical_digest(rows), 'attempt_budget': len(rows) + 1,
                'provenance': 'actual CPU execution on constructed public inputs'}
    path = out / 'identity.json'
    if path.exists() and load(path) != identity:
        raise ValueError('frozen inputs or implementation changed; use a new output directory')
    save(path, identity)
    save(out / 'inputs.json', rows)
    spec = importlib.util.spec_from_file_location('student_normalizer', implementation)
    module = importlib.util.module_from_spec(spec)
    # Compile source directly: do not allow timestamp-granularity bytecode caches
    # to execute an older student implementation after a rapid local edit.
    exec(compile(Path(implementation).read_bytes(), str(implementation), 'exec'), module.__dict__)
    done = {e['case_id'] for e in events(out) if e['event'] == 'processed'}
    attempts = sum(e['event'] == 'attempt' for e in events(out))
    for index, row in enumerate(rows):
        cid = row['case_id']
        if cid in done:
            continue
        if attempts >= identity['attempt_budget']:
            append(out, 'budget_stop', attempts=attempts)
            raise RuntimeError('attempt budget exhausted')
        attempts += 1
        run_id = f'run-{attempts:03d}'
        append(out, 'attempt', run_id=run_id, case_id=cid)
        injected = any(e['event'] == 'controlled_failure' for e in events(out))
        if fault_once and index == 2 and not injected:
            append(out, 'controlled_failure', run_id=run_id, case_id=cid,
                   reason='injected interruption before processing; no model call')
            save(out / 'state.json', {'completed': sorted(done), 'next': cid, 'attempts': attempts})
            return 2
        start = time.perf_counter_ns()
        try:
            result = module.normalize_record(row['record'])
            json.dumps(result)  # the downstream contract requires serializable output
            accepted, error = True, None
        except Exception as exc:
            result, accepted, error = None, False, f'{type(exc).__name__}: {exc}'
        append(out, 'processed', run_id=run_id, case_id=cid, accepted=accepted,
               output=result, error=error, elapsed_ns=time.perf_counter_ns() - start)
        done.add(cid)
    save(out / 'state.json', {'completed': sorted(done), 'next': None, 'attempts': attempts})
    return 0


def evaluate(out, reference):
    out = Path(out)
    identity = load(out / 'identity.json')
    if digest(out / 'inputs.json') != identity['inputs']:
        # JSON formatting can differ in the saved snapshot; compare canonical bytes
        # to the recorded canonical hash created at execution instead of raw input.
        if canonical_digest(load(out / 'inputs.json')) != identity.get('canonical_inputs'):
            raise ValueError('input snapshot does not match execution identity')
    records = [e for e in events(out) if e['event'] == 'processed']
    expected = load(reference)['cases']
    input_ids = unique(load(out / 'inputs.json'))
    if unique(expected) != input_ids or unique(records) != input_ids:
        raise ValueError('evaluation must retain every input and exactly one outcome per case')
    by_id = {e['case_id']: e for e in records}
    good = [e for e in expected if e['accept']]
    bad = [e for e in expected if not e['accept']]
    kept = sum(by_id[e['case_id']]['accepted'] and by_id[e['case_id']]['output'] == e['expected'] for e in good)
    blocked = sum(not by_id[e['case_id']]['accepted'] for e in bad)
    result = {'provenance': 'actual execution; public constructed development checks',
              'identity': identity, 'reference_sha256': digest(reference),
              'events_sha256': digest(out / 'events.jsonl'), 'inputs': len(input_ids),
              'normal_total': len(good), 'normal_preserved': kept,
              'invalid_total': len(bad), 'invalid_rejected': blocked,
              'normal_errors': len(good) - kept, 'invalid_admitted': len(bad) - blocked,
              'implementation_time_ns': sum(e['elapsed_ns'] for e in records),
              'timing_scope': 'single local run; excludes setup/import/evaluation; not a speed benchmark',
              'controlled_failures': sum(e['event'] == 'controlled_failure' for e in events(out))}
    # A new reference produces a distinct report, never silently replacing a prior evaluation.
    target = out / ('evaluation-' + result['reference_sha256'][:12] + '-' + result['events_sha256'][:12] + '.json')
    save(target, result)
    return result


def canonical_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    run = subs.add_parser('execute')
    run.add_argument('--inputs', type=Path, default=Path(__file__).with_name('inputs.json'))
    run.add_argument('--implementation', type=Path, default=Path(__file__).with_name('baseline.py'))
    run.add_argument('--out', type=Path, required=True)
    run.add_argument('--fault-once', action='store_true')
    ev = subs.add_parser('evaluate')
    ev.add_argument('--out', type=Path, required=True)
    ev.add_argument('--reference', type=Path, default=Path(__file__).with_name('reference.json'))
    args = parser.parse_args()
    try:
        if args.command == 'execute':
            return execute(args.inputs, args.implementation, args.out, args.fault_once)
        print(json.dumps(evaluate(args.out, args.reference), ensure_ascii=False, indent=2))
        return 0
    except (ValueError, KeyError, OSError, RuntimeError) as exc:
        parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
