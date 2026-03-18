# SCH File Server SOP

This markdown is generated automatically from `master_policy.yaml`. Edit the master policy, then rerun `export_policies.py`.

## What this system is
- One legal company per top-level company folder.
- One asset folder per project or asset.
- Workstream is the physical filing axis.
- Phase stays in the filename and metadata, not as the main folder tree.
- FIN and CNT keep counterparties in the filename and metadata instead of deep folder trees.

## The four naming backbones
- Company folder: `{NAMECODE}-{TYP3}-{VAT9}`
- Asset folder: `{TYPEID}_{PROJECT_NAME}_{LOCATION}`
- TYPEID: `{TYPE}{METRIC}-{SS}`
- Internal filename: `{TYPEID}_{PHASE}_{DOCTYPE}_{DESCRIPTION}_{DATE}_{VERSION}_{STATUS}.{EXT}`

## What users enter
- `asset`
- `workstream`
- `phase`
- `doc_type`
- `description`
- `date`
- `version`
- `status`

Conditional fields:
- `FIN` also requires: `counterparty_name`
- `CNT` also requires: `counterparty_name`
- `DRWTEC` also requires: `deliverable_stage`
- `SDYTEC` also requires: `deliverable_stage`

## What the system derives
- `company_folder`
- `asset_folder`
- `type`
- `metric`
- `ss`
- `owner_or_project`

## Optional metadata
- `other_counterparty_name`
- `payment_category`
- `contract_category`
- `correspondence_scope`
- `report_scope`
- `drawing_discipline`
- `counterparty_role`

## Status values
`DRAFT`, `REVIEW`, `REVISED`, `FINAL`, `APPROVED`, `SIGNED`, `SENT`, `RECEIVED`, `SUPERSEDED`, `CANCELLED`

## Deliverable stages for stage-based technical documents
`CONCEPT`, `PRELIM`, `TENDER`, `IFC`, `SHOP`, `ASBUILT`, `RECORD`

## Workstreams
Use one of these workstream codes: `AM`, `PCD`, `LS`, `PMT`, `TDE`, `PRC`, `FNI`, `CND`, `OPM`, `DCM`, `EXPORTS`.

### AM — Asset Master
Canonical folder: `00_ASSET_MASTER`
Subfolders: `01_IDENTITY_REGISTERS`, `02_MASTER_DATA`, `03_STATUS_MILESTONES`
Review bucket: `99_MISC_REVIEW`

### PCD — Project Controls and Development
Canonical folder: `01_DEVELOPMENT`
Subfolders: `01_PROGRAMME_WBS`, `02_PROGRESS_REPORTING`, `03_COST_RISK_CHANGE`, `04_MEETINGS_ACTIONS`
Review bucket: `99_MISC_REVIEW`

### LS — Land and Site
Canonical folder: `02_LAND_SITE`
Subfolders: `01_OWNERSHIP_SURVEYS`, `02_AGREEMENTS`, `03_SITE_INVESTIGATIONS`, `04_PAYMENTS_COMPENSATIONS`
Review bucket: `99_MISC_REVIEW`

### PMT — Permitting and Approvals
Canonical folder: `03_PERMITTING_APPROVALS`
Subfolders: `01_PERMITS_LICENSES`, `02_SUBMISSIONS_RESPONSES`, `03_SUPPORT_CONTRACTS`, `04_FEES_PAYMENTS`
Review bucket: `99_MISC_REVIEW`

### TDE — Technical Design
Canonical folder: `04_TECHNICAL_DESIGN`
Subfolders: `01_STUDIES`, `02_DRAWINGS`, `03_MODELS_CALCULATIONS`, `04_CONSULTANT_CONTRACTS`, `05_PAYMENTS`
Review bucket: `99_MISC_REVIEW`

### PRC — Commercial and Procurement
Canonical folder: `05_COMMERCIAL_PROCUREMENT`
Subfolders: `01_RFQ_BIDS_EVALUATION`, `02_PURCHASE_ORDERS_SUPPLY_CONTRACTS`, `03_DELIVERIES_EXPEDITING`, `04_PAYMENTS`
Review bucket: `99_MISC_REVIEW`

### FNI — Finance and Insurance
Canonical folder: `06_FINANCE_INSURANCE`
Subfolders: `01_BUDGETS_CASHFLOW`, `02_BANKS_INSURANCE`, `03_PAYABLES`, `04_RECEIVABLES`, `05_TAX_STATUTORY`, `06_COST_REPORTING`
Review bucket: `99_MISC_REVIEW`

### CND — Construction Delivery
Canonical folder: `07_CONSTRUCTION_DELIVERY`
Subfolders: `01_DRAWINGS`, `02_SITE_DIARY_PROGRESS`, `03_BOQ_BOM_QUANTITIES`, `04_CONTRACTS_SUBCONTRACTS`, `05_PAYMENTS_IPC_COST`, `06_QAQC_HSE`, `07_HANDOVER_CLOSEOUT`
Review bucket: `99_MISC_REVIEW`

### OPM — Operations and Maintenance
Canonical folder: `08_OPERATIONS_MAINTENANCE`
Subfolders: `01_ASSET_DOCUMENTS`, `02_SERVICE_CONTRACTS`, `03_PAYMENTS`, `04_REPORTING_EVENTS`
Review bucket: `99_MISC_REVIEW`

### DCM — Decommissioning
Canonical folder: `09_DECOMMISSIONING`
Subfolders: `01_STUDIES_PERMITS`, `02_CLOSING_AGREEMENTS`, `03_PAYMENTS`, `04_DISPOSAL_SALE_RECORDS`
Review bucket: `99_MISC_REVIEW`

### EXPORTS — Exports
Canonical folder: `99_EXPORTS`

## Document types
| Doc type | Meaning | Routing family | Extra user input |
|---|---|---|---|
| `PER` | Permit or License | `fixed` | — |
| `DRWTEC` | Technical Drawing | `by_stage` | deliverable_stage |
| `SDYTEC` | Technical Study | `by_stage` | deliverable_stage |
| `FIN` | Finance Document | `by_workstream` | counterparty_name |
| `CNT` | Contract Document | `by_workstream` | counterparty_name |
| `COR` | Correspondence | `by_workstream_with_fallback` | — |
| `REP` | Report | `by_workstream_with_fallback` | — |
| `MIN` | Minutes | `by_workstream_with_fallback` | — |
| `DAT` | Data File | `by_workstream_with_fallback` | — |
| `IMG` | Image or Photo | `by_workstream_with_fallback` | — |
| `QAQC` | QAQC Record | `fixed` | — |
| `HSE` | HSE Record | `fixed` | — |

## Daily filing flow
1. Select the asset.
2. Select the workstream.
3. Select the phase.
4. Select the document type.
5. Add deliverable stage only for `DRWTEC` and `SDYTEC`.
6. Add counterparty for `FIN` and `CNT`.
7. Write a short canonical description.
8. Set date, version, and status.
9. Let the system build the canonical filename and route the file.
10. If confidence is low, send the file to the same workstream `99_MISC_REVIEW` bucket.

## Canonical examples
- Company folder: `SCH-IKE-123456789` following `{NAMECODE}-{TYP3}-{VAT9}`
- Asset folder: `PVS15p473-01_Project-Name_Location` following `{TYPEID}_{PROJECT_NAME}_{LOCATION}`
- Internal filename: `PVS15p473-01_DE_FIN_HABITATIO-design-invoice_20260315_v01_RECEIVED.pdf` following `{TYPEID}_{PHASE}_{DOCTYPE}_{DESCRIPTION}_{DATE}_{VERSION}_{STATUS}.{EXT}`

## Path and naming limits
- Max full path: `240` characters
- Max filename: `120` characters
- Max folder name: `64` characters
- Max depth: `12` segments

## Review and special folders
- `99_MISC_REVIEW` is the temporary review bucket inside a workstream.
- `_SUPERSEDED` stores older replaced files kept for traceability.
- `_DUPLICATED` stores exact duplicate non-keepers.
- `_DEPRECATED` stores obsolete files kept only for reference.
- `_BACKUP` stores emergency or noncanonical backups.
- `99_EXPORTS` is for temporary export packs only, not canonical storage.

## What not to do
- Do not create phase-first trees.
- Do not create counterparty subfolder hierarchies under workstreams.
- Do not allow uncontrolled custom subfolders in canonical storage.
- Do not use 99_EXPORTS as the final canonical home.

## Regeneration command
```bash
python /mnt/data/export_policies.py
```
