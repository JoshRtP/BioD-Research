#!/usr/bin/env python3
"""Validate the internal consistency of the v2 farm-data research package."""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_RESEARCH = ROOT.parent

with (ROOT / "farm_data_dictionary.csv").open(newline="", encoding="utf-8") as stream:
    fields = list(csv.DictReader(stream))

field_ids = [row["field_id"] for row in fields]
assert len(field_ids) == len(set(field_ids)), "Duplicate field_id values"
assert all(row["field_id"] == f'{row["table_name"]}.{row["field_name"]}' for row in fields)

tables = sorted({row["table_name"] for row in fields})
valid_metric_ids = {f"M{i:02d}" for i in range(1, 19)}
linked_metric_ids = {
    metric_id
    for row in fields
    for metric_id in row["linked_metrics"].split("|")
    if metric_id
}
assert linked_metric_ids <= valid_metric_ids, f"Unknown linked metric IDs: {linked_metric_ids - valid_metric_ids}"
assert linked_metric_ids == valid_metric_ids, f"Metrics without linked dictionary fields: {valid_metric_ids - linked_metric_ids}"
for table in tables:
    expected = [row["field_name"] for row in fields if row["table_name"] == table]
    with (ROOT / "templates" / f"{table}.csv").open(newline="", encoding="utf-8") as stream:
        actual = next(csv.reader(stream))
    assert actual == expected, f"Template header differs from dictionary: {table}"

with (ROOT / "metric_calculation_rules.csv").open(newline="", encoding="utf-8") as stream:
    metrics = list(csv.DictReader(stream))
assert [row["metric_id"] for row in metrics] == [f"M{i:02d}" for i in range(1, 19)]
for metric in metrics:
    for table in metric["required_tables"].split("|"):
        assert table in tables, f'{metric["metric_id"]} references missing table {table}'

broken_links = []
for markdown in REPO_RESEARCH.glob("**/*.md"):
    for link in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)", markdown.read_text(encoding="utf-8")):
        if "://" not in link and not link.startswith("mailto:") and not (markdown.parent / link).exists():
            broken_links.append((markdown, link))
assert not broken_links, f"Broken local Markdown links: {broken_links}"

print(f"PASS: {len(fields)} fields, {len(tables)} tables/templates, {len(metrics)} metric rules, local links valid")
