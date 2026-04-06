# SCH Payment Priority Board v4 — SOP Manual (EN)

**Application:** `03_payment_priority_board_v4_20260318.html`  
**Workspace:** `sch_file_server_management`  
**Manual date:** `2026-04-06`  
**Purpose:** Standard operating procedure for creating, reviewing, approving, notifying, paying, and archiving payment requests in the SCH local HTML payment board.

---

## 1. Purpose and scope

This manual explains how to operate the SCH Payment Priority Board v4. The tool is a **local HTML app** used by technical and economic teams to:

- register payment requests,
- calculate operational and economic impact,
- rank open requests by urgency,
- record `Tech`, `Econ`, and `Director` approvals,
- notify the next approver by email draft,
- move completed items into the paid archive.

This SOP applies to normal day-to-day use of the following file:

- `03_payment_priority_board_v4_20260318.html`

---

## 2. Operating model

### 2.1 What the board does

The board combines:

- **asset master data** from `assets_master.json`
- **company master data** from `company_master.json`
- **asset-type logic** from `asset_types.json`
- **economics and approval settings** from `payment_priority_config.json`
- **live request queue data** from `payment_priority_jobs.json`

The app then calculates:

- estimated lost production per day,
- lost revenue / exposure per day,
- Security and HSE risk scores,
- simple payback,
- a stable priority score,
- the ranked order of open requests.

### 2.2 What the board does **not** do

- It is **not** a central cloud system.
- It does **not** silently send emails through a mail server.
- It does **not** replace formal finance approval policy.
- It does **not** guarantee correct economics if the master data or config values are wrong.

> Email notifications in this version use **`mailto:`**. That means the app opens a **prefilled email draft** in the user’s mail client; the user still confirms/sends the message.

---

## 3. Required files

| File | Required | Purpose |
|---|---:|---|
| `assets_master.json` | Yes | Asset lookup and selected asset metadata |
| `company_master.json` | Yes | Company names and company linkage |
| `asset_types.json` | Yes | Asset type labels and display behavior |
| `payment_priority_config.json` | Yes | Economics, thresholds, weights, approval keywords, notification emails |
| `payment_priority_jobs.json` | Optional on first use | Open and paid request history |
| `contractors_master.json` | Optional | Loaded by the app but not central to core payment ranking |
| `legal_types.json` | Optional | Loaded by the app but not central to core payment ranking |

---

## 4. Roles and responsibilities

| Role | Main responsibility |
|---|---|
| **Technical user** | Creates requests, describes the issue, enters amount, production effect, and risk values |
| **Economic approver** | Reviews the ranking, evaluates spend urgency and financial reasonableness |
| **Director approver** | Gives the final management approval when required |
| **Board administrator** | Maintains master files, config settings, approval keywords, and notification emails |

---

## 5. Approval and email flow

The approval chain is strictly sequential:

1. **Tech approval**
2. **Econ approval**
3. **Director approval**
4. **Mark paid**

### 5.1 Notification behavior

When an approval is recorded:

- after **Tech approval**, the app opens an email draft to **Econ**,
- after **Econ approval**, the app opens an email draft to **Director**,
- after **Director approval**, no further email is needed.

### 5.2 Where approver emails are configured

In `payment_priority_config.json`:

```json
"approvals": {
  "emails": {
    "tech": "",
    "econ": "",
    "director": ""
  },
  "cc": {
    "tech": "",
    "econ": "",
    "director": ""
  }
}
```

### 5.3 Important note on sending

- The board opens a **mail draft**.
- The email is **not fully automatic server-side sending**.
- If an address is missing, the app can prompt the user to enter it.

---

## 6. Start-up procedure

### 6.1 Recommended start-up

1. Open `03_payment_priority_board_v4_20260318.html` in the browser.
2. Click **Open working folder**.
3. Select the folder that contains the JSON files.
4. Confirm the status cards show:
   - Folder connected
   - `4 / 4 required loaded`
   - Active assets count above `0` when applicable
5. If a jobs file already exists, confirm the board reports the number of requests loaded.

### 6.2 If folder access is blocked

If browser folder access is unavailable:

1. Use the manual load buttons:
   - `Load assets_master.json`
   - `Load company_master.json`
   - `Load asset_types.json`
   - `Load payment_priority_config.json`
   - optionally `Load jobs JSON`
2. Work normally in the board.
3. Save/export the jobs file back into the working folder when finished.

---

## 7. Daily operating procedure for Technical users

### 7.1 Create a new request

1. Open the board and load the working folder.
2. In **Search asset**, type part of the asset, company, location, project, or type.
3. Select the correct asset in the **Asset** dropdown.
4. Review the asset metadata panel:
   - Asset
   - Company
   - Type
   - Derived capacity
   - Typical CF
   - Value per kWh
5. In **Request name**, enter a short, meaningful title.
6. In **Problem description**, describe the technical issue and why payment is required.
7. Enter **Request amount (€)**.
8. Enter **Effect on production (%)**.
9. Set the four risk dropdowns:
   - Security likelihood
   - Security impact
   - HSE likelihood
   - HSE impact
10. Tick **Critical business obligation** only if the case must be treated as mandatory for business/legal reasons.
11. Review the calculated preview cards.
12. Click **Add to ranking**.
13. Confirm the request appears in **Open ranking**.

### 7.2 When to tick “Critical business obligation”

Use it only for cases such as:

- legal or regulatory exposure,
- tax or insurance obligations,
- supplier-stop / service-stop risk,
- grid or licensing compliance,
- contractually mandatory payment situations.

Do **not** tick it simply to push a normal request higher in the queue.

### 7.3 Update an existing request

1. Click the row in the open table.
2. Edit the form fields.
3. Click **Update selected**.
4. Re-check the ranking and score.

> If key fields change, prior approvals may reset. This is intentional control behavior.

---

## 8. Daily operating procedure for Economic users

### 8.1 Review the live ranking

1. Open the board and load the working folder.
2. Focus on the **Open ranking** table.
3. Review, in order:
   - `Priority class`
   - `Exposure/day`
   - `Security risk`
   - `HSE risk`
   - `Payback`
   - `Score (0-100)`
4. Click the most relevant row to inspect its details in the form panel.

### 8.2 Decide on payment order

Use the table as a decision support board. Priority is driven first by **Mandatory / Pay soon / Normal**, then by calculated score and exposure.

### 8.3 Approve the request

1. Click the relevant button in the row:
   - `Tech`
   - `Econ`
   - `Director`
2. Enter the approval keyword when prompted.
3. Confirm the status line updates.
4. If you are not the final approver, the app opens the next-step email draft.

### 8.4 Mark the request as paid

1. Ensure all three approvals show complete.
2. Click **Mark paid**.
3. Confirm the request disappears from the open queue.
4. Confirm the same request appears in **Paid archive**.

---

## 9. KPI meanings and formulas

### 9.1 Core inputs

The main user-entered fields are:

- `request_amount`
- `production_effect_pct`
- `security_likelihood`
- `security_impact`
- `hse_likelihood`
- `hse_impact`
- `business_critical`

The main asset/config inputs are:

- `capacity_mw`
- `typical_cf`
- `value_per_kwh`
- risk thresholds from `payment_priority_config.json`

### 9.2 Core formulas

```text
security_risk = security_likelihood × security_impact
hse_risk      = hse_likelihood × hse_impact

production_effect_fraction = production_effect_pct / 100

If calc_mode = mw_capacity:
  lost_kwh_day = capacity_mw × 1000 × 24 × typical_cf × production_effect_fraction
  lost_revenue_day = lost_kwh_day × value_per_kwh
Else:
  lost_kwh_day = 0
  lost_revenue_day = 0

total_exposure_day = lost_revenue_day
payback_days = request_amount / lost_revenue_day   (when lost_revenue_day > 0)
```

### 9.3 Priority class logic

```text
If business_critical = true:
  Mandatory
Else if max(security_risk, hse_risk) >= high_risk_threshold:
  Mandatory
Else if max(security_risk, hse_risk) >= medium_risk_threshold:
  Pay soon
Else:
  Normal
```

### 9.4 Score logic

The board calculates a stable absolute score using exposure, Security, HSE, efficiency, and a mild cost penalty. The score is used for ranking **inside** the priority class.

---

## 10. Ranking order used by the app

The final sorting order of open requests is:

1. `Mandatory`
2. `Pay soon`
3. `Normal`
4. business-critical items first within the same class
5. higher `priority_score`
6. higher `total_exposure_day`
7. higher max risk
8. older item first if still tied

This means a serious HSE/Security or mandatory business case will stay above a routine lower-risk item even if the routine item has a larger spend.

---

## 11. Button reference

| Button | Action |
|---|---|
| `Open working folder` | Connects the HTML app to the local working folder |
| `Save jobs JSON` | Writes the current queue to `payment_priority_jobs.json` |
| `Load jobs JSON` | Manually imports a saved jobs file |
| `Export open ranking CSV` | Exports ranking and archive data to CSV |
| `New empty jobs file` | Clears the in-memory request list and starts fresh |
| `Clear selection` | Clears the currently selected row/form state |
| `Add to ranking` | Creates a new request |
| `Update selected` | Saves changes to the selected request |
| `Clear form` | Empties the current input form |
| `Tech / Econ / Director` | Records the corresponding approval |
| `Mark paid` | Moves a fully approved request to archive |
| `Reopen` | Returns a paid item back to the open queue |
| `Delete` | Permanently removes the request from the current jobs set |

---

## 12. Data quality rules

To keep the board useful, the user must follow these rules:

- Always select the **correct asset**.
- Use realistic **production effect** values.
- Do not exaggerate risk scores.
- Use the **Critical business obligation** checkbox only when justified.
- Keep the request title short and specific.
- Keep the description factual and operational.
- Save the jobs file after material changes.

---

## 13. End-of-day routine

At the end of each working session:

1. Review newly added or updated requests.
2. Confirm approvals recorded correctly.
3. Click **Save jobs JSON**.
4. Confirm `payment_priority_jobs.json` was written successfully.
5. If required, export a CSV snapshot for reporting.
6. Keep a dated backup copy of the working folder before major cleanup or restructuring.

---

## 14. Troubleshooting

### 14.1 No assets appear in the dropdown

Check that all required master files were loaded:

- `assets_master.json`
- `company_master.json`
- `asset_types.json`
- `payment_priority_config.json`

### 14.2 The score looks wrong

Check:

- selected asset,
- capacity information,
- configured `typical_cf`,
- `value_per_kwh`,
- entered production effect,
- Security/HSE values.

### 14.3 A request cannot be marked paid

All three approvals must be completed first:

- Tech
- Econ
- Director

### 14.4 Email draft does not open

Check:

- a local mail client is installed,
- the browser allows `mailto:` handling,
- the next approver email exists in `payment_priority_config.json`.

### 14.5 Folder access fails

Use the manual JSON load buttons and then save/download the jobs file manually.

---

## 15. Control and security notes

- Approval keywords are a workflow control, **not** strong security.
- Replace placeholder keywords such as `change-me-tech` before production use.
- Restrict who can edit `payment_priority_config.json`.
- Keep backups of all JSON files.
- Do not run parallel uncontrolled copies of the same jobs file.

---

## 16. Recommended administrator checklist

Before live operational use, confirm that:

- [ ] `payment_priority_config.json` contains the correct approval keywords
- [ ] approver email addresses are configured
- [ ] `cc` settings are correct
- [ ] asset economics are reasonable by asset type
- [ ] the required JSON files are in one controlled working folder
- [ ] users know that email notifications open as drafts, not as silent sends

---

## 17. Record of expected outputs

The normal outputs of this app are:

- `payment_priority_jobs.json` — the live working queue and paid archive
- `payment_priority_open_and_paid.csv` — exported reporting snapshot
- email drafts for the next approver via `mailto:`

---

## 18. Summary

`03_payment_priority_board_v4_20260318.html` is the SCH local operating board for payment prioritization. Technical users create and describe requests; economic and management users approve them in sequence; the board ranks the queue using risk and economics; and the system preserves both the open queue and the paid archive in local JSON.
