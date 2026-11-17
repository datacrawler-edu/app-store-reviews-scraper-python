"""Export an existing Dataset without starting an Actor run."""

import argparse
import csv
from pathlib import Path

from request import iter_reviews

FIELDS = (
    "appId", "country", "reviewId", "rating", "reviewedAt", "title", "text",
    "hasDeveloperResponse", "developerResponse",
)


def spreadsheet_cell(value):
    if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    with args.csv_path.open("x", encoding="utf-8-sig", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        for row in iter_reviews(args.dataset_id):
            writer.writerow({field: spreadsheet_cell(row.get(field)) for field in FIELDS})
