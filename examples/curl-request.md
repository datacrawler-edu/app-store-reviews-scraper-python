# App Store reviews with cURL

Set the `APIFY_API_TOKEN` environment variable. Run from the repository root. The first request starts a run and returns its ID. If a response is lost, check your Apify Runs before issuing another start.

```bash
curl --fail-with-body --silent --show-error --max-time 25 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample-input.json \
  "${APIFY_API_BASE_URL:-https://api.apify.com/v2}/acts/datascraperes~app-store-reviews-deep-scraper/runs?maxTotalChargeUsd=0.03&timeout=180"
```

Set `RUN_ID`, then repeat this read until it reports a terminal status. Use the Dataset and Key-Value Store IDs returned by the run.

```bash
curl --fail-with-body --silent --show-error --max-time 25 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "${APIFY_API_BASE_URL:-https://api.apify.com/v2}/actor-runs/$RUN_ID?waitForFinish=15"
```

Use `KVS_ID` for coverage and `DATASET_ID` to read the first 250 rows. Use the Python [CSV exporter](python/export_reviews.py) for automatic pagination.

```bash
curl --fail-with-body --silent --show-error --max-time 25 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "${APIFY_API_BASE_URL:-https://api.apify.com/v2}/key-value-stores/$KVS_ID/records/SUMMARY"

curl --fail-with-body --silent --show-error --max-time 25 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "${APIFY_API_BASE_URL:-https://api.apify.com/v2}/datasets/$DATASET_ID/items?format=json&offset=0&limit=250"
```
