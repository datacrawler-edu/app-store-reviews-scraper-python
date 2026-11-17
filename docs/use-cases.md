# Review workflows

- **Storefront comparison.** Run the [two-country example](../examples/python/batch_storefronts.py) with the same app and sort. Review the per-country coverage before comparing rating distributions.
- **Product feedback.** Adjust `publishedAfter` and `maxRating` to sample recent complaints. Keep `reviewId` and `country` when joining later runs.
- **Developer replies.** Enable `onlyWithDeveloperResponse` to focus on answered reviews. Use both timestamps to measure response lag only when both are available.
