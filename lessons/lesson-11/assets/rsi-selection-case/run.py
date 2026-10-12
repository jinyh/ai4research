#!/usr/bin/env python3
"""Frozen, CPU-only selection experiment. Python standard library only.

The selector accepts observed counts, never oracle probabilities or final data.
Simulation references are available only to the environment and reporting stage.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from collections import defaultdict
from pathlib import Path

METHODS = ("history", "uniform", "random")
SCENARIOS = ("equal", "heterogeneous")
METRICS = ("history_optimism", "selection_loss", "final_score", "parent_difference", "unknown_fraction")


def seed_for(root: int, *parts: object) -> int:
    key = json.dumps([root, *parts], separators=(",", ":"), ensure_ascii=True)
    return int.from_bytes(hashlib.sha256(key.encode()).digest()[:8], "big")


def validate_config(config: dict) -> None:
    if config.get("schema_version") != 1:
        raise ValueError("Unsupported schema_version")
    for name in ("pool_size", "history_trials", "validation_trials_per_candidate", "final_trials", "repeats", "bootstrap_samples"):
        if type(config.get(name)) is not int or config[name] <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if config["pool_size"] < 2:
        raise ValueError("pool_size must be at least two")
    counts = config.get("candidate_counts")
    if not isinstance(counts, list) or not counts or counts != sorted(set(counts)):
        raise ValueError("candidate_counts must be nonempty, increasing and unique")
    if any(type(k) is not int or k < 1 or k > config["pool_size"] for k in counts):
        raise ValueError("candidate_counts exceed the fixed pool")
    if type(config.get("root_seed")) is not int:
        raise ValueError("root_seed must be an integer")
    p = config.get("equal_probability")
    bounds = config.get("heterogeneous_range", [])
    if not isinstance(p, (int, float)) or not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError("Invalid equal_probability")
    if len(bounds) != 2 or not all(isinstance(x, (int, float)) and math.isfinite(x) for x in bounds) or not 0 <= bounds[0] <= bounds[1] <= 1:
        raise ValueError("Invalid heterogeneous_range")


def choose(observations: dict[int, tuple[int, int]]) -> int:
    """Unknown observations cannot be ranked; ties use the fixed numeric ID."""
    if not observations:
        raise ValueError("Missing candidate observations")
    available = []
    for candidate, (successes, trials) in observations.items():
        if type(candidate) is not int or type(successes) is not int or type(trials) is not int or not 0 <= successes <= trials:
            raise ValueError("Invalid observation counts")
        if trials:
            available.append((candidate, successes / trials))
    if not available:
        raise ValueError("No observed candidate; all candidates are unknown")
    return max(available, key=lambda item: (item[1], -item[0]))[0]


def probabilities(config: dict, scenario: str) -> list[float]:
    n = config["pool_size"]
    if scenario == "equal":
        return [config["equal_probability"]] * n
    low, high = config["heterogeneous_range"]
    values = [low + (high - low) * i / (n - 1) for i in range(n)]
    random.Random(seed_for(config["root_seed"], "pool_order")).shuffle(values)
    return values


def sample_counts(probability: float, trials: int, seed: int) -> tuple[int, int]:
    rng = random.Random(seed)
    return sum(rng.random() < probability for _ in range(trials)), trials


def simulate(config: dict) -> tuple[list[dict], list[dict]]:
    validate_config(config)
    raw, results = [], []
    root = config["root_seed"]
    for scenario in SCENARIOS:
        truth = probabilities(config, scenario)
        for repeat in range(config["repeats"]):
            cache = {}

            def observe(role: str, candidate: int, trials: int, k: int = 0) -> tuple[int, int]:
                key = (role, candidate, k)
                if key not in cache:
                    seed = seed_for(root, scenario, repeat, role, candidate, k)
                    counts = sample_counts(truth[candidate], trials, seed)
                    record_id = f"{scenario}-R{repeat:04d}-{role}-K{k:02d}-C{candidate:02d}"
                    cache[key] = (counts, record_id)
                    raw.append(dict(record_id=record_id, scenario=scenario, repeat=repeat,
                                    role=role, candidate_count=k, candidate_id=candidate,
                                    successes=counts[0], trials=trials, seed=seed))
                return cache[key][0]

            # Shared frozen evidence for the nested candidate subsets.
            history = {i: observe("history", i, config["history_trials"]) for i in range(max(config["candidate_counts"]))}
            uniform = {i: observe("validation_uniform", i, config["validation_trials_per_candidate"]) for i in range(max(config["candidate_counts"]))}
            frozen = []
            for k in config["candidate_counts"]:
                budget = k * config["validation_trials_per_candidate"]
                allocation_seed = seed_for(root, scenario, repeat, "allocation_random", k)
                rng = random.Random(allocation_seed)
                allocations = [0] * k
                for _ in range(budget):
                    allocations[rng.randrange(k)] += 1
                observations = {
                    "history": {i: history[i] for i in range(k)},
                    "uniform": {i: uniform[i] for i in range(k)},
                    "random": {i: observe("validation_random", i, allocations[i], k) for i in range(k)},
                }
                for method in METHODS:
                    observed = observations[method]
                    chosen = choose(observed)
                    role = {"history": "history", "uniform": "validation_uniform", "random": "validation_random"}[method]
                    frozen.append((k, method, chosen, sum(n == 0 for _, n in observed.values()) / k,
                                   cache[(role, chosen, k if method == "random" else 0)][1],
                                   allocation_seed if method == "random" else ""))

            # Reveal final evidence only after ALL selections for this repeat are frozen.
            final = {i: observe("final", i, config["final_trials"]) for i in sorted({0, *(row[2] for row in frozen)})}
            parent_score = final[0][0] / final[0][1]
            for k, method, chosen, unknown, evidence_id, allocation_seed in frozen:
                selected_score = final[chosen][0] / final[chosen][1]
                results.append(dict(
                    result_id=f"{scenario}-R{repeat:04d}-K{k:02d}-{method}",
                    scenario=scenario, repeat=repeat, candidate_count=k, method=method,
                    selected_candidate=chosen, parent_candidate=0, selection_evidence_id=evidence_id,
                    final_evidence_id=cache[("final", chosen, 0)][1],
                    parent_evidence_id=cache[("final", 0, 0)][1], allocation_seed=allocation_seed,
                    oracle_probability=truth[chosen], pool_best_probability=max(truth[:k]),
                    history_optimism=history[chosen][0] / history[chosen][1] - truth[chosen],
                    selection_loss=max(truth[:k]) - truth[chosen], final_score=selected_score,
                    parent_difference=selected_score - parent_score, unknown_fraction=unknown,
                    history_cost=k * config["history_trials"],
                    additional_cost=0 if method == "history" else k * config["validation_trials_per_candidate"],
                    final_cost=config["final_trials"] * len({chosen, 0}),
                    shared_final_evidence=True,
                ))
    return raw, results


def mean_interval(values: list[float], rng: random.Random, samples: int) -> dict:
    n = len(values)
    if min(values) == max(values):
        return dict(mean=values[0], ci95=[values[0], values[0]], n=n)
    means = sorted(sum(values[i] for i in rng.choices(range(n), k=n)) / n for _ in range(samples))
    # Linear interpolation of the empirical bootstrap quantiles.
    def quantile(p):
        index = (samples - 1) * p
        low = int(index)
        high = min(low + 1, samples - 1)
        return means[low] + (means[high] - means[low]) * (index - low)
    return dict(mean=sum(values) / n, ci95=[quantile(0.025), quantile(0.975)], n=n)


def validate_records(raw: list[dict], results: list[dict], config: dict) -> None:
    """Auditable workflow contract: completeness, roles, costs and trace links."""
    validate_config(config)
    expected_raw = set()
    for scenario in SCENARIOS:
        for repeat in range(config["repeats"]):
            for role in ("history", "validation_uniform"):
                expected_raw.update((scenario, repeat, role, 0, i) for i in range(max(config["candidate_counts"])))
            for k in config["candidate_counts"]:
                expected_raw.update((scenario, repeat, "validation_random", k, i) for i in range(k))
            selected = {0, *(r["selected_candidate"] for r in results if r["scenario"] == scenario and r["repeat"] == repeat)}
            expected_raw.update((scenario, repeat, "final", 0, i) for i in selected)
    actual_raw = {(r["scenario"], r["repeat"], r["role"], r["candidate_count"], r["candidate_id"]) for r in raw}
    if actual_raw != expected_raw:
        raise ValueError("Missing or unexpected raw evidence")
    indexed = {row["record_id"]: row for row in raw}
    raw_groups = defaultdict(dict)
    for r in raw:
        key = (r["scenario"], r["repeat"], r["role"], r["candidate_count"])
        if r["candidate_id"] in raw_groups[key]:
            raise ValueError("Duplicate candidate evidence")
        raw_groups[key][r["candidate_id"]] = (r["successes"], r["trials"])
    if len(indexed) != len(raw):
        raise ValueError("Duplicate raw record IDs")
    expected = {(s, r, k, m) for s in SCENARIOS for r in range(config["repeats"]) for k in config["candidate_counts"] for m in METHODS}
    keys = [(row["scenario"], row["repeat"], row["candidate_count"], row["method"]) for row in results]
    if len(keys) != len(set(keys)) or set(keys) != expected:
        raise ValueError("Missing or duplicate result rows")
    for row in raw:
        canonical_id = f'{row["scenario"]}-R{row["repeat"]:04d}-{row["role"]}-K{row["candidate_count"]:02d}-C{row["candidate_id"]:02d}'
        if row["record_id"] != canonical_id or row["seed"] != seed_for(config["root_seed"], row["scenario"], row["repeat"], row["role"], row["candidate_id"], row["candidate_count"]):
            raise ValueError("Changed evidence ID or random stream")
        if not 0 <= row["successes"] <= row["trials"] or row["trials"] < 0:
            raise ValueError("Invalid raw counts")
    for row in results:
        k, method = row["candidate_count"], row["method"]
        if row["result_id"] != f'{row["scenario"]}-R{row["repeat"]:04d}-K{k:02d}-{method}':
            raise ValueError("Changed result ID")
        if row["parent_candidate"] != 0 or row["final_cost"] != config["final_trials"] * len({0, row["selected_candidate"]}):
            raise ValueError("Parent or final cost mismatch")
        if any(not math.isfinite(row[m]) for m in (*METRICS, "oracle_probability", "pool_best_probability")):
            raise ValueError("Nonfinite report metric")
        role = {"history": "history", "uniform": "validation_uniform", "random": "validation_random"}[method]
        source = raw_groups[(row["scenario"], row["repeat"], role, k if method == "random" else 0)]
        group = {i: counts for i, counts in source.items() if i < k}
        if len(group) != k or choose(group) != row["selected_candidate"]:
            raise ValueError("Incomplete selection evidence or changed selection")
        if row["history_cost"] != k * config["history_trials"] or row["additional_cost"] != (0 if method == "history" else k * config["validation_trials_per_candidate"]):
            raise ValueError("Budget mismatch")
        expected_trials = row["history_cost"] if method == "history" else row["additional_cost"]
        if sum(n for _, n in group.values()) != expected_trials:
            raise ValueError("Raw execution budget mismatch")
        for field, expected_role, candidate in (("selection_evidence_id", role, row["selected_candidate"]),
                                               ("final_evidence_id", "final", row["selected_candidate"]),
                                               ("parent_evidence_id", "final", 0)):
            r = indexed.get(row[field])
            if r is None or r["role"] != expected_role or r["candidate_id"] != candidate or r["scenario"] != row["scenario"] or r["repeat"] != row["repeat"] or r["candidate_count"] != (k if field == "selection_evidence_id" and method == "random" else 0):
                raise ValueError("Missing or wrong-role evidence")
        f, p = indexed[row["final_evidence_id"]], indexed[row["parent_evidence_id"]]
        if f["trials"] != config["final_trials"] or p["trials"] != config["final_trials"]:
            raise ValueError("Final evaluation budget mismatch")
        if abs(row["final_score"] - f["successes"] / f["trials"]) > 1e-12 or abs(row["parent_difference"] - (f["successes"] / f["trials"] - p["successes"] / p["trials"])) > 1e-12:
            raise ValueError("Report does not match final evidence")
        if abs(row["selection_loss"] - (row["pool_best_probability"] - row["oracle_probability"])) > 1e-12:
            raise ValueError("Oracle reference metric mismatch")
        truth = probabilities(config, row["scenario"])
        h = raw_groups[(row["scenario"], row["repeat"], "history", 0)][row["selected_candidate"]]
        if abs(row["oracle_probability"] - truth[row["selected_candidate"]]) > 1e-12 or abs(row["pool_best_probability"] - max(truth[:k])) > 1e-12:
            raise ValueError("Changed oracle reference")
        if abs(row["history_optimism"] - (h[0] / h[1] - truth[row["selected_candidate"]])) > 1e-12 or abs(row["unknown_fraction"] - sum(n == 0 for _, n in group.values()) / k) > 1e-12:
            raise ValueError("Reported metric differs from frozen counts")


def summarize(results: list[dict], config: dict) -> dict:
    groups = defaultdict(list)
    for row in results:
        groups[(row["scenario"], row["candidate_count"], row["method"])].append(row)
    summary = dict(config=config, groups=[], paired_differences=[], actual_technical_failures=0,
                   failure_note="完整实跑未发生技术失败；测试中的注入故障是测试材料。",
                   cost_note="组内 final_cost 含所选候选与父版本；跨方法/候选数量共享记录，总成本不能直接相加。",
                   uncertainty_unit="independent repeated simulation conditional on a frozen candidate pool")
    for (scenario, k, method), rows in sorted(groups.items()):
        metrics = {metric: mean_interval([float(row[metric]) for row in rows],
                   random.Random(seed_for(config["root_seed"], "statistics", scenario, k, method, metric)), config["bootstrap_samples"]) for metric in METRICS}
        summary["groups"].append(dict(scenario=scenario, candidate_count=k, method=method, metrics=metrics,
                                     history_cost=rows[0]["history_cost"], additional_cost=rows[0]["additional_cost"],
                                     evidence_ids=[row["result_id"] for row in rows]))
    for scenario in SCENARIOS:
        for k in config["candidate_counts"]:
            a = {row["repeat"]: row for row in groups[(scenario, k, "uniform")]}
            b = {row["repeat"]: row for row in groups[(scenario, k, "random")]}
            metrics = {metric: mean_interval([a[i][metric] - b[i][metric] for i in sorted(a)],
                       random.Random(seed_for(config["root_seed"], "paired_statistics", scenario, k, metric)), config["bootstrap_samples"])
                       for metric in ("selection_loss", "final_score", "parent_difference")}
            summary["paired_differences"].append(dict(scenario=scenario, candidate_count=k, contrast="uniform-minus-random", metrics=metrics))
    return summary


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def load_csv(path: Path, integer_fields: set[str], float_fields: set[str]) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for key in integer_fields:
            row[key] = int(row[key])
        for key in float_fields:
            row[key] = float(row[key])
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.json"))
    parser.add_argument("--output", type=Path, required=True, help="A NEW directory; existing evidence is never overwritten")
    parser.add_argument("--records", type=Path, help="Recompute report from an existing frozen raw/results directory")
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    validate_config(config)
    if args.output.exists():
        parser.error("Output directory already exists; select a new directory")
    if args.records:
        stored = json.loads((args.records / "config.json").read_text())
        if stored != config:
            raise ValueError("Frozen records/config mismatch")
        raw = load_csv(args.records / "raw-counts.csv", {"repeat", "candidate_count", "candidate_id", "successes", "trials", "seed"}, set())
        results = load_csv(args.records / "results.csv", {"repeat", "candidate_count", "selected_candidate", "parent_candidate", "history_cost", "additional_cost", "final_cost"}, set(METRICS) | {"oracle_probability", "pool_best_probability"})
    else:
        raw, results = simulate(config)
    validate_records(raw, results, config)
    print(f"Validated {len(raw)} raw records and {len(results)} result rows", flush=True)
    summary = summarize(results, config)
    summary["unique_execution_costs"] = {role: sum(row["trials"] for row in raw if row["role"] == role) for role in sorted({row["role"] for row in raw})}
    args.output.mkdir(parents=True)
    write_csv(args.output / "raw-counts.csv", raw)
    write_csv(args.output / "results.csv", results)
    (args.output / "config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    (args.output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.output.iterdir())}
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("Complete: all selections frozen before final evaluation; no technical failures", flush=True)


if __name__ == "__main__":
    main()
