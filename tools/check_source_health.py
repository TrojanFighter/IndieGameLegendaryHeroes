#!/usr/bin/env python3
"""Check HTTP(S) source health for Evidence Ledgers.

This is deliberately a maintenance report, not a research truth checker. It does
not mutate evidence files and it exits zero for dead/restricted URLs so external
website failures do not become merge gates.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import socket
import ssl
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://[^\s<>\"'`]+")
TRAILING = ".,;:!?)]}>，。；：！？）】》"
USER_AGENT = (
    "IndieGameLegendaryHeroes-source-health/0.1 "
    "(+https://github.com/TrojanFighter/IndieGameLegendaryHeroes)"
)


@dataclass
class Reference:
    file: str
    line: int


@dataclass
class Result:
    url: str
    status: str
    http_status: int | None
    final_url: str | None
    detail: str
    references: list[Reference]


def clean_url(raw: str) -> str:
    return raw.rstrip(TRAILING)


def discover_urls(root: Path) -> dict[str, list[Reference]]:
    refs: dict[str, list[Reference]] = defaultdict(list)
    for path in sorted(root.rglob("*.md")):
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in URL_RE.finditer(line):
                url = clean_url(match.group(0))
                if url:
                    refs[url].append(Reference(rel, line_no))
    return dict(refs)


def classify_http(code: int, original: str, final: str | None) -> str:
    if 200 <= code < 300:
        if final and final.rstrip("/") != original.rstrip("/"):
            return "REDIRECTED"
        return "HEALTHY"
    if code in {401, 402, 403}:
        return "ACCESS_RESTRICTED"
    if code in {404, 410}:
        return "DEAD"
    if code in {408, 425, 429} or 500 <= code < 600:
        return "TEMPORARILY_UNREACHABLE"
    if 400 <= code < 500:
        return "CLIENT_ERROR"
    return "UNKNOWN_ERROR"


def check_one(url: str, references: list[Reference], timeout: float) -> Result:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
            "Range": "bytes=0-2047",
        },
        method="GET",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            code = int(response.getcode() or 0)
            final = response.geturl()
            try:
                response.read(512)
            except Exception:
                # A body-read failure does not erase the HTTP response we received.
                pass
            return Result(
                url=url,
                status=classify_http(code, url, final),
                http_status=code,
                final_url=final,
                detail="",
                references=references,
            )
    except HTTPError as exc:
        code = int(exc.code)
        final = exc.geturl() if hasattr(exc, "geturl") else None
        return Result(
            url=url,
            status=classify_http(code, url, final),
            http_status=code,
            final_url=final,
            detail=str(exc.reason or "HTTP error"),
            references=references,
        )
    except (TimeoutError, socket.timeout) as exc:
        return Result(
            url=url,
            status="TEMPORARILY_UNREACHABLE",
            http_status=None,
            final_url=None,
            detail=f"timeout: {exc}",
            references=references,
        )
    except URLError as exc:
        reason = exc.reason
        if isinstance(reason, (TimeoutError, socket.timeout)):
            status = "TEMPORARILY_UNREACHABLE"
        elif isinstance(reason, ssl.SSLError):
            status = "TEMPORARILY_UNREACHABLE"
        else:
            status = "TEMPORARILY_UNREACHABLE"
        return Result(
            url=url,
            status=status,
            http_status=None,
            final_url=None,
            detail=f"network: {reason}",
            references=references,
        )
    except Exception as exc:  # pragma: no cover - defensive boundary
        return Result(
            url=url,
            status="UNKNOWN_ERROR",
            http_status=None,
            final_url=None,
            detail=f"{type(exc).__name__}: {exc}",
            references=references,
        )


def run_checks(
    refs: dict[str, list[Reference]], timeout: float, workers: int
) -> list[Result]:
    results: list[Result] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(check_one, url, references, timeout): url
            for url, references in refs.items()
        }
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return sorted(results, key=lambda r: (r.status, r.url))


def markdown_report(results: Iterable[Result], total_refs: int) -> str:
    rows = list(results)
    counts = Counter(r.status for r in rows)
    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        "# Evidence Source Health",
        "",
        f"Generated: `{generated}`",
        "",
        f"Unique URLs: **{len(rows)}** · URL references: **{total_refs}**",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status in [
        "HEALTHY",
        "REDIRECTED",
        "ACCESS_RESTRICTED",
        "TEMPORARILY_UNREACHABLE",
        "DEAD",
        "CLIENT_ERROR",
        "UNKNOWN_ERROR",
    ]:
        lines.append(f"| {status} | {counts.get(status, 0)} |")

    needs_review = [r for r in rows if r.status != "HEALTHY"]
    lines.extend(["", "## Needs review", ""])
    if not needs_review:
        lines.append("No non-healthy URLs in this run.")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "| Status | HTTP | URL | Referenced from | Detail |",
            "|---|---:|---|---|---|",
        ]
    )
    for result in needs_review:
        refs = ", ".join(f"{r.file}:{r.line}" for r in result.references[:5])
        if len(result.references) > 5:
            refs += f" (+{len(result.references) - 5})"
        final_note = ""
        if result.final_url and result.final_url != result.url:
            final_note = f" → {result.final_url}"
        detail = (result.detail + final_note).replace("|", "\\|").replace("\n", " ")
        url = result.url.replace("|", "%7C")
        lines.append(
            f"| {result.status} | {result.http_status or ''} | {url} | {refs} | {detail} |"
        )
    lines.extend(
        [
            "",
            "> This report checks reachability only. A live URL does not prove that the page still contains the same evidence, and a restricted URL is not automatically a paywall.",
        ]
    )
    return "\n".join(lines) + "\n"


def json_report(results: Iterable[Result], total_refs: int) -> dict[str, object]:
    rows = list(results)
    counts = Counter(r.status for r in rows)
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "unique_urls": len(rows),
        "url_references": total_refs,
        "counts": dict(sorted(counts.items())),
        "results": [
            {
                **{k: v for k, v in asdict(result).items() if k != "references"},
                "references": [asdict(ref) for ref in result.references],
            }
            for result in rows
        ],
    }


def write_text(path: str | None, content: str) -> None:
    if not path:
        return
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-dir", default="evidence")
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--json-out")
    parser.add_argument("--markdown-out")
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Only validate URL extraction; do not make network requests.",
    )
    args = parser.parse_args()

    evidence_root = ROOT / args.evidence_dir
    if not evidence_root.exists():
        print(f"missing evidence directory: {evidence_root}", file=sys.stderr)
        return 2

    refs = discover_urls(evidence_root)
    total_refs = sum(len(items) for items in refs.values())
    print(f"discovered {len(refs)} unique URLs across {total_refs} references")

    if args.list_only:
        if not refs:
            print("warning: no HTTP(S) URLs discovered", file=sys.stderr)
        return 0

    results = run_checks(refs, timeout=args.timeout, workers=max(1, args.workers))
    md = markdown_report(results, total_refs)
    data = json_report(results, total_refs)

    write_text(args.markdown_out, md)
    if args.json_out:
        target = Path(args.json_out)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
