#!/usr/bin/env python3
"""Query public scholarly APIs and save reproducible raw/normalized records.

This script deliberately makes no screening, evidence-role, or verification-state
decisions. Those require the human review described in the parent SKILL.md.
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


USER_AGENT = "graduate-course-research-search/1.0 (public metadata research workflow)"
SOURCES = ("crossref", "openalex", "arxiv", "dblp", "semantic-scholar")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Query a public scholarly source and preserve raw and normalized results."
    )
    parser.add_argument("--source", required=True, choices=SOURCES)
    query_group = parser.add_mutually_exclusive_group(required=True)
    query_group.add_argument("--query", help="Convenience search text; mapping is source-specific.")
    query_group.add_argument(
        "--raw-query",
        help=(
            "Source-native query: URL parameters for Crossref/OpenAlex, exact "
            "search_query for arXiv, or q/query text for DBLP/Semantic Scholar."
        ),
    )
    query_group.add_argument("--doi", help="Exact DOI lookup; supported by Crossref only.")
    parser.add_argument("--author", help="Optional author text; Crossref uses a separate field.")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 200:
        parser.error("--limit must be between 1 and 200")
    if args.doi and args.source != "crossref":
        parser.error("--doi is supported only with --source crossref")
    if args.raw_query and args.author:
        parser.error("--author cannot be combined with --raw-query; encode it in the native query")
    return args


def build_request(args: argparse.Namespace) -> tuple[str, str]:
    if args.source == "crossref":
        if args.doi:
            doi = urllib.parse.quote(args.doi.strip(), safe="")
            return f"https://api.crossref.org/works/{doi}", "json"
        if args.raw_query:
            params = urllib.parse.parse_qsl(args.raw_query, keep_blank_values=True)
            if not any(key == "rows" for key, _value in params):
                params.append(("rows", str(args.limit)))
            return "https://api.crossref.org/works?" + urllib.parse.urlencode(params), "json"
        params: dict[str, str | int] = {
            "query.title": args.query,
            "rows": args.limit,
        }
        if args.author:
            params["query.author"] = args.author
        return "https://api.crossref.org/works?" + urllib.parse.urlencode(params), "json"

    query = args.raw_query or args.query or ""
    if args.author:
        query = f"{query} {args.author}".strip()

    if args.source == "openalex":
        if args.raw_query:
            params = urllib.parse.parse_qsl(args.raw_query, keep_blank_values=True)
            if not any(key == "per-page" for key, _value in params):
                params.append(("per-page", str(args.limit)))
            return "https://api.openalex.org/works?" + urllib.parse.urlencode(params), "json"
        params = {"search": query, "per-page": args.limit}
        return "https://api.openalex.org/works?" + urllib.parse.urlencode(params), "json"
    if args.source == "arxiv":
        search_query = query if args.raw_query else f'all:"{query}"'
        params = {
            "search_query": search_query,
            "start": 0,
            "max_results": args.limit,
        }
        return "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params), "xml"
    if args.source == "dblp":
        params = {"q": query, "h": args.limit, "format": "json"}
        return "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(params), "json"
    if args.source == "semantic-scholar":
        params = {
            "query": query,
            "limit": min(args.limit, 100),
            "fields": "title,authors,year,venue,externalIds,url,publicationTypes",
        }
        return (
            "https://api.semanticscholar.org/graph/v1/paper/search?"
            + urllib.parse.urlencode(params),
            "json",
        )
    raise ValueError(f"Unsupported source: {args.source}")


def build_ssl_context() -> tuple[ssl.SSLContext, str]:
    """Use a verified CA bundle, including common macOS package-manager paths."""
    verify_paths = ssl.get_default_verify_paths()
    candidates = [
        os.environ.get("SSL_CERT_FILE"),
        verify_paths.cafile,
        verify_paths.openssl_cafile,
        "/etc/ssl/cert.pem",
        "/opt/homebrew/etc/openssl@3/cert.pem",
        "/usr/local/etc/openssl@3/cert.pem",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return ssl.create_default_context(cafile=candidate), candidate
    return ssl.create_default_context(), "system-default"


def as_text(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, list):
        return as_text(value[0]) if value else None
    text = str(value).strip()
    return text or None


def first_year(value: Any) -> int | None:
    try:
        if isinstance(value, dict):
            parts = value.get("date-parts", [[]])
            return int(parts[0][0]) if parts and parts[0] else None
        if value:
            return int(str(value)[:4])
    except (TypeError, ValueError, IndexError):
        return None
    return None


def normalize_crossref(payload: dict[str, Any], exact_doi: bool) -> tuple[int | None, list[dict[str, Any]]]:
    message = payload.get("message", {})
    if exact_doi:
        items = [message] if message else []
        total = len(items)
    else:
        items = message.get("items", [])
        total = message.get("total-results")
    results = []
    for index, item in enumerate(items):
        authors = []
        for author in item.get("author", []):
            name = " ".join(filter(None, [author.get("given"), author.get("family")])).strip()
            if name:
                authors.append(name)
        doi = as_text(item.get("DOI"))
        results.append(
            {
                "source": "crossref",
                "source_id": doi,
                "title": as_text(item.get("title")),
                "authors": authors,
                "year": first_year(item.get("published") or item.get("issued")),
                "venue": as_text(item.get("container-title")),
                "doi": doi,
                "url": as_text(item.get("URL")),
                "publication_type": as_text(item.get("type")),
                "raw_index": index,
            }
        )
    return total, results


def normalize_openalex(payload: dict[str, Any]) -> tuple[int | None, list[dict[str, Any]]]:
    items = payload.get("results", [])
    results = []
    for index, item in enumerate(items):
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        ids = item.get("ids") or {}
        doi = as_text(item.get("doi") or ids.get("doi"))
        if doi and doi.lower().startswith("https://doi.org/"):
            doi = doi[16:]
        results.append(
            {
                "source": "openalex",
                "source_id": as_text(item.get("id")),
                "title": as_text(item.get("display_name") or item.get("title")),
                "authors": [
                    as_text((authorship.get("author") or {}).get("display_name"))
                    for authorship in item.get("authorships", [])
                    if as_text((authorship.get("author") or {}).get("display_name"))
                ],
                "year": first_year(item.get("publication_year")),
                "venue": as_text(source.get("display_name")),
                "doi": doi,
                "url": as_text(primary.get("landing_page_url") or item.get("id")),
                "publication_type": as_text(item.get("type")),
                "raw_index": index,
            }
        )
    return (payload.get("meta") or {}).get("count"), results


def normalize_arxiv(raw: bytes) -> tuple[int | None, list[dict[str, Any]]]:
    root = ET.fromstring(raw)
    atom = "{http://www.w3.org/2005/Atom}"
    opensearch = "{http://a9.com/-/spec/opensearch/1.1/}"
    arxiv = "{http://arxiv.org/schemas/atom}"
    total_text = root.findtext(f"{opensearch}totalResults")
    total = int(total_text) if total_text and total_text.isdigit() else None
    results = []
    for index, entry in enumerate(root.findall(f"{atom}entry")):
        source_id = as_text(entry.findtext(f"{atom}id"))
        if source_id:
            source_id = source_id.rsplit("/", 1)[-1]
        published = as_text(entry.findtext(f"{atom}published"))
        results.append(
            {
                "source": "arxiv",
                "source_id": source_id,
                "title": " ".join((entry.findtext(f"{atom}title") or "").split()) or None,
                "authors": [
                    as_text(author.findtext(f"{atom}name"))
                    for author in entry.findall(f"{atom}author")
                    if as_text(author.findtext(f"{atom}name"))
                ],
                "year": first_year(published),
                "venue": "arXiv",
                "doi": as_text(entry.findtext(f"{arxiv}doi")),
                "url": as_text(entry.findtext(f"{atom}id")),
                "publication_type": "preprint",
                "raw_index": index,
            }
        )
    return total, results


def normalize_dblp(payload: dict[str, Any]) -> tuple[int | None, list[dict[str, Any]]]:
    hits = (payload.get("result") or {}).get("hits") or {}
    items = hits.get("hit", [])
    if isinstance(items, dict):
        items = [items]
    results = []
    for index, hit in enumerate(items):
        info = hit.get("info") or {}
        authors_value = (info.get("authors") or {}).get("author", [])
        if isinstance(authors_value, (str, dict)):
            authors_value = [authors_value]
        authors = []
        for author in authors_value:
            authors.append(as_text(author.get("text")) if isinstance(author, dict) else as_text(author))
        results.append(
            {
                "source": "dblp",
                "source_id": as_text(info.get("key")),
                "title": as_text(info.get("title")),
                "authors": [author for author in authors if author],
                "year": first_year(info.get("year")),
                "venue": as_text(info.get("venue")),
                "doi": as_text(info.get("doi")),
                "url": as_text(info.get("ee") or info.get("url")),
                "publication_type": as_text(info.get("type")),
                "raw_index": index,
            }
        )
    total = hits.get("@total")
    try:
        total = int(total) if total is not None else None
    except (TypeError, ValueError):
        total = None
    return total, results


def normalize_semantic_scholar(payload: dict[str, Any]) -> tuple[int | None, list[dict[str, Any]]]:
    results = []
    for index, item in enumerate(payload.get("data", [])):
        external = item.get("externalIds") or {}
        publication_types = item.get("publicationTypes") or []
        results.append(
            {
                "source": "semantic-scholar",
                "source_id": as_text(item.get("paperId")),
                "title": as_text(item.get("title")),
                "authors": [
                    as_text(author.get("name"))
                    for author in item.get("authors", [])
                    if as_text(author.get("name"))
                ],
                "year": first_year(item.get("year")),
                "venue": as_text(item.get("venue")),
                "doi": as_text(external.get("DOI")),
                "url": as_text(item.get("url")),
                "publication_type": ", ".join(publication_types) or None,
                "raw_index": index,
            }
        )
    return payload.get("total"), results


def save_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def save_results(path: Path, results: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")


def save_summary(
    output_dir: Path,
    *,
    source: str,
    requested_at: str,
    run_status: str,
    total: int | None,
    normalized_count: int,
    raw_response: str | None,
    http_status: int | None = None,
    error: str | None = None,
) -> None:
    summary = {
        "source": source,
        "requested_at_utc": requested_at,
        "run_status": run_status,
        "http_status": http_status,
        "reported_total": total,
        "normalized_count": normalized_count,
        "raw_response": raw_response,
        "error": error,
        "note": "No screening, evidence-role, or verification-state decisions were made.",
    }
    save_json(output_dir / "summary.json", summary)


def main() -> int:
    args = parse_args()
    url, response_format = build_request(args)
    if args.output_dir.exists() and (
        not args.output_dir.is_dir() or any(args.output_dir.iterdir())
    ):
        print(
            f"Output directory is not empty; use a new run directory: {args.output_dir}",
            file=sys.stderr,
        )
        return 4
    args.output_dir.mkdir(parents=True, exist_ok=True)
    requested_at = datetime.now(timezone.utc).isoformat()
    request_record: dict[str, Any] = {
        "source": args.source,
        "query": args.query,
        "raw_query": args.raw_query,
        "author": args.author,
        "doi": args.doi,
        "limit": args.limit,
        "requested_at_utc": requested_at,
        "url": url,
        "response_format": response_format,
        "http_status": None,
    }
    ssl_context, ca_bundle = build_ssl_context()
    request_record["ca_bundle"] = ca_bundle
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout, context=ssl_context) as response:
            raw = response.read()
            request_record["http_status"] = response.status
            request_record["response_content_type"] = response.headers.get("Content-Type")
    except urllib.error.HTTPError as error:
        raw = error.read()
        request_record["http_status"] = error.code
        request_record["error"] = str(error)
        save_json(args.output_dir / "request.json", request_record)
        (args.output_dir / "raw-error.txt").write_bytes(raw)
        save_results(args.output_dir / "results.jsonl", [])
        save_summary(
            args.output_dir,
            source=args.source,
            requested_at=requested_at,
            run_status="http-error",
            total=None,
            normalized_count=0,
            raw_response="raw-error.txt",
            http_status=error.code,
            error=str(error),
        )
        print(f"HTTP error {error.code}; trace saved to {args.output_dir}", file=sys.stderr)
        return 2
    except urllib.error.URLError as error:
        request_record["error"] = str(error.reason)
        save_json(args.output_dir / "request.json", request_record)
        save_results(args.output_dir / "results.jsonl", [])
        save_summary(
            args.output_dir,
            source=args.source,
            requested_at=requested_at,
            run_status="network-error",
            total=None,
            normalized_count=0,
            raw_response=None,
            error=str(error.reason),
        )
        print(f"Network error; trace saved to {args.output_dir}: {error.reason}", file=sys.stderr)
        return 2
    except TimeoutError as error:
        request_record["error"] = str(error)
        save_json(args.output_dir / "request.json", request_record)
        save_results(args.output_dir / "results.jsonl", [])
        save_summary(
            args.output_dir,
            source=args.source,
            requested_at=requested_at,
            run_status="network-error",
            total=None,
            normalized_count=0,
            raw_response=None,
            error=str(error),
        )
        print(f"Network timeout; trace saved to {args.output_dir}: {error}", file=sys.stderr)
        return 2

    raw_path = args.output_dir / f"raw.{response_format}"
    raw_path.write_bytes(raw)
    save_json(args.output_dir / "request.json", request_record)

    try:
        if response_format == "json":
            payload = json.loads(raw.decode("utf-8"))
            if args.source == "crossref":
                total, results = normalize_crossref(payload, bool(args.doi))
            elif args.source == "openalex":
                total, results = normalize_openalex(payload)
            elif args.source == "dblp":
                total, results = normalize_dblp(payload)
            else:
                total, results = normalize_semantic_scholar(payload)
        else:
            total, results = normalize_arxiv(raw)
    except (json.JSONDecodeError, ET.ParseError, UnicodeDecodeError, TypeError, ValueError) as error:
        request_record["normalization_error"] = str(error)
        save_json(args.output_dir / "request.json", request_record)
        save_results(args.output_dir / "results.jsonl", [])
        save_summary(
            args.output_dir,
            source=args.source,
            requested_at=requested_at,
            run_status="parse-error",
            total=None,
            normalized_count=0,
            raw_response=raw_path.name,
            http_status=request_record["http_status"],
            error=str(error),
        )
        print(f"Normalization error; raw response kept at {raw_path}: {error}", file=sys.stderr)
        return 3

    save_results(args.output_dir / "results.jsonl", results)
    save_summary(
        args.output_dir,
        source=args.source,
        requested_at=requested_at,
        run_status="success" if results else "zero-hit",
        total=total,
        normalized_count=len(results),
        raw_response=raw_path.name,
        http_status=request_record["http_status"],
    )
    summary = json.loads((args.output_dir / "summary.json").read_text(encoding="utf-8"))
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
