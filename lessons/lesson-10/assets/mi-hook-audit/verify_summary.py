#!/usr/bin/env python3
"""Verify summary statistics and snapshot invariants for L10 Case 2 (2026-10-20 GPT-2 IOI runs)."""

from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

EXPECTED_IDS = [f"store-0{i}" for i in range(1, 7)] + [f"park-0{i}" for i in range(1, 7)]
EXPECTED_POSITIONS = {
    "residual": 9,
    "single": 13,
}
EXPECTED_POSITION_LABELS = {
    "residual": "subject",
    "single": "last",
}


def check_run(prefix: str) -> None:
    policy_doc = json.loads((BASE / f"{prefix}-policy.json").read_text(encoding="utf-8"))
    rows = [
        json.loads(line)
        for line in (BASE / f"{prefix}-results.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    n = len(rows)
    assert n == 12, f"{prefix}: expected 12 rows, got {n}"

    ids = [r["id"] for r in rows]
    assert len(set(ids)) == 12 and set(ids) == set(EXPECTED_IDS), f"{prefix}: unexpected IDs {ids}"
    assert {r["split"] for r in rows} == {"dev"}, f"{prefix}: unexpected splits"
    families = [r["family"] for r in rows]
    assert families.count("store") == 6 and families.count("park") == 6, f"{prefix}: unexpected family counts"
    for r in rows:
        assert r["id"].startswith(r["family"] + "-"), f"{prefix}: id/family mismatch {r['id']} vs {r['family']}"

    patch_minus_corrupt = sum(r["patch"] - r["corrupt"] for r in rows) / n
    patch_minus_random = sum(r["patch"] - r["random"] for r in rows) / n
    max_noop_ld_error = max(abs(r["noop"] - r["corrupt"]) for r in rows)

    rec = policy_doc["recorded_summary"]
    assert abs(patch_minus_corrupt - rec["patch_minus_corrupt"]) < 1e-12
    assert abs(patch_minus_random - rec["patch_minus_random"]) < 1e-12
    assert abs(max_noop_ld_error - rec["max_noop_error"]) < 1e-12

    pol = policy_doc["policy"]
    layers = {r["layer"] for r in rows}
    positions = {r["position"] for r in rows}
    components = {r["component"] for r in rows}
    heads_set = {tuple(r["heads"]) for r in rows}

    assert layers == {pol["layer"]}, f"{prefix}: layer mismatch {layers} vs {pol['layer']}"
    assert pol["position"] == EXPECTED_POSITION_LABELS[prefix], (
        f"{prefix}: policy position label mismatch {pol['position']} vs {EXPECTED_POSITION_LABELS[prefix]}"
    )
    assert positions == {EXPECTED_POSITIONS[prefix]}, (
        f"{prefix}: position mismatch {positions} vs {EXPECTED_POSITIONS[prefix]}"
    )
    assert components == {pol["component"]}, f"{prefix}: component mismatch"
    assert heads_set == {tuple(pol["heads"])}, f"{prefix}: heads mismatch"

    print(
        f"[OK] {prefix}: layer={pol['layer']}, pos={EXPECTED_POSITIONS[prefix]} ({pol['position']}), "
        f"component={pol['component']}, heads={pol['heads']}, n={n} (store=6, park=6), "
        f"LD_patch-corrupt={patch_minus_corrupt:+.6f}, LD_patch-random={patch_minus_random:+.6f}, "
        f"max|LD_noop-LD_corrupt|={max_noop_ld_error:.6f}"
    )


def main() -> None:
    check_run("residual")
    check_run("single")


if __name__ == "__main__":
    main()
