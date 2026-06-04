# SOP: SCH Asset Register

## File
`01_sch_asset_register_v1_20260417.html`

## Purpose
Manage the asset master register and generate canonical asset identifiers and asset folder names.

## Usage
1. Open the HTML file in a browser.
2. Grant folder access when prompted so the app can read/write `assets_master.json`.
3. Add or edit asset records using fields such as:
   - `Type`
   - `Metric`
   - `SS`
   - `Project name`
   - `Location`
4. The app computes derived values automatically:
   - `TYPEID`
   - `Asset folder`
   - `Owner or project`

## Asset naming rules
- `TYPEID = {TYPE}{METRIC}-{SS}`
- `Metric` is calculated from source units and normalized to the base unit defined by each type.
- The generated `Asset folder` is:
  - `{TYPEID}_{PROJECT_NAME}_{LOCATION}`

## Supported metric input behavior
- Users may enter capacity or quantity values in supported units.
- The app normalizes input to a single `METRIC` value by applying the type-specific unit multiplier.
- The final `METRIC` encoding uses `p` to separate integer and fractional base units, e.g. `15p473`.

## Save workflow
- Save updates back to `assets_master.json`.
- Use the generated `Asset folder` value when creating the corresponding asset folder on disk.

## Notes
- This app provides the asset naming and folder rules that feed the file naming assistant and match the policy's asset folder topology.
