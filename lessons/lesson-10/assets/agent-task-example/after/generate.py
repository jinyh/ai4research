REQUIRED_FIELDS = ("paper_id", "summary")


def normalize_record(record):
    missing = [field for field in REQUIRED_FIELDS if field not in record]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    return {"paper_id": record["paper_id"], "summary": record["summary"].strip()}
