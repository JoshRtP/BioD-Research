# Farm data collection protocol

## 1. Collection calendar

| Timing | Required capture |
|---|---|
| Onboarding and boundary change | Farm identity; validated property boundary; fields; habitat, protected, riparian, wetland, restoration and water-source features; rights/tenure screen; historical conversion screen |
| Start of each reporting period | Reporting dates; operator/assurance contacts; applicability triggers; planned crops; legal/register status; open corrective actions |
| Each crop cycle | Crop and field area; planting/harvest; production; soil-cover and rotation records; IPM scouting; every pesticide application; relevant irrigation/withdrawal |
| Event-triggered, within program-defined notification window | Land-cover change, fire, erosion, spill, contamination, fish/wildlife mortality, prohibited input, grievance, rights conflict, threatened-species incident, restoration reversal |
| Annual | Sourcing lots; inventories; habitat extent/loss screen; legal/rights/safeguard attestations; management actions; incidents; evidence reconciliation |
| Every 2–3 years or trigger | Habitat/restoration condition, water quality, connectivity inputs; field verification |
| Pilot/leadership schedule | Repeated biological surveys, soil-biota sampling, invasive-species efficacy |

## 2. Required evidence hierarchy

1. **Direct measurement/observation:** calibrated meter, laboratory result, field observation, geospatial interpretation with source imagery.
2. **Contemporaneous record:** invoice, application log, scouting record, permit, dated photo, restoration work record.
3. **Official/external record:** government register, validated boundary, embargo/protected-area data, competent-authority decision.
4. **Attestation:** accepted only where specified; never sufficient alone for conversion, rights, prohibited-input, or outcome claims.

Every evidence item receives an `evidence_id`, date, owner, file hash or immutable link, type, coverage, access class, and reviewer status.

## 3. Geospatial capture

- Submit property, field, and habitat polygons rather than only hectare totals.
- Validate property geometry before metric calculation. Record source, date, CRS, positional accuracy, and topology results.
- Classify land cover using the approved legend and retain interpreter/model, imagery dates, confidence, and field-verification status.
- Record gross loss and gross gain separately. Never net restoration or regrowth against prohibited conversion.
- A potential conversion alert creates an investigation record; it remains unresolved until disposition and evidence are approved.

## 4. Farm-record capture

- Record pesticide applications at application-event level, not annual totals. Capture product, registration, active ingredients, formulation concentration, amount used, treated area, date/time, target pest, decision basis, weather, buffers, applicator, and incident linkage.
- Record crop cycles at field level. Shared/intercropped area must be flagged to avoid double counting.
- Record water withdrawal by source and measurement method; estimated values must include the estimation method and confidence.
- Record management actions and observations separately so implementation is not mistaken for condition change.

## 5. Field sampling and observations

- Predefine sampling frame, method version, season/window, minimum effort, equipment/calibration, and replicates.
- Use stable plot/site IDs and repeat locations unless the protocol explicitly requires random resampling.
- Record observer, date/time, effort, weather/site conditions, raw observations, detection/non-detection, and QA status.
- Laboratory samples require sample ID, chain of custody, lab/method, detection limits, units, and QA flags.

## 6. Validation controls

### Automated checks

- Required fields, type/domain, date order, positive quantities, valid IDs, and referential integrity.
- Area reconciliation: fields and habitat polygons must lie within the boundary; explain overlaps/gaps and boundary changes.
- Quantity reconciliation: pesticide purchase/inventory/application/disposal; sourced volume versus plausible production; withdrawal totals versus meter readings.
- Duplicate detection by ID, geometry, date, product, and quantity.
- Safeguard flags: post-cutoff change, prohibited product, missing rights evidence, unresolved grievance, protected-area disturbance, and unknown traceability.

### Reviewer checks

- Risk-based image and evidence review; field checks for material/high-risk discrepancies.
- Compare current and prior periods; require explanations for implausible changes.
- Independently repeat at least 20% of pilot observations as specified in version 1.

## 7. Missing, estimated, and corrected data

- Use explicit `not_applicable`, `not_collected`, `unknown`, and `estimated` statuses; never encode missing as zero.
- Estimated values require method, source inputs, confidence, and approver.
- A safeguard with missing required evidence is `unresolved/non-compliant pending review`.
- Corrections preserve original record, reason, date, editor, and approval trail.

## 8. Privacy and access

- Classify data as public, program-confidential, restricted personal/rights, or restricted ecological.
- Restrict names/contact information, grievances, land conflicts, consent records, and precise threatened-species locations.
- Obtain consent and define permitted use before collecting community, traditional-knowledge, or sensitive ecological data.
