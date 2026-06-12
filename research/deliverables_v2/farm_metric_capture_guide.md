# Farm-level metric capture guide

This guide is the human-readable companion to [`metric_calculation_rules.csv`](metric_calculation_rules.csv). Field names shown in backticks are defined in [`farm_data_dictionary.csv`](farm_data_dictionary.csv).

## Safeguards

### M01 — Traceable sourcing coverage

Capture one `sourcing_lot` row per transfer: `volume_tonnes`, `traceability_type`, `origin_fields`, buyer/destination, harvest/transfer dates, and supporting document. Link each origin field to a validated property/field geometry. The denominator is **all submitted farm volume**, including unknown-origin volume; unknowns never count as traceable.

### M02 — No post-cutoff natural-ecosystem conversion

Capture the applicable cutoff in `reporting_period.applicable_cutoff_date`; validated property/habitat geometries; and an annual/event `land_cover_observation` for each relevant polygon. Every potential change needs `area_ha`, `change_type`, start/end dates, `natural_ecosystem_conversion_flag`, confidence, field-verification status, and approved investigation disposition. Report confirmed post-cutoff conversion hectares, while pending/uncertain alerts make status unresolved.

### M03 — Legal/protected/riparian/wetland compliance

Capture legal designations on every `habitat_polygon`, permits/status for `water_source`, current official/legal evidence, and any `incident` or `assurance_finding`. Do not duplicate hectares where APP, Legal Reserve, wetland, or other designations overlap.

### M04 — Rights, tenure, grievance, and FPIC

Capture farm tenure/use-right status and evidence plus restricted `rights_grievance` cases with type, date/channel, affected-group code, required consent/FPIC and status, severity, case status, and remedy. Missing/disputed rights or open high-risk cases are unresolved until qualified review.

### M05 — Threatened-species protection

Capture the risk/list version and any `species_observation`: scientific name, identification confidence, threat source/status, observation type/count, and protection action/status. Capture hunting, collection, mortality, or habitat harm as incidents. No recorded observation must never be interpreted as species absence.

### M06 — Prohibited pesticides and contamination/buffer breaches

Capture every application event, including registration, active ingredients, concentration, amount/unit, treated area, date/time, buffer, weather, and prohibited-product flag. Link spills, drift, contamination, and buffer breaches to `incident`. Reconcile applications to purchase/inventory/disposal evidence during assurance.

## Core farm improvement metrics

### M07 — Native/semi-natural habitat extent and annual loss

Capture unique non-overlapping habitat polygons with ecosystem/management class and area plus annual land-cover observations. Calculate current extent from unique polygon area and report gross loss and gross gain separately by ecosystem class. Never subtract gain/restoration from prohibited loss.

### M08 — Habitat-management implementation and condition

Capture the habitat polygon’s management-plan link and due/completed actions in the approved plan system. For condition, capture stable plot/site, method/version, date, raw `indicator_name`, `indicator_value`, unit, sampling effort, reference value, derived score, and disturbance flags. Only compare compatible methods, seasons, and sites.

### M09 — Riparian/wetland protection and restoration

Use habitat polygon designation/class and annual land-cover/incident records for protected extent and gross disturbance. Where restoration occurs, capture intervention area and method, establishment year, monitoring effort, survival counts, native cover/richness, condition observations, and reversals.

### M10 — Pesticide toxic-load trajectory and IPM

The toxic-load calculation needs event-level product amount, active-ingredient concentration, treated area, managed crop area, and an approved versioned toxicity factor. IPM evidence requires raw scouting result, sampling effort/method, action threshold, natural-enemy result where applicable, decision, and non-chemical action. Report active ingredient and modeled toxic load per hectare; do not claim a biodiversity outcome.

### M11 — Soil cover, crop diversity, and erosion risk

For each field, capture crop-cycle dates/crop/area/preceding crop and repeated key-window observations of living cover %, residue cover %, bare soil %, method, effort, and erosion signs. Retain field erosion-risk class and event-level erosion incidents. Shared/intercropped area must be flagged so physical hectares are not counted twice.

### M12 — Water risk, withdrawal, and quality incidents

All farms capture source/use/permit/basin-risk status. Farms withdrawing water capture period, source, volume, method, meter readings where used, irrigated fields, permit limit, and exceedance. Risk-triggered monitoring captures raw sample parameter/result/unit/method/QA/threshold and site position. Report estimates as estimated and do not infer basin causality.

## Conditional and leadership metrics

### M13 — Restoration survival and condition

Calculate survival only from comparable cohorts as `100 × surviving_individuals_count / sampled_individuals_count`. Report treated/intervention area, survival, native cover/richness, condition change, and reversal area separately. An intervention hectare is not automatically a restored hectare.

### M14 — Landscape connectivity

The farm supplies validated, dated habitat geometry/class/condition inputs. Connectivity itself is calculated at the approved landscape boundary using a transparent versioned method. Report farm-controlled corridor/habitat area separately from external landscape change.

### M15 — Freshwater condition

Capture raw valid water-quality samples with site position, time, flow/season context where required, parameter/result/unit, method/lab, detection limit, QA flag, reference, and exceedance. Trend or upstream/downstream interpretation requires an approved repeated/comparator design.

### M16 — Pollinator or bird response

Capture repeat survey events with fixed site geometry, target, method, date/time, effort/unit, conditions, raw taxon detections **and valid zero detections**, and identification validation. Occupancy/diversity estimates require a pre-approved detection-aware model and sufficient repeated sampling.

### M17 — Soil-biota response

Use a pilot-approved sample design and capture sample location, timing, method, effort, laboratory/field result, QA, and field/soil/crop context. Compare only method-, season-, soil-, and field-compatible samples; retain raw results rather than a universal score.

### M18 — Invasive-species extent and control efficacy

Capture species, polygon, date, method, occupied area/density, whether the row is baseline/treatment/follow-up, treatment method, efficacy under an approved comparison, and non-target harm. Treatment alone is not efficacy; no follow-up means no control-outcome claim.
