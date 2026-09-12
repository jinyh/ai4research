import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def compute():
    config = load("config.json")
    records = load(config["input"])
    if len(records) != config["expected_records"]:
        raise ValueError("record count does not match config")
    field = config["condition_field"]
    missing = sum(not bool(record[field]) for record in records)
    return {
        "records": len(records),
        "missing": missing,
        "omission_rate": missing / len(records),
        "claim_status": "teaching_artifact_not_empirical",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = compute()
    if args.verify:
        if result != load("results.json"):
            raise SystemExit("results.json does not match recomputation")
        metric_events = [
            json.loads(line)
            for line in (ROOT / "run-log.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        metric = next(event for event in metric_events if event["event"] == "metric")
        for key in ("records", "missing", "omission_rate"):
            if metric[key] != result[key]:
                raise SystemExit("run-log.jsonl does not match recomputation")
        print(
            f"verified: {result['records']} records, {result['missing']} missing, "
            f"omission_rate={result['omission_rate']}"
        )
        return
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
