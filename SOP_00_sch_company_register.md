# SOP: SCH Company Register

## File
`00_sch_company_register_v1_20260417.html`

## Purpose
Manage the company master register and generate canonical company folder names for the file server.

## Usage
1. Open the HTML file in a browser.
2. Grant folder access when prompted so the app can read/write `company_master.json`.
3. Enter or edit a company record using:
   - `Display name`
   - `NAMECODE` (up to 6 alphanumeric characters)
   - `TYP3` (legal entity type)
   - `VAT9` (9-digit VAT or registration number)
4. The generated `Company folder` field shows the canonical folder name.

## Canonical company folder rule
- `COMPANY_FOLDER = {NAMECODE}-{TYP3}-{VAT9}`
- `NAMECODE` is normalized to uppercase letters and digits only.
- `VAT9` is zero-padded to 9 digits if needed.

## Save workflow
- Save updates back to `company_master.json`.
- Use `Create company folder` to make the actual folder in the host file system when the chosen folder is available.

## Notes
- This app enforces the same company folder template used by the naming assistant and policy.
- If `NAMECODE` is blank, the display name is normalized as the fallback source for the company code.
