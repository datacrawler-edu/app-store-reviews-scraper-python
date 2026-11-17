# Frequently asked questions

**Do I need an Apple account?** Collection reads public written reviews. Calling the Apify API requires an Apify token.

**Why did a successful run return fewer rows than my cap?** The cap is an upper bound. Filters, availability and source conditions can reduce the collection. Check `SUMMARY.complete` and each pair's `stopReason`.

**What if the start response is lost?** Check your Apify Runs before trying the start again. If you already have a run ID, read that run and its storage.

**Can I export without another run?** Yes. Use an existing Dataset ID with the [CSV exporter](../examples/python/export_reviews.py).
