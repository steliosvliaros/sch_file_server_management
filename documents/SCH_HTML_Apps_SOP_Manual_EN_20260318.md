## 2. Common operating rules

- Keep the three HTML files and their JSON files in one controlled working folder.
- Prefer `Open working folder` whenever the browser allows it. This gives the apps direct read/write access to the local JSON files.
- If folder access is blocked, use the manual JSON load buttons and then save or download the resulting JSON back into the working folder.
- Treat the JSON files as the system of record. The HTML files are interfaces, not the permanent database.
- Always keep a dated backup of the working folder before major edits.

## 3. SOP for 00_company_assets_admin_scroll_lists_v09_20260318.html

### 3.1 Purpose

This tool is the master-data editor of the local system. It is used to create, review, edit, and delete company, asset, and contractor records that are later consumed by the naming assistant and, where relevant, by the payment board.

### 3.2 Files expected in the working folder

- `company_master.json`
- `assets_master.json`
- `contractors_master.json`
- `legal_types.json`
- `asset_types.json`

### 3.3 Main actions

- Open the working folder and load the current JSON masters.
- Create or revise company records.
- Create or revise asset records.
- Create or revise contractor/counterparty records.
- Save back to the folder or download the updated JSON files.

### 3.4 Standard procedure

1. Open the HTML file locally in the browser.
2. Click **Open working folder** and select the folder that contains the master JSON files.
3. Check that the companies, assets, and contractors are visible in the scrolling lists and tables.
4. Select the required record or create a new one.
5. Complete or update the key fields.
6. Save the record.
7. Save the relevant JSON back to the working folder.
8. Re-open the record from the list and confirm the saved values.

### 3.5 Field guidance

- Company records should contain the correct legal type, VAT, canonical company folder, and active status.
- Asset records should contain the correct company link, asset type, metric or input value, location, asset folder, and active status.
- Contractor records should contain a canonical uppercase naming form where required by downstream file naming logic.

### 3.6 Good practice

- Do not create duplicate company or asset records for the same real entity.
- Use consistent canonical spellings before saving.
- Save immediately after each material edit.
- If a contractor is no longer used, mark it inactive rather than losing historical meaning.

## 4. SOP for 01_sch_file_naming_assistant_standalone_v8_20260318.html

### 4.1 Purpose

This tool generates the canonical filename and the canonical destination folder according to the SCH naming policy. It is the interface used to turn a real document into a policy-compliant filename and path.

### 4.2 Files expected in the working folder

- `policy.json`
- `company_master.json`
- `assets_master.json`
- `contractors_master.json`

### 4.3 What the tool does

- Reads the policy and master files.
- Lets the user choose the company, asset, phase, workstream, document type, status, and related description fields.
- Normalizes the description according to the rules.
- Builds the canonical filename.
- Builds the destination path under the policy tree.
- Checks path and filename length limits.
- Shows a review/ready state and explanation.
- Can create policy folders when the browser grants folder access.

### 4.4 Standard procedure

1. Open the HTML file locally.
2. Load the working folder or manually load the four required JSON files.
3. Select the company and asset.
4. Select phase, workstream, document type, deliverable stage, status, and date.
5. Fill the description inputs, including counterparties where the document type needs them.
6. Review the generated filename and destination path.
7. Read the validation/explanation area.
8. If the result is acceptable, copy the filename and path or create the policy folders if needed.
9. Rename and file the document accordingly.

### 4.5 What to verify before using the result

- The company and asset are the correct records.
- The phase and document type are correct for the document's real meaning.
- The description follows the naming rules and does not contain junk words such as `final`, `copy`, `scan`, or duplicated dates.
- Counterparty names are canonical when a FIN or CNT document requires them.
- The resulting path and filename do not violate the length limits.

### 4.6 Good practice

- Use the naming assistant before you manually rename files.
- Prefer the nearest meaningful workstream and the correct document type rather than a vague generic bucket.
- If the output is still ambiguous, stop and correct the metadata or master data first.

## 5. SOP for 03_payment_priority_board_v4_20260318.html

### 5.1 Purpose

This tool turns technical requests into a ranked open-payment queue for the economic department. The technical side enters the request, risk, and production-effect values. The app resolves the selected asset, applies the economics configuration, calculates the request impact, and maintains a ranked open queue plus a paid archive.

### 5.2 Files expected in the working folder

- `assets_master.json`
- `company_master.json`
- `asset_types.json`
- `payment_priority_config.json`
- optionally `payment_priority_jobs.json`

### 5.3 Roles

- The technical department creates and updates request records.
- The economic department reviews the open ranking, decides what to pay first, and marks paid requests as paid.
- Paid records are removed from the open ranking and kept in the archive.

### 5.4 Standard technical workflow

1. Open the HTML file locally.
2. Load the working folder.
3. Check that the asset dropdown is populated.
4. Select the relevant asset.
5. Enter the request title and a short problem description.
6. Enter the request amount in EUR.
7. Enter the effect on production as a percentage.
8. Select Security likelihood and impact from the verbal dropdowns.
9. Select HSE likelihood and impact from the verbal dropdowns.
10. Tick **Critical business obligation** only when the request must be treated as mandatory for legal, tax, insurance, supplier-stop, grid, or equivalent business reasons.
11. Review the calculated impact cards.
12. Save the request.

### 5.5 Standard economic workflow

1. Open the same board and load the same working folder.
2. Review the **Open ranking** list.
3. Click a row to select the request and inspect the full details.
4. Read the calculated impact, payback, score, and priority reason.
5. Decide what to pay first.
6. Mark paid requests as paid.
7. Confirm that the request moved from the open ranking to the paid archive.
8. Save the updated `payment_priority_jobs.json`.

### 5.6 KPI cards and dashboard meaning

- **Lost kWh/day**: estimated daily production loss driven by asset capacity, configured typical capacity factor, and the entered production effect.
- **Lost revenue/day**: monetary value of the lost kWh/day.
- **Total exposure/day**: current daily economic exposure used in ranking.
- **Security risk** and **HSE risk**: likelihood multiplied by impact on a 1 to 5 scale.
- **Payback**: simple payback in days.
- **Score (0-100)**: stable absolute score used for ranking inside the priority bucket.
- The bottom graphs summarize the most important open requests, open exposure by asset, and the count of requests by bucket.

## 6. KPI calculations, ranking logic, and reasoning

### 6.1 Capacity and type assumptions

The payment board reads the selected asset from `assets_master.json`. The asset type is used to find the corresponding economic model in `payment_priority_config.json`. For MW-based project types, the board can estimate lost production. For disabled or unimplemented calculation modes, the request is still tracked and ranked, but the production-loss KPI may be zero or only partially available.

### 6.2 Core formulas used by the payment board

```text
production_effect_fraction = production_effect_pct / 100
security_risk = security_likelihood * security_impact
hse_risk = hse_likelihood * hse_impact

If calc_mode = mw_capacity:
  lost_kwh_day = capacity_mw * 1000 * 24 * typical_cf * production_effect_fraction
  lost_revenue_day = lost_kwh_day * value_per_kwh
Else:
  lost_kwh_day = 0 unless another mode is implemented
  lost_revenue_day = 0 unless another mode is implemented

total_exposure_day = lost_revenue_day
payback_days = request_amount / lost_revenue_day   (only when lost_revenue_day > 0)
```

### 6.3 Priority class logic

The app first assigns a bucket before it ranks inside the bucket.

```text
If business_critical = true:
  priority_class = Mandatory
Else if max(security_risk, hse_risk) >= 16:
  priority_class = Mandatory
Else if max(security_risk, hse_risk) >= 8:
  priority_class = Pay soon
Else:
  priority_class = Normal
```

This means that legal, insurance, tax, supplier-stop, or equivalent obligations can be forced into the Mandatory class even when the production-loss value is low.

### 6.4 Stable absolute score

Inside the bucket, the board uses a stable absolute score rather than a score that depends on the current queue maximum. The default v4 logic is:

```text
exposure_score   = clamp(total_exposure_day / 5000)
security_score   = clamp(security_risk / 25)
hse_score        = clamp(hse_risk / 25)
efficiency_ratio = (total_exposure_day * 30) / request_amount
efficiency_score = clamp(efficiency_ratio / 1)
cost_penalty     = clamp(request_amount / 50000)

raw_score =
    0.35 * exposure_score
  + 0.20 * security_score
  + 0.20 * hse_score
  + 0.20 * efficiency_score
  - 0.05 * cost_penalty

priority_score = max(raw_score * 100, 0)
```

### 6.5 Final sorting order

The open queue is sorted in this order:

1. `Mandatory`, then `Pay soon`, then `Normal`
2. business-critical items first inside the bucket
3. higher `priority_score`
4. higher `total_exposure_day`
5. higher max risk
6. older item first when the above are equal

### 6.6 Why this reasoning is sound

- Risk is separated from economics through the bucket system, so serious HSE or Security cases are not buried by a purely financial ranking.
- The score is stable because it uses fixed business scales rather than today's maximum values.
- Efficiency is included through the 30-day avoided-loss ratio, which helps distinguish a highly effective payment from an expensive low-return payment.
- The size penalty is mild, so the model does not automatically punish large but justified payments.
- The business-critical override gives management a controlled way to force mandatory treatment for non-technical but real obligations.

### 6.7 Limits and cautions

- The quality of `lost_kwh_day` and `lost_revenue_day` depends on the quality of the asset master and the economics configuration.
- Datacenter, hotel, hydroponics, BESS, and other non-standard project types may need type-specific economic models rather than the simple MW-capacity method.
- Simple payback is only an indicator; it assumes the payment restores the lost revenue and that the loss is continuous.
- If the wrong asset is selected, all derived KPIs can become misleading.

## 7. Data governance and controls

- Keep only one active authoritative copy of each master JSON file.
- Use backups before bulk edits.
- Record the date of major structural changes to the masters.
- When possible, update the admin tool first, then use the naming assistant and payment board against the refreshed masters.
- Do not manually edit the same JSON file in multiple places at the same time.

## 8. Troubleshooting

### 8.1 The browser does not read or write the folder

- Use a Chromium-based browser that supports the folder picker.
- Open the HTML locally, then click **Open working folder**.
- If direct folder access is unavailable, load the JSON files manually and use the download buttons.

### 8.2 A dropdown is empty

- The required JSON file may not be loaded.
- The JSON schema may be incomplete or malformed.
- The record may exist but may be inactive or missing a required field.

### 8.3 A filename or path looks wrong

- Check the selected company and asset.
- Recheck document type and workstream.
- Recheck the description and counterparties.
- Verify that the underlying master data is correct.

### 8.4 A payment request shows zero production loss

- The project type may be configured with `calc_mode = disabled`.
- The asset may not have a usable capacity value.
- The production effect may be zero.
- The economics configuration may be missing for that asset type.

## 9. Worked examples

### Example 1 - Add a company and asset in the admin tool

Objective: create the master records before using the naming assistant.

1. Open `00_company_assets_admin_scroll_lists_v09_20260318.html`.
2. Load the working folder.
3. Create company `SCH SOLAR LARISA IKE` with the correct legal type, VAT, and company folder.
4. Create asset `PVS1200-01_helios_larisa` linked to that company and mark it active.
5. Save the company and asset.
6. Save back to `company_master.json` and `assets_master.json`.

Result: the new records are now available to the other tools.

### Example 2 - Generate a canonical filename with the naming assistant

Objective: produce a valid contract filename for a civil-works document.

Inputs:
- Asset: `PVS1200-01_helios_larisa`
- Phase: `DEV`
- Document type: `CNT`
- Counterparty: `HABITATIO`
- Other counterparty: `MYTILINEOS`
- Meaning stem: `civil-works`
- Date: `2026-03-18`
- Version: `v01`
- Status: `draft`

Expected canonical output pattern:

```text
PVS1200-01_DEV_CNT_HABITATIO-to-MYTILINEOS-civil-works_2026-03-18_v01_draft.pdf
```

The user should then review the destination folder, confirm that the length limits are respected, and file the document under the generated path.

### Example 3 - Enter and rank a payment request

Objective: show how the technical team creates a request and how the economic team interprets the ranking.

Inputs:
- Asset capacity: 12 MW (derived from the selected asset/master)
- Type economics: typical CF = 0.15, value per kWh = EUR 0.02
- Request amount: EUR 18,000
- Production effect: 35%
- Security likelihood = 2, Security impact = 3
- HSE likelihood = 1, HSE impact = 2
- Business critical = No

Calculation:

```text
lost_kwh_day = 12 * 1000 * 24 * 0.15 * 0.35 = 15,120 kWh/day
lost_revenue_day = 15,120 * 0.02 = EUR 302.40/day
security_risk = 2 * 3 = 6
hse_risk = 1 * 2 = 2
payback_days = 18,000 / 302.40 = 59.5 days
```

Interpretation:
- Max risk is 6, so the request stays in `Normal` rather than `Pay soon` or `Mandatory`.
- The board still gives it a positive score because it has real exposure and a measurable payback.
- The economic team compares this request with the other open items in the ranking and decides whether to pay it now or after higher-bucket cases.

### Example 4 - Use the business-critical override

Objective: push a legally required payment into the Mandatory bucket.

Inputs:
- Request title: annual insurance renewal
- Production effect: 0%
- Security and HSE risks: low
- Business critical: Yes

Interpretation:
- Even if production loss is zero, the request becomes `Mandatory` because management explicitly identified a critical business obligation.
- This prevents legal, tax, insurance, or equivalent obligations from being incorrectly delayed by a purely technical-loss ranking.
