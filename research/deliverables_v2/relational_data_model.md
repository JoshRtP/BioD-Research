# Relational farm data model

## Core relationship map

```text
program_farm 1 ── * property_boundary
program_farm 1 ── * reporting_period
program_farm 1 ── * field
program_farm 1 ── * habitat_polygon
program_farm 1 ── * water_source
program_farm 1 ── * evidence_register

reporting_period 1 ── * sourcing_lot
reporting_period 1 ── * crop_cycle
crop_cycle 1 ── * pesticide_application
crop_cycle 1 ── * ipm_scouting
crop_cycle 1 ── * soil_cover_observation

habitat_polygon 1 ── * land_cover_observation
habitat_polygon 1 ── * habitat_condition_observation
habitat_polygon 1 ── * restoration_observation
habitat_polygon 1 ── * invasive_species_observation

water_source 1 ── * water_withdrawal
water_source 1 ── * water_quality_sample
program_farm 1 ── * incident
program_farm 1 ── * rights_grievance
program_farm 1 ── * species_observation
program_farm 1 ── * biological_survey_event
program_farm 1 ── * assurance_finding
```

## Primary and foreign-key rules

- Every table has one program-issued `*_id` primary key. IDs are immutable and unique across all reporting periods.
- Every farm-level table includes `farm_id`; transactional/observation tables also include `reporting_period_id` or an observation date from which it is derived.
- `field_id`, `habitat_polygon_id`, and `water_source_id` are foreign keys and must exist before related observations are accepted.
- Evidence is referenced with `evidence_ids`, a pipe-delimited list in CSV exchange. Production systems should implement a junction table instead.
- Geometry is submitted as a separate GeoPackage/GeoJSON object referenced by `geometry_id`; CSV templates capture geometry metadata, not coordinate strings.

## Grains and double-counting controls

| Table | One row represents | Prohibited aggregation error |
|---|---|---|
| `farm` | One program farm/property unit | Do not duplicate a property because it supplies multiple buyers |
| `reporting_period` | One farm in one program reporting period | Do not mix crop seasons without explicit period dates |
| `field` | One stable management polygon | Do not treat crop cycles as separate physical area |
| `crop_cycle` | One crop planted on one field for one cycle | Intercrop components require shared-area flag; do not sum area twice |
| `habitat_polygon` | One stable native/semi-natural/restoration polygon | Overlapping legal designations do not create extra habitat hectares |
| Observation tables | One observation/event/sample at a date/location/method | Do not average methods or seasons without retaining source rows |
| `sourcing_lot` | One transfer/lot from farm to buyer | Do not use sold volume as production area |

## Time and version rules

- Store dates in ISO 8601 (`YYYY-MM-DD`) and timestamps in UTC with offset.
- A changed boundary creates a new `boundary_version`; historical calculations retain the original version.
- Corrected records retain `supersedes_record_id`, correction reason, editor, and timestamp in the production system.
- A controlled-vocabulary or formula change requires a schema/method version and recalculation log.

## Geospatial rules

- Minimum geometry types: property boundary, field polygon, habitat polygon, water-source point/line/polygon, sampling point, and incident point/polygon.
- Record CRS/EPSG, source, capture date, positional accuracy, and validation status for every geometry.
- Run topology checks for invalid geometry, self-intersection, duplicate geometry, property overlap, field overlap, and polygons outside the validated property boundary.
- Store sensitive species/rightsholder locations in a restricted layer; expose only generalized locations for routine reporting.
