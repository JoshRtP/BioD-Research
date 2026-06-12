# Biodiversity research execution package — version 2 farm data design

**Release:** 2.0 farm-data specification — 12 June 2026
**Builds on:** [`../deliverables/`](../deliverables/)

Version 1 defined what the program should measure. Version 2 defines the **specific farm-level data that must be captured** to calculate, verify, and interpret those metrics. It does not replace the legal, stakeholder, or pilot gates in version 1.

The v2 schema contains **413 defined fields across 25 relational capture tables**, 25 matching empty CSV templates, and explicit farm-level calculation/interpretation rules for **M01–M18**.

## What is included

| Deliverable | Purpose |
|---|---|
| [`farm_data_dictionary.csv`](farm_data_dictionary.csv) | Machine-readable definition of every proposed farm-level field, including type, unit/domain, required-when rule, method, frequency, evidence, validation, sensitivity, and linked metrics |
| [`metric_calculation_rules.csv`](metric_calculation_rules.csv) | Exact provisional formulas, grains, inputs, applicability, missing-data, QA, and output rules for M01–M18 |
| [`farm_data_collection_protocol.md`](farm_data_collection_protocol.md) | Operational instructions for onboarding, annual/seasonal/event capture, geospatial data, sampling, evidence, and data-quality controls |
| [`relational_data_model.md`](relational_data_model.md) | Table relationships, keys, aggregation levels, and rules that prevent double counting |
| [`minimum_farm_submission.md`](minimum_farm_submission.md) | Plain-language checklist of what each farm submits and when |
| [`farm_metric_capture_guide.md`](farm_metric_capture_guide.md) | Human-readable metric-by-metric explanation of the exact records and fields needed |
| [`worked_metric_examples.md`](worked_metric_examples.md) | Fictional worked examples showing how representative farm records become metric outputs |
| [`validate_v2.py`](validate_v2.py) | Reusable internal consistency check for the dictionary, templates, metric references, and links |
| [`templates/`](templates/) | Empty CSV capture templates whose headers are generated directly from the data dictionary |

## Design principles

1. **Capture observations before scores.** Preserve raw quantities, dates, locations, methods, evidence, and uncertainty.
2. **Separate spatial grains.** Property, field, habitat polygon, sampling plot, water source, and event records must not be mixed.
3. **Use stable identifiers.** Records link through program-issued IDs; farm names and personal data are not analytical keys.
4. **Distinguish required, conditional, and pilot data.** A farm only supplies conditional tables when an applicability trigger is met.
5. **Treat unknown safeguards as unresolved.** Missing evidence does not equal zero impact or compliance.
6. **Do not infer outcomes from practices.** Practice, pressure, condition, and biological-response records remain separate.
7. **Protect sensitive data.** Rights-holder, grievance, threatened-species, and precise-location data require restricted access.

## Implementation sequence

1. Approve field names, controlled vocabularies, and applicability triggers with Brazilian technical, legal, rights, producer, and assurance reviewers.
2. Load the empty templates into the selected data platform without changing stable field IDs.
3. Pilot form usability and evidence burden with representative farms.
4. Validate formulas and thresholds against real observations before production claims.
5. Version schema changes; never silently redefine a field or historical result.
