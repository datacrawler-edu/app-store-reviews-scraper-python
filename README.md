# Apple App Store reviews scraper with Python and CSV export

Collect written iOS App Store reviews through the hosted Apify Actor. Compare storefronts, keep developer replies with the original review, and export a saved Dataset for analysis.

[Open the App Store Reviews Scraper on Apify](https://apify.com/datascraperes/app-store-reviews-deep-scraper?fpr=edudata)

## What this repository helps you do

- Pull a small review sample for a single app with Python, JavaScript or cURL.
- Compare collection coverage across storefronts with one run.
- Export an existing Dataset with a paginated Python script.

## Example result

A review row includes its storefront, rating, text, date and reply fields. See the illustrative [JSON sample](data/sample-output.json) or the [CSV sample](data/sample-output.csv).

## Run without code

Open the [hosted Actor](https://apify.com/datascraperes/app-store-reviews-deep-scraper?fpr=edudata), enter an app ID and select a storefront. Set a small review limit for your first run. Open the Dataset to download CSV or JSON, and check the run summary for coverage. [Step-by-step guide](docs/no-code-guide.md)

## Try it with Apify's free plan

Apify's Free plan includes $5 per month in prepaid usage and requires no credit card. See the [current Apify plans](https://apify.com/pricing?fpr=edudata) and the Actor's Pricing tab before choosing a budget.

## Quick start for developers

Use Python 3.10 or newer. Set `APIFY_API_TOKEN` to your Apify API token in your environment. The examples use the Python standard library.

```bash
python examples/python/request.py
```

The script prints the saved reviews as JSON and reports the run ID and any incomplete coverage on stderr. It starts one potentially billable run with a spending cap of USD 0.03.

## Input example

```json
{
  "apps": ["310633997"],
  "countries": ["us"],
  "maxReviewsPerApp": 10,
  "maxItems": 10,
  "sort": "mostRecent"
}
```

The [input reference](docs/input-reference.md) lists available filters and sorting modes.

## Request examples

| Goal | Example |
| --- | --- |
| Run once and print review rows | [Python](examples/python/request.py) |
| Compare coverage in the US and UK | [Python storefront workflow](examples/python/batch_storefronts.py) |
| Export an existing Dataset to CSV | [Python export](examples/python/export_reviews.py) |
| Submit, check and read by ID | [cURL](examples/curl-request.md) |
| Run once and read pages with Node.js 22+ | [JavaScript](examples/javascript/request.mjs) |

## Output fields

Use `appId`, `country` and `reviewId` together when merging exports. Use `developerResponse` and `developerResponseAt` for reply analysis. The Key-Value Store record `SUMMARY` contains coverage by app and country. [Output reference](docs/output-reference.md)

## Common use cases

[Use cases and input choices](docs/use-cases.md) explains storefront comparison, feedback analysis and developer reply monitoring.

## Export Apple App Store reviews to CSV with Python

```bash
python examples/python/export_reviews.py DATASET_ID app-store-reviews.csv
```

Get the Dataset ID from a saved run. The exporter reads pages from that Dataset without starting an Actor run. Spreadsheet-sensitive values are prefixed with an apostrophe in the exported CSV. Use the JSON Dataset for the original values.

## Compare iOS reviews across storefronts

Run `python examples/python/batch_storefronts.py` to inspect coverage for the same app in the US and UK. Check each pair's `stopReason` before drawing conclusions from a small sample.

## FAQ

See the [FAQ](docs/faq.md) for successful runs with incomplete coverage, input identifiers and ambiguous starts.

## Limits and pricing

Each delivered unique review counts as one `review-scraped` event. Apify can also charge a startup event. The app–storefront cap and total cap are independent. Review history depends on what Apple makes available for the selected storefront. Check the [Actor's Pricing tab](https://apify.com/datascraperes/app-store-reviews-deep-scraper?fpr=edudata) for your tier and current rates.

## Hosted version

Use the [Apify Actor](https://apify.com/datascraperes/app-store-reviews-deep-scraper?fpr=edudata) for collection, run logs, scheduling and Dataset storage.

## Responsible use

Use review data in accordance with applicable terms and privacy obligations. Keep API tokens out of source control and redact personal data before sharing exports.

## Support

For example issues, [open a GitHub issue](https://github.com/datacrawler-edu/app-store-reviews-scraper-python/issues) with a sanitized input and the error. For collection issues, open the [hosted Actor](https://apify.com/datascraperes/app-store-reviews-deep-scraper?fpr=edudata) and include your run ID.

## License

The examples and guides use the [MIT License](LICENSE).
