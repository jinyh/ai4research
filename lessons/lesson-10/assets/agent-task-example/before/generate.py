def normalize_record(record):
    return {"paper_id": record["paper_id"], "summary": record["summary"].strip()}
