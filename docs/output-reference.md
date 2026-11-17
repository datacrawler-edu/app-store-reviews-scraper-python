# Read the Dataset and run coverage

The default Dataset contains one row per delivered review. The [JSON sample](../data/sample-output.json) shows all fields. `reviewedAt` is the review date, `scrapedAt` is the collection timestamp, and `developerResponseAt` can be null. `position` is the position in Apple's paged result and may have gaps after filtering.

Read `SUMMARY` from the run's default Key-Value Store. It records `status`, `complete`, counts and per-pair `coverage`, including stop reasons and rating histograms when available. A platform status of `SUCCEEDED` can accompany partial coverage or invalid input. Use the summary when deciding whether to consume or compare datasets.

For larger saved Datasets, use the [Python exporter](../examples/python/export_reviews.py). It reads successive offsets until an empty page.
