#!/usr/bin/env python3
"""Real GPT-2 residual patching with explicit controls and immutable run folders.

Uses local model files only. Download the pinned public model before class.
The runner measures a research object; the research agent separately proposes
policies and interprets development feedback under WORKFLOW.md.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_cases(path, split):
    rows = [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
    ids = [row['id'] for row in rows]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate case IDs')
    families = {}
    for row in rows:
        families.setdefault(row['family'], set()).add(row['split'])
    if any(len(values) != 1 for values in families.values()):
        raise ValueError('Template family leaks across splits')
    selected = [row for row in rows if row['split'] == split]
    if not selected:
        raise ValueError('Empty split')
    return selected


def validate_policy(policy):
    if type(policy.get('layer')) is not int or not 0 <= policy['layer'] < 12:
        raise ValueError('layer must be an integer from 0 to 11')
    if policy.get('position') not in ('subject', 'last'):
        raise ValueError('position must be subject or last')
    component = policy.get('component', 'residual')
    if component not in ('residual', 'attention_heads'):
        raise ValueError('component must be residual or attention_heads')
    heads = policy.get('heads', [])
    if component == 'attention_heads':
        if (not isinstance(heads, list) or not heads or
            any(type(h) is not int or not 0 <= h < 12 for h in heads) or
            len(set(heads)) != len(heads)):
            raise ValueError('heads must be unique GPT-2 head indices 0–11')
    elif heads:
        raise ValueError('heads only applies to attention_heads')


def replace_slice(hidden, replacement, pos, dimensions=None):
    """Patch a position; head dimensions are concatenated attention outputs before c_proj."""
    changed = hidden.clone()
    if dimensions is None:
        changed[:, pos, :] = replacement
    else:
        changed[:, pos, dimensions] = replacement[:, dimensions]
    return changed


def summarize(rows):
    keys = ('clean', 'corrupt', 'noop', 'random', 'patch')
    mean = lambda seq: sum(seq) / len(seq)
    return {
        'n': len(rows),
        'mean_logit_difference': {k: mean([r[k] for r in rows]) for k in keys},
        'patch_minus_corrupt': mean([r['patch'] - r['corrupt'] for r in rows]),
        'patch_minus_random': mean([r['patch'] - r['random'] for r in rows]),
        'max_noop_error': max(abs(r['noop'] - r['corrupt']) for r in rows),
        'by_family': {f: mean([r['patch'] - r['corrupt'] for r in rows if r['family'] == f])
                      for f in sorted({r['family'] for r in rows})},
        'interpretation': 'Descriptive measurements on teaching templates; no significance or general circuit claim.'
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model-dir', type=Path, required=True)
    p.add_argument('--policy', type=Path, default=ROOT / 'policy-baseline.json')
    p.add_argument('--split', choices=['dev', 'heldout'], default='dev')
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--resume', action='store_true')
    p.add_argument('--fault-after', type=int, help='Controlled interruption after this many completed cases')
    args = p.parse_args()
    protocol = json.loads((ROOT / 'protocol.json').read_text())
    policy = json.loads(args.policy.read_text())
    validate_policy(policy)
    cases = load_cases(ROOT / 'cases.jsonl', args.split)
    # Read-only evaluator inputs; a revision gets a new output directory.
    identity = {'protocol_sha256': digest(ROOT / 'protocol.json'),
                'cases_sha256': digest(ROOT / 'cases.jsonl'),
                'policy_sha256': digest(args.policy), 'runner_sha256': digest(__file__),
                'model_revision': protocol['revision'], 'split': args.split}
    args.out.mkdir(parents=True, exist_ok=True)
    manifest_path = args.out / 'manifest.json'
    if any(args.out.iterdir()):
        if not args.resume or not manifest_path.exists():
            raise ValueError('Output is nonempty; use a new directory or resume the same run')
        old = json.loads(manifest_path.read_text())
        if old['identity'] != identity:
            raise ValueError('Cannot resume with changed inputs, policy, protocol or implementation')
        manifest = old
    else:
        manifest = {'identity': identity, 'created_utc': datetime.now(timezone.utc).isoformat(),
                    'policy': policy, 'protocol': protocol, 'python': platform.python_version(),
                    'hardware': platform.machine(), 'sessions': []}
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    import torch
    import transformers
    from transformers import AutoModelForCausalLM, AutoTokenizer
    torch.set_num_threads(protocol['threads'])
    torch.manual_seed(protocol['seed'])
    torch.use_deterministic_algorithms(True)
    start = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(args.model_dir, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(args.model_dir, local_files_only=True,
                                                torch_dtype=torch.float32, attn_implementation='eager')
    model.eval()
    manifest['versions'] = {'torch': torch.__version__, 'transformers': transformers.__version__}
    manifest['model_files_sha256'] = {name: digest(args.model_dir / name)
                                    for name in ('config.json', 'model.safetensors', 'tokenizer.json')}
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    results_path = args.out / 'results.jsonl'
    rows = [json.loads(l) for l in results_path.read_text().splitlines()] if results_path.exists() else []
    done = {row['id'] for row in rows}
    if len(done) != len(rows) or not done <= {r['id'] for r in cases}:
        raise ValueError('Inconsistent existing result IDs')
    events = args.out / 'events.jsonl'
    forwards = 0
    exit_code = 0
    try:
        for case in cases:
            if case['id'] in done:
                continue
            clean = tokenizer(case['clean'], return_tensors='pt')['input_ids']
            corrupt = tokenizer(case['corrupt'], return_tensors='pt')['input_ids']
            if clean.shape != corrupt.shape:
                raise ValueError('Clean and corrupt token lengths differ: ' + case['id'])
            target = tokenizer.encode(' ' + case['indirect_object'], add_special_tokens=False)
            subject = tokenizer.encode(' ' + case['subject'], add_special_tokens=False)
            if len(target) != 1 or len(subject) != 1:
                raise ValueError('Answer names must each be one token: ' + case['id'])
            occurrences = (clean[0] == subject[0]).nonzero().flatten().tolist()
            if len(occurrences) != 2:
                raise ValueError('Expected two clean subject occurrences: ' + case['id'])
            pos = occurrences[-1] if policy['position'] == 'subject' else clean.shape[1] - 1
            layer = model.transformer.h[policy['layer']]
            head_patch = policy.get('component', 'residual') == 'attention_heads'
            dimensions = None
            if head_patch:
                width = model.config.n_embd // model.config.n_head
                dimensions = [h * width + i for h in policy['heads'] for i in range(width)]
            cache = {}

            def capture(_module, _inputs, output):
                hidden = output[0] if isinstance(output, tuple) else output
                cache['value'] = hidden[:, pos, :].detach().clone()

            def forward(ids, replacement=None):
                nonlocal forwards
                def hook(_module, _inputs, output):
                    hidden = output[0] if isinstance(output, tuple) else output
                    changed = replace_slice(hidden, replacement, pos, dimensions)
                    return (changed,) + output[1:] if isinstance(output, tuple) else changed
                if head_patch:
                    def pre_hook(_module, inputs):
                        # c_proj receives concatenated head outputs, before projection.
                        hidden = inputs[0]
                        if replacement is None:
                            cache['value'] = hidden[:, pos, :].detach().clone()
                            return None
                        return (replace_slice(hidden, replacement, pos, dimensions),) + inputs[1:]
                    handle = layer.attn.c_proj.register_forward_pre_hook(pre_hook)
                else:
                    handle = layer.register_forward_hook(capture if replacement is None else hook)
                try:
                    with torch.inference_mode():
                        logits = model(ids, use_cache=False).logits[0, -1]
                    forwards += 1
                    return float(logits[target[0]] - logits[subject[0]])
                finally:
                    handle.remove()

            c = forward(clean)
            clean_activation = cache['value'].clone()
            b = forward(corrupt)
            corrupt_activation = cache['value'].clone()
            # Seed derives from case ID, so order and resume cannot change the control.
            seed = protocol['seed'] + int(hashlib.sha256(case['id'].encode()).hexdigest()[:8], 16)
            generator = torch.Generator().manual_seed(seed)
            shuffled = clean_activation[:, torch.randperm(clean_activation.shape[-1], generator=generator)]
            if head_patch:
                shuffled = clean_activation.clone()
                permutation = torch.randperm(len(dimensions), generator=generator)
                shuffled[:, dimensions] = clean_activation[:, [dimensions[i] for i in permutation.tolist()]]
            row = {'id': case['id'], 'family': case['family'], 'split': args.split,
                   'layer': policy['layer'], 'position': pos, 'clean': c, 'corrupt': b,
                   'component': policy.get('component', 'residual'), 'heads': policy.get('heads', []),
                   'noop': forward(corrupt, corrupt_activation),
                   'random': forward(corrupt, shuffled),
                   'patch': forward(corrupt, clean_activation)}
            with results_path.open('a') as f:
                f.write(json.dumps(row) + '\n')
            rows.append(row)
            with events.open('a') as f:
                f.write(json.dumps({'event': 'case-complete', 'id': case['id']}) + '\n')
            if args.fault_after is not None and len(rows) >= args.fault_after:
                with events.open('a') as f:
                    f.write(json.dumps({'event': 'controlled-interruption', 'completed': len(rows)}) + '\n')
                exit_code = 2
                break
    except Exception as error:
        with events.open('a') as f:
            f.write(json.dumps({'event': 'failure', 'type': type(error).__name__, 'message': str(error)}) + '\n')
        raise
    finally:
        manifest['sessions'].append({'seconds_including_model_load': time.perf_counter() - start,
                                     'forward_passes': forwards, 'completed_cases': len(rows)})
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    if len(rows) == len(cases):
        summary = summarize(rows)
        (args.out / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
        print(json.dumps(summary))
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
