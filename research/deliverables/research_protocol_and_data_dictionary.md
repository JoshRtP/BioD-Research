# Research protocol and data dictionary

## Protocol

1. **Source inclusion:** prioritize current law and official government data, normative certification documents, official framework methods, and peer-reviewed protocols. Record version/status/access date.
2. **Finding labels:** `document-confirmed`, `expert-interpretation`, `empirical-evidence`, or `research-hypothesis`.
3. **Crosswalk unit:** one auditable requirement or guidance concept per row. Split compound clauses where they map to different metrics.
4. **Equivalence:** E1 same requirement/threshold; E2 same concept/different threshold; E3 partial overlap; E4 complementary; E5 conflict; E0 no equivalent identified.
5. **Safeguard gate:** legality, rights, traceability, conversion, critical habitat, threatened species, and prohibited inputs bypass weighted scoring.
6. **Metric scoring:** 0–5 for the ten criteria in the plan. Weighted total is a prioritization aid, not proof of ecological validity.
7. **QC:** verify clause/page; validate CSV schema; dual-code at least 20% before final release; require Brazilian legal review; preserve disagreements.
8. **Versioning:** update the source register annually and before claims-policy changes. Store superseded recommendations rather than silently overwriting them.

## Core data dictionary

| Field | Definition / rule |
|---|---|
| `record_id` | Stable unique identifier; never recycle |
| `source_name`, `source_version`, `source_status` | Exact instrument identity and whether current/needs verification |
| `clause_or_page` | Exact clause and PDF page where available |
| `taxonomy_id` | B1–B14 taxonomy from the research plan |
| `metric_layer` | A safeguard; B pressure/practice; C state/condition; D biological response |
| `normative_strength` | shall/must, should, guidance, context |
| `equivalence_code` | E0–E5 per coding rule above |
| `candidate_program_treatment` | required safeguard, core universal, core conditional, leadership, research/pilot, exclude |
| `baseline_rule` | Fixed historical cutoff for safeguards or first verified measurement for improvement |
| `threshold_or_trajectory` | Pass/fail requirement or defined direction/target |
| `assurance_method` | Evidence and independent verification approach |
| `evidence_confidence` | High: direct normative/protocol support; medium: plausible but validation needed; low: hypothesis/pilot |
| `legal_relationship` | Legal minimum, voluntary addition, or requires legal review |
| `review_status` | desk reviewed, dual-coded, legal reviewed, stakeholder validated, pilot validated |

## Missing and uncertain data rules

- Unknown traceability or conversion status is **not compliant**, not zero impact.
- Do not impute a passed safeguard from regional averages.
- For improvement metrics, report coverage and missingness; do not award improvement points for missing data.
- Flag cloud, classification, seasonality, and boundary uncertainty; field-check material/high-risk discrepancies.
- Preserve numerator, denominator, area, sourcing volume, and confidence separately from any aggregate index.
