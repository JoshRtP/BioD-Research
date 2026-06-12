# Minimum farm submission checklist

This checklist translates the version 2 data model into a plain-language farm request. The exact platform may collect the same fields through forms, APIs, GIS files, or group-managed records.

## A. Onboarding package — submit once and update when changed

### Farm and legal/rights identity

- Program farm ID, farm name, operator type, municipality/state, primary biome, total validated property area, CAR/SICAR identifier where applicable, tenure/use-right status and supporting evidence.
- Current rights/tenure conflicts, required consent/FPIC status, and grievance-channel information. Sensitive case details go only to the restricted rights process.

### Spatial package

Submit validated GIS geometry and metadata for:

- complete property boundary;
- every stable management field;
- every native/semi-natural habitat, riparian, wetland, protected, restoration, and other priority-habitat polygon;
- every relevant water source and monitoring site.

For every geometry submit: geometry ID/version, file/link, CRS/EPSG, capture date, source method, positional accuracy, calculated area where relevant, and topology/validation status.

### Baseline package

- Applicable conversion cutoff date and historical/current land-cover evidence.
- Habitat ecosystem/management class, legal designation, area, reference ecosystem where applicable, priority flag, and management-plan link.
- Water-source type/use, permit requirement/status, metering status, and basin-risk class.
- Field slope, erosion-risk class, and adjacency to sensitive features.

## B. Submit for every reporting year

- Reporting-period dates, signed safeguard attestation, and open corrective-action count.
- Every sourced/sold lot: buyer/destination, commodity, harvest/transfer dates, tonnes, traceability model, origin fields where required, and document number.
- Updated legal/register/permit evidence and any changed boundary or classification.
- Annual land-cover result for every habitat polygon, including imagery/method, current class, gross loss/gain/degradation, change dates, confidence, field verification, and investigation disposition.
- Current habitat-management actions and approved condition observations when scheduled.
- All incidents, grievances, assurance findings, protection actions, and corrective actions.
- Every crop cycle and required soil-cover observations.
- Water withdrawal and water-quality records where applicable.
- Restoration and invasive-species monitoring where applicable.

## C. Submit for every crop cycle and management field

### Crop-cycle record

- Field ID; crop and cultivar where available; planting and harvest dates; managed area; shared/intercrop area flag; production tonnes; tillage system; preceding crop cycle; residue management.

### Every pesticide application event

- Crop cycle and field; date/time; product trade name and registration; active ingredients and concentration; product amount/unit; treated hectares; target pest; decision basis; weather/rain; maintained buffer distance; prohibited-product flag; linked incident if relevant.

### IPM scouting

- Field/crop cycle; scouting date; target; method; sampling effort; raw pest measure; action threshold; natural-enemy measure where applicable; decision; non-chemical action.

### Soil-cover/erosion observations

- Field/crop cycle/date; approved method; living cover %, residue cover %, bare soil %, number of observation points/images; erosion sign and type.

## D. Event-triggered submission

Immediately create an incident/investigation record for potential conversion, fire, spill, contamination, buffer breach, erosion, protected-area disturbance, wildlife mortality, hunting/collection, restoration reversal, prohibited-product use, rights conflict, or serious grievance.

Each record needs date, location, type, affected area where relevant, severity, safeguard-failure assessment, authority notification where required, root cause, corrective-action status, and evidence.

## E. Conditional monitoring

| Trigger | Additional farm-level data |
|---|---|
| Irrigation or material water use | Source-level withdrawal periods/volumes, measurement method, meter readings where used, irrigated fields, permit limit, exceedance flag |
| Material freshwater risk | Approved water samples: site position, time, parameter, result/unit, method/lab, detection limit, QA, threshold/reference, exceedance |
| Restoration obligation/claim | Intervention/maintenance/monitoring/reversal record, area, year, sampled/surviving individuals, native cover/richness, condition observations |
| Habitat condition schedule | Stable plot/site, date, method, raw indicator/value/unit, effort, reference, derived score, disturbance flags |
| Invasive-species materiality | Species, occupied area/density, method, treatment, follow-up efficacy, non-target harm |
| Threatened-species risk | Species/risk evidence, list/version, observation type, protection action and status; precise location restricted |
| Leadership biological monitoring | Repeat survey site/date/time, method, effort/unit, weather/site conditions, raw detections/non-detections, identification validation |

## F. Evidence submitted with all applicable records

Each evidence file/item requires an evidence ID, type, date, coverage description, immutable link, file hash, owner/issuer, access class, review status, and expiry where applicable.
