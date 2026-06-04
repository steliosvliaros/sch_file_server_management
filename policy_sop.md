# SCH File Server Policy SOP

## Purpose
This policy SOP describes the file, folder, and routing rules implemented by `policy.json` and used by the SCH HTML apps.

## Policy alignment
- `policy.json` is the active master policy used by `04_sch_naming_assistant_v1_20260417.html`.
- The six HTML apps reviewed already implement the same naming, route, and validation rules defined in `policy.json`.
- No direct changes to `policy.json` were required during the review.
- The source policy is generated from `policy_yaml/master_policy.yaml` using `src/export_policies.py`.

## Core naming backbones
- Company folder: `{NAMECODE}-{TYP3}-{VAT9}`
- Asset folder: `{TYPEID}_{PROJECT_NAME}_{LOCATION}`
- TYPEID: `{TYPE}{METRIC}-{SS}`
- Internal filename: `{TYPEID}_{PHASE}_{DOCTYPE}_{DESCRIPTION}_{DATE}_{VERSION}_{STATUS}.{EXT}`
- Portable export filename: `{COMPANY_FOLDER}_{INTERNAL_FILENAME}`

## Folder and route topology
- Company root: `{COMPANY_FOLDER}`
- Asset root: `{COMPANY_FOLDER}/ASSETS/{ASSET_FOLDER}`
- Special asset folders: `_SUPERSEDED`, `_DUPLICATED`, `_DEPRECATED`, `_BACKUP`
- Portfolio shared root: `__PORTFOLIO_SHARED__`
- Portfolio shared standard folders route to `00_PORTFOLIO_MASTER`, `01_SHARED_CONTRACTS`, `02_SHARED_REGISTERS`, `03_SHARED_REPORTING`

## Document type routing
`policy.json` defines routing in `routing.route_registry` with three modes:
- `fixed`: route to a single target folder regardless of workstream or stage
- `by_stage`: route based on `deliverable_stage`, with fallback if stage is missing
- `by_workstream` / `by_workstream_with_fallback`: route by workstream, with a fallback bucket when no workstream-specific route exists

### Document type behaviors
- `PER`: fixed route
- `DRWTEC`: by stage
- `SDYTEC`: by stage
- `FIN`: by workstream
- `CNT`: by workstream
- `COR`: by workstream with fallback
- `REP`: by workstream with fallback
- `MIN`: by workstream with fallback
- `DAT`: by workstream with fallback
- `IMG`: by workstream with fallback
- `QAQC`: fixed route
- `HSE`: fixed route

## Special naming rules
- `FIN` and `CNT` are `counterparty_sensitive` and require `counterparty_name`.
- `FIN` also requires a `FIN document stem` and a `FIN specific` value.
- `DRWTEC` and `SDYTEC` are `stage_sensitive` and require `deliverable_stage`.
- Counterparty values are normalized into lowercase hyphenated text.

## Validation constraints
- Maximum full path length: 240 characters
- Maximum filename length: 120 characters
- Maximum folder name length: 64 characters
- Maximum path depth: 12 segments

## When to update the policy
Update `policy.json` when any of the following change:
- workstream or review bucket structure
- document type routing mode or target folders
- filename backbone, type catalog, or doc type metadata behavior
- company or asset folder templates

## Policy maintenance workflow
1. Edit the authoritative YAML in `policy_yaml/master_policy.yaml`.
2. Run `src/export_policies.py` to regenerate `policy.json` and derived YAML.
3. Verify updated routing and folder IDs in `policy.json`.
4. Test `04_sch_naming_assistant_v1_20260417.html` against the revised policy.
