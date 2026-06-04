# SOP: SCH File Naming Assistant

## File
`04_sch_naming_assistant_v1_20260417.html`

## Purpose
Generate canonical filenames and destination folders for SCH files using `policy.json`, company master, asset master, and contractor master data.

## Usage
1. Open the HTML file in a browser.
2. Click `Open working folder` and grant access to load the JSON masters from the working folder.
3. Verify that the following files are available in the working folder:
   - `policy.json`
   - `company_master.json`
   - `assets_master.json`
   - `contractors_master.json`
4. Enter the filing metadata:
   - `Company folder`
   - `Asset folder`
   - `TYPEID`
   - `Workstream`
   - `Phase`
   - `Document type`
   - `Description`
   - `Date`
   - `Version`
   - `Status`
5. For special document types, provide additional inputs:
   - `DRWTEC` or `SDYTEC`: add `Deliverable stage`
   - `FIN`: add `Counterparty`, `FIN document stem`, and `FIN specific`
   - `CNT`: add `Counterparty`
6. Review the generated canonical filename and target destination folder.
7. If review is required, use the `Force review` option.

## Naming rules enforced
- `FIN` and `CNT` place counterparties into the description segment rather than into folder hierarchy.
- `DRWTEC` and `SDYTEC` route by deliverable stage.
- `COR`, `REP`, `MIN`, `DAT`, `IMG` route by workstream with a review fallback.
- `PER`, `QAQC`, and `HSE` use fixed route folders.

## Validation checks
The app validates:
- filename length against 120 characters
- full path length against 240 characters
- path depth against 12 segments
- required fields for the selected document type and mode
- `FIN specific` values as 1 to 9 uppercase letters/numbers

## Notes
- The assistant uses `policy.json` route registry and folder index for destination resolution.
- Portfolio Shared mode uses `__PORTFOLIO_SHARED__` route folders instead of company asset folders.
- If `policy.json` changes, reload the app after saving the updated file.
