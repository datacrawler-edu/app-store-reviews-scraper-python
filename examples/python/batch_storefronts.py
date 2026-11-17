"""Compare coverage for two storefronts in a single bounded Actor run."""

import json

from request import collect


if __name__ == "__main__":
    _, summary = collect({
        "apps": ["310633997"],
        "countries": ["us", "gb"],
        "maxReviewsPerApp": 10,
        "maxItems": 20,
        "sort": "mostRecent",
    })
    coverage = {
        "status": summary["status"],
        "complete": summary["complete"],
        "coverage": summary["coverage"],
    }
    print(json.dumps(coverage, ensure_ascii=False, indent=2))
