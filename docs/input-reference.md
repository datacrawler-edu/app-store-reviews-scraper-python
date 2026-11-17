# Actor input reference

| Field | Value and behavior |
| --- | --- |
| `apps` | Required. Up to 100 numeric IDs, bundle IDs or full public App Store URLs. |
| `countries` | Two-letter App Store storefront codes. If omitted, uses URL storefronts, then `us` as the fallback. |
| `maxReviewsPerApp` | Cap per app and country. Defaults to 200. |
| `maxItems` | Combined cap across the run. Defaults to 2,000. |
| `sort` | `mostRecent` (default), `mostHelpful`, `mostFavorable`, `mostCritical`. |
| `minRating`, `maxRating` | Set a star bound from 1 to 5. Use 0 to disable a bound. |
| `publishedAfter` | Earliest review date, formatted as `YYYY-MM-DD`. An empty string disables the filter. |
| `onlyWithDeveloperResponse` | Set to `true` to deliver reviews with a public developer reply. Defaults to `false`. |

Every selected app is paired with every selected storefront. The [sample input](../data/sample-input.json) selects one pair.
