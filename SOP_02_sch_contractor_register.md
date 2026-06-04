# SOP: SCH Contractor Register

## File
`02_sch_contractor_register_v1_20260417.html`

## Purpose
Manage the contractors master register used by SCH file workflows.

## Usage
1. Open the HTML file in a browser.
2. Grant folder access when prompted so the app can read/write `contractors_master.json`.
3. Add or update contractor records with details such as:
   - contractor name
   - contractor code
   - contact details
   - notes and status
4. Save changes to persist updates to `contractors_master.json`.

## Notes
- Contractor master data is used by the broader SCH system for reference and filing consistency.
- The app keeps contractor information separate from company and asset masters.
- Contractor records do not directly generate canonical file or folder names, but they support contract-sensitive workflows in the file naming assistant.
