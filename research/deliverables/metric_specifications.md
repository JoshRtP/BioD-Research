# Metric specification sheets and protocol catalogue

## Common rules for every metric

- **No offsetting:** failed safeguards are ineligible and cannot be compensated by improvement scores.
- **Denominators:** retain both area and sourced-volume denominators; report coverage/missingness.
- **Baseline:** fixed historical cutoff for conversion; first complete verified measurement for improvements.
- **Aggregation:** report distributions and safeguard failures before averages. Portfolio results are volume- and risk-disaggregated.
- **QA/QC:** boundary validation, source lineage, date/version, field verification of material discrepancies, and independent risk-based assurance.
- **Uncertainty:** report classification/sampling uncertainty and natural variability; do not claim change within the method’s minimum detectable difference.
- **Acceptable claims:** stop at measured layer. “Implemented,” “reduced pressure,” “improved condition,” and “biological response” are distinct.

## M01 — Traceable sourcing coverage (required safeguard)

- **Decision use:** establish eligible denominator and enable every spatial safeguard.
- **Metric:** `verified volume traceable to validated rural-property boundary / total program volume × 100`.
- **Threshold:** 100% direct program volume; unknown origin is non-compliant, not low risk.
- **Frequency/data:** continuous transaction records; annual reconciliation of supplier, volume, property identifiers, and polygons.
- **Assurance/gaming:** reconcile mass balance and purchases; test duplicates, overlapping polygons, indirect suppliers, and volume plausibility.
- **Claim:** “X% of program volume was traceable to validated property boundaries.”

## M02 — No post-cutoff natural-ecosystem conversion (required safeguard)

- **Decision use:** prevent unacceptable harm.
- **Metric:** hectares of natural-ecosystem conversion after the strictest applicable cutoff; pass only at zero, subject to documented de minimis/error review rather than automatic tolerance.
- **Protocol:** validated property boundary; historical land-cover baseline; annual alert/current imagery; classify all natural ecosystems, not forest only; investigate alerts; assess linked indirect sourcing and leakage.
- **Frequency/assurance:** annual and event-triggered independent geospatial screen; field evidence for disputes.
- **Claim:** specific cutoff, ecosystem scope, traceability coverage, and assurance must be stated.

## M03/M04/M05/M06 — Legal, rights, species, and prohibited-input safeguards

| Metric | Evidence | Pass rule | Key integrity control |
|---|---|---|---|
| M03 protected/riparian/wetland/legal | Current permits/registers, official layers, property map, field checks | No material unresolved non-compliance; required protection/restoration plan active | CAR registration alone is not proof; verify status and overlaps |
| M04 rights/tenure/grievance/FPIC | Land-right evidence, conflict screen, accessible grievance records, rights-holder engagement | No unresolved rights violation; FPIC where applicable; no retaliation | Do not infer consent from absence of complaint |
| M05 threatened species | Risk/occurrence screen, protection plan, incident records | Protection in place; zero prohibited hunting/collection | Absence of database records is not proof of absence |
| M06 pesticides/contamination | Current legal/prohibited list, purchase/application records, buffers, incidents | Zero prohibited use and unremediated material breach | Reconcile purchased, stocked, applied, and disposed quantities |

## M07 — Native/semi-natural habitat extent and annual loss

- **Metric:** hectares and percentage of validated property/supply shed in native or semi-natural habitat; annual gross loss and gain reported separately.
- **Direction:** zero loss; maintain/increase extent. Gain never cancels prohibited loss.
- **Data/frequency:** annual GIS classification; field-check uncertain/material areas; retain ecosystem type and condition class.
- **Burden:** low–medium centrally; group-managed option.
- **Claim:** “Maintained X ha; no detected gross loss above the method’s detection threshold,” with uncertainty.

## M08 — Habitat-management-plan implementation and condition

- **Metric:** completed priority actions / due actions; plus a biome-appropriate condition index using fixed indicators (for example canopy/ground cover, native composition, degradation/fire/invasive pressure).
- **Sampling:** stratify by ecosystem type and condition; permanent plots/photo points; reference sites selected by Brazilian ecologists.
- **Frequency:** actions annually; condition every 2–3 years and after major events.
- **Missing rule:** no condition claim if comparable repeat measurement is absent.
- **Claim:** action completion supports a management claim; measured index change supports a condition claim.

## M09/M13 — Riparian/wetland protection and restoration

- **Metrics:** protected/required extent; gross disturbance; hectares under restoration; survival/establishment; native composition; condition trajectory.
- **Threshold:** legal and safeguard pass/fail; restoration milestones are conditional improvement requirements.
- **Protocol:** map hydrology and required areas; select reference ecosystem; record intervention, year, method, and maintenance; measure survival after establishment and condition over time.
- **Integrity:** planted hectares alone are not restored hectares; report reversals and failures.

## M10 — Pesticide toxic-load trajectory and IPM

- **Metric:** active ingredient, application area/rate, and a selected transparent ecotoxicity-risk index per hectare and per tonne, alongside IPM evidence and natural-predator monitoring.
- **Baseline/trajectory:** complete verified first season; set crop/region-specific reduction target only after pilot. Prohibited use remains a safeguard.
- **Data:** purchases, inventory, application logs, weather/buffers, pest scouting, decision thresholds, non-chemical controls.
- **Integrity:** mass alone is insufficient; prevent substitution to lower-dose/higher-toxicity products; report uncertainty in toxicity factors.
- **Claim:** “Modeled toxic load reduced X%” rather than “biodiversity increased.”

## M11 — Year-round soil cover, crop diversity, and erosion risk

- **Metrics:** percent days/area with living or residue cover; rotation/crop diversity; modeled/observed erosion-risk class; erosion incidents.
- **Direction:** increased cover/diversity and reduced erosion risk; tillage practice is supporting evidence, not outcome.
- **Frequency:** seasonal records and imagery; annual field/audit sample.
- **Claim:** practice/pressure reduction unless soil condition/biota is separately measured.

## M12/M15 — Water risk, withdrawal, incidents, and freshwater condition

- **Applicability:** universal basin-risk/incident screen; withdrawal metric where irrigation/material use exists; field water-quality metric where operations create material risk.
- **Metrics:** permitted and actual withdrawal; source/basin stress; contamination incidents; selected upstream/downstream or comparator parameters with justified design.
- **Integrity:** do not attribute basin-scale change to a farm without an appropriate design; protect sensitive location/community data.

## M14 — Landscape connectivity (conditional)

- **Trigger:** fragmented/priority landscapes, restoration investments, or collective-action claims.
- **Metric:** preselected transparent index such as effective connected habitat/patch adjacency, supported by corridor area and condition.
- **Scale/frequency:** supply shed/landscape; every 2–3 years.
- **Accountability:** distinguish changes controlled by participants from external landscape changes; monitor leakage.

## M16/M17/M18 — Leadership and pilot outcomes

| Metric | Recommended design | Status and claim limit |
|---|---|---|
| M16 pollinator/bird response | Stratified repeated surveys, fixed season/time, occupancy/detection model, comparator where feasible | Pilot first; no causal claim without design |
| M17 soil-biota response | Standardized sampling, lab QA, season/soil controls, pair with soil function | Research/pilot; methods and interpretability need validation |
| M18 invasive extent/control | Map extent and priority species; treatment and efficacy; prevent non-target harm | Conditional core when material; report control outcome, not generic biodiversity gain |

## Protocol selection gate

Before adopting a named tool or proprietary index, document: ecological rationale; formula; data rights; reproducibility; sensitivity; uncertainty; cost; auditability; biome validation; and whether changing providers breaks the baseline. Prefer transparent, interoperable protocols and retain raw observations.
