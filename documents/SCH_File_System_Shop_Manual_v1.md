# SCH File System Shop Manual

Operational manual for the master file-system policy, the Company & Asset Admin app, and the SCH File Naming Assistant.

## 1. What this manual covers
This manual explains how SCH should use the file-system policy in daily work, how to maintain company and asset master data, and how to generate canonical file names and target folders before filing.

## 2. The operating model in one page
1. Create or maintain the company record in Company & Asset Admin.
2. Create or maintain the asset record in Company & Asset Admin.
3. Use SCH File Naming Assistant when you are about to file a document.
4. Choose the asset, workstream, phase, and document type.
5. Let the assistant generate the canonical filename and target folder.
6. Store the source document in its canonical folder.
7. Use `99_EXPORTS` only as a temporary outbox for sendable copies, not as final storage.
8. Keep submissions, responses, and receipts in the case folder for permitting; keep final issued permits in the permits/licenses folder.

## 3. Core naming and structure rules
- Company folder: `{NAMECODE}-{TYP3}-{VAT9}`
- Asset folder: `{TYPEID}_{PROJECT_NAME}_{LOCATION}`
- TYPEID: `{TYPE}{METRIC}-{SS}`
- Internal filename: `{TYPEID}_{PHASE}_{DOCTYPE}_{DESCRIPTION}_{DATE}_{VERSION}_{STATUS}.{EXT}`

## 4. Folder structure
- **AM** → `00_ASSET_MASTER`
- **PCD** → `01_DEVELOPMENT`
- **LS** → `02_LAND_SITE`
- **PMT** → `03_PERMITTING_APPROVALS`
- **TDE** → `04_TECHNICAL_DESIGN`
- **PRC** → `05_COMMERCIAL_PROCUREMENT`
- **FNI** → `06_FINANCE_INSURANCE`
- **CND** → `07_CONSTRUCTION_DELIVERY`
- **OPM** → `08_OPERATIONS_MAINTENANCE`
- **DCM** → `09_DECOMMISSIONING`
- **EXPORTS** → `99_EXPORTS`

## 5. Company & Asset Admin
- Opens a working folder that contains `company_master.json`, `assets_master.json`, `legal_types.json`, and `asset_types.json`.
- Generates `company_folder` automatically from `NAMECODE-TYP3-VAT9`.
- Generates `TYPEID` and `asset_folder` automatically from type, metric, sequence, project name, and location.
- Enforces NAMECODE uppercase max 6 letters.
- Uses legal-type and asset-type dropdowns.
- Normalizes project_name to lowercase and location to uppercase.

## 6. SCH File Naming Assistant
- Loads `policy.json`, `company_master.json`, and `assets_master.json`.
- Lets the user choose asset, workstream, phase, doc type, and conditional fields such as stage or counterparty.
- Returns target folder, canonical filename, full path, routing explanation, and validation output.
- Uses a review badge to tell the user whether the file is ready for canonical filing.

## 7. Export packs versus canonical storage
- Canonical source files stay in their workstream folders.
- `03_PERMITTING_APPROVALS/02_SUBMISSIONS_RESPONSES` is the case file for submissions and responses.
- `99_EXPORTS` is only a temporary outbox.
- Final issued permits go to `03_PERMITTING_APPROVALS/01_PERMITS_LICENSES`.

## 8. Applied example — Environmental approval submission
- Source studies are searched in 04_TECHNICAL_DESIGN/01_STUDIES.
- Topographical and cadastral evidence is searched in 02_LAND_SITE/01_OWNERSHIP_SURVEYS.
- Land agreements or rights are searched in 02_LAND_SITE/02_AGREEMENTS.
- Plans are searched in 04_TECHNICAL_DESIGN/02_DRAWINGS.
- Permit fee evidence is searched in 03_PERMITTING_APPROVALS/04_FEES_PAYMENTS.
- The official application package is stored in 03_PERMITTING_APPROVALS/02_SUBMISSIONS_RESPONSES.
- A zipped upload set may be created temporarily in 99_EXPORTS for portal submission.
- After sending, the receipt, protocol number, acknowledgement, and any clarification request stay in 03_PERMITTING_APPROVALS/02_SUBMISSIONS_RESPONSES.
- If more information is requested, revised studies stay in their source folders, while the reply package and correspondence stay in 02_SUBMISSIONS_RESPONSES.
- The final issued environmental approval goes to 03_PERMITTING_APPROVALS/01_PERMITS_LICENSES.

## 9. Common mistakes to avoid
- Using `99_EXPORTS` as permanent storage.
- Duplicating unchanged source files across many canonical folders.
- Creating new personal folder trees.
- Ignoring the review flag in the assistant.