"""Start the hosted Actor once, check coverage and print the stored reviews."""

import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ACTOR = "datascraperes~app-store-reviews-deep-scraper"
SAMPLE = Path(__file__).resolve().parents[2] / "data" / "sample-input.json"
TERMINAL_FAILURES = {"FAILED", "ABORTED", "TIMED-OUT"}


def request(path, *, params=None, body=None):
    base = os.environ.get("APIFY_API_BASE_URL", "https://api.apify.com/v2").rstrip("/")
    url = base + path + ("?" + urlencode(params) if params else "")
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Authorization": "Bearer " + os.environ["APIFY_API_TOKEN"]}
    if data is not None:
        headers["Content-Type"] = "application/json"
    with urlopen(Request(url, data=data, headers=headers), timeout=25) as reply:
        return json.load(reply)


def collect(input_data, budget=0.03):
    if not os.environ.get("APIFY_API_TOKEN"):
        raise SystemExit("Set APIFY_API_TOKEN first.")
    try:
        run = request(
            "/acts/" + ACTOR + "/runs",
            params={"maxTotalChargeUsd": budget, "timeout": 180},
            body=input_data,
        )["data"]
        run_id = run["id"]
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError) as exc:
        raise SystemExit("Could not confirm the start. Check Apify Runs before trying again.") from exc
    print("Apify run ID: " + run_id, file=sys.stderr)
    for remaining in range(13, -1, -1):
        if run["status"] == "SUCCEEDED":
            summary = request("/key-value-stores/" + run["defaultKeyValueStoreId"] + "/records/SUMMARY")
            if summary.get("complete") is not True:
                print("Collection is incomplete. Inspect SUMMARY for coverage and stop reasons.", file=sys.stderr)
            return run, summary
        if run["status"] in TERMINAL_FAILURES:
            raise SystemExit(f"Run {run_id} ended as {run['status']}. Inspect its log and storage.")
        if not remaining:
            break
        run = request("/actor-runs/" + run_id, params={"waitForFinish": 15})["data"]
    raise SystemExit("Wait limit reached. Check the saved run ID before starting another run.")


def iter_reviews(dataset_id):
    offset = 0
    while True:
        page = request("/datasets/" + dataset_id + "/items", params={"format": "json", "offset": offset, "limit": 250})
        if not isinstance(page, list):
            raise ValueError("Expected a list of Dataset items.")
        if not page:
            return
        yield from page
        offset += len(page)


if __name__ == "__main__":
    run, _ = collect(json.loads(SAMPLE.read_text(encoding="utf-8")))
    print(json.dumps(list(iter_reviews(run["defaultDatasetId"])), ensure_ascii=False, indent=2))
