# Worked farm-metric examples

All values below are fictional and illustrate calculations only. They are not program thresholds or evidence that a claim is valid.

## M01 — Traceable sourcing coverage

A farm submits three lots:

| Lot | Volume (t) | Traceability/evidence status | Counts as traceable? |
|---|---:|---|---|
| L1 | 500 | Physical identity preserved; origin fields and documents verified | Yes |
| L2 | 300 | Segregated; property origin verified under approved rule | Yes |
| L3 | 200 | Origin unknown | No |

`traceable coverage = 100 × (500 + 300) / (500 + 300 + 200) = 80%`

Output: `80% traceable; 200 t unknown`. The unknown lot remains in the denominator.

## M02 and M07 — Conversion safeguard and habitat extent

A validated 1,000 ha property contains unique current habitat polygons totaling 340 ha. Annual comparison identifies 4 ha gross habitat loss after the cutoff, 2 ha gross gain, and 3 ha uncertain change pending investigation.

- `current habitat extent = 100 × 340 / 1,000 = 34%`
- M07 reports `340 ha / 34% extent`, `4 ha gross loss`, `2 ha gross gain`, and `3 ha uncertain` separately.
- M02 status is **failed** if the 4 ha is confirmed natural-ecosystem conversion after the cutoff. It remains **unresolved** while the 3 ha alert is pending.
- Netting loss against gain (`4 − 2 = 2 ha`) is prohibited.

## M08 — Habitat action completion and condition

A habitat plan has 10 actions due this year. Seven are verified complete, one is completed but not verified, and two are overdue.

`verified action completion = 100 × 7 / 10 = 70%`

A comparable habitat-condition protocol recorded a baseline score of 58 and current score of 64:

`condition change = 64 − 58 = +6 score points`

Report the 70% action result and +6 condition result separately; one does not substitute for the other.

## M10 — Active ingredient and toxic-load trajectory

For one 100 ha crop cycle, two example applications have already been unit-normalized:

| Application | Active ingredient mass | Approved toxicity factor | Modeled toxic load |
|---|---:|---:|---:|
| A1 | 20 kg a.i. | 3 factor units/kg | 60 units |
| A2 | 10 kg a.i. | 8 factor units/kg | 80 units |

- `active ingredient intensity = (20 + 10) / 100 = 0.30 kg a.i./ha`
- `toxic load intensity = (60 + 80) / 100 = 1.40 index units/ha`

The result must retain the toxicity-factor source/version. A lower active-ingredient mass could still have higher toxic load, so mass alone is not the risk metric.

## M11 — Area-weighted soil cover

Two fields are observed in the same approved key window:

| Field | Area | Total cover |
|---|---:|---:|
| F1 | 60 ha | 90% |
| F2 | 40 ha | 50% |

`area-weighted cover = ((60 × 90) + (40 × 50)) / (60 + 40) = 74%`

The program also reports bare-soil observations, crop/rotation diversity, erosion-risk area, and incidents separately. An observation outside the approved window is retained but excluded from this comparable result.

## M12 — Water withdrawal intensity

Valid source-level records total 120,000 m³ withdrawal for 300 irrigated hectares and 1,000 tonnes of eligible production:

- `withdrawal intensity by area = 120,000 / 300 = 400 m³/ha`
- `withdrawal intensity by production = 120,000 / 1,000 = 120 m³/t`

These intensities do not by themselves show basin or biodiversity improvement. Permit status, basin risk, estimation/metering method, incidents, and any approved water-quality results remain separate.

## M13 — Restoration survival and reversal

Comparable monitoring of one restoration cohort assesses 240 planted/established individuals and finds 192 surviving:

`survival = 100 × 192 / 240 = 80%`

The farm separately reports intervention area, native cover/richness, condition score, and any reversal area. “80% survival” does not mean “80% restored,” and the original intervention hectares are not automatically verified restored hectares.

## M16 — Valid zero detections

A pollinator survey has four protocol-compliant repeat events at one site, with raw detections `3, 0, 1, 0`. Both zeros are retained because effort, timing, method, and conditions were recorded. A missed survey is `not_collected`, not a zero. Occupancy or response estimates are produced only through the approved detection-aware analysis across enough sites and repeats.
