## 2. Κοινοί κανόνες λειτουργίας

- Κρατήστε τα τρία HTML αρχεία και τα JSON αρχεία τους σε έναν ελεγχόμενο φάκελο εργασίας.
- Προτιμήστε το `Open working folder` όταν το επιτρέπει ο browser. Έτσι τα apps αποκτούν άμεση πρόσβαση ανάγνωσης/εγγραφής στα τοπικά JSON.
- Αν η πρόσβαση στον φάκελο μπλοκάρεται, χρησιμοποιήστε τα manual JSON load buttons και μετά αποθηκεύστε ή κατεβάστε το νέο JSON πίσω στον φάκελο εργασίας.
- Θεωρήστε τα JSON αρχεία ως το system of record. Τα HTML αρχεία είναι interfaces και όχι η μόνιμη βάση δεδομένων.
- Κρατάτε πάντα dated backup του φακέλου εργασίας πριν από σημαντικές αλλαγές.

## 3. SOP για το 00_company_assets_admin_scroll_lists_v09_20260318.html

### 3.1 Σκοπός

Το εργαλείο αυτό είναι ο editor των master data του τοπικού συστήματος. Χρησιμοποιείται για δημιουργία, έλεγχο, τροποποίηση και διαγραφή εταιρειών, assets και contractors που στη συνέχεια καταναλώνονται από το naming assistant και, όπου χρειάζεται, από το payment board.

### 3.2 Αρχεία που αναμένονται στον φάκελο εργασίας

- `company_master.json`
- `assets_master.json`
- `contractors_master.json`
- `legal_types.json`
- `asset_types.json`

### 3.3 Κύριες ενέργειες

- Άνοιγμα του φακέλου εργασίας και φόρτωση των τρεχόντων JSON masters.
- Δημιουργία ή αναθεώρηση company records.
- Δημιουργία ή αναθεώρηση asset records.
- Δημιουργία ή αναθεώρηση contractor/counterparty records.
- Αποθήκευση πίσω στον φάκελο ή download των ενημερωμένων JSON αρχείων.

### 3.4 Τυπική διαδικασία

1. Ανοίξτε το HTML τοπικά στον browser.
2. Πατήστε **Open working folder** και επιλέξτε τον φάκελο που περιέχει τα master JSON αρχεία.
3. Ελέγξτε ότι εταιρείες, assets και contractors εμφανίζονται στις scrolling lists και στους πίνακες.
4. Επιλέξτε το απαιτούμενο record ή δημιουργήστε νέο.
5. Συμπληρώστε ή ενημερώστε τα βασικά πεδία.
6. Αποθηκεύστε το record.
7. Αποθηκεύστε το αντίστοιχο JSON πίσω στον φάκελο εργασίας.
8. Ξανανοίξτε το record από τη λίστα και επιβεβαιώστε τις αποθηκευμένες τιμές.

### 3.5 Οδηγίες πεδίων

- Τα company records πρέπει να περιέχουν σωστό legal type, VAT, canonical company folder και active status.
- Τα asset records πρέπει να περιέχουν σωστό company link, asset type, metric ή input value, location, asset folder και active status.
- Τα contractor records πρέπει να έχουν canonical uppercase naming form όπου αυτό απαιτείται από τη downstream λογική ονοματοδοσίας αρχείων.

### 3.6 Καλή πρακτική

- Μην δημιουργείτε διπλά company ή asset records για την ίδια πραγματική οντότητα.
- Χρησιμοποιείτε συνεπείς canonical ορθογραφίες πριν από το save.
- Κάνετε save αμέσως μετά από κάθε ουσιαστική αλλαγή.
- Αν ένας contractor δεν χρησιμοποιείται πλέον, προτιμήστε να τον κάνετε inactive αντί να χαθεί το ιστορικό νόημα.

## 4. SOP για το 01_sch_file_naming_assistant_standalone_v8_20260318.html

### 4.1 Σκοπός

Το εργαλείο αυτό δημιουργεί το canonical filename και το canonical destination folder σύμφωνα με το SCH naming policy. Είναι το interface που μετατρέπει ένα πραγματικό έγγραφο σε filename και path συμβατά με την πολιτική.

### 4.2 Αρχεία που αναμένονται στον φάκελο εργασίας

- `policy.json`
- `company_master.json`
- `assets_master.json`
- `contractors_master.json`

### 4.3 Τι κάνει το εργαλείο

- Διαβάζει το policy και τα master files.
- Επιτρέπει στον χρήστη να επιλέξει company, asset, phase, workstream, document type, status και σχετικά description fields.
- Κανονικοποιεί το description σύμφωνα με τους κανόνες.
- Δημιουργεί το canonical filename.
- Δημιουργεί το destination path μέσα στο policy tree.
- Ελέγχει limits μήκους για path και filename.
- Δείχνει review/ready state και explanation.
- Μπορεί να δημιουργήσει policy folders όταν ο browser δώσει folder access.

### 4.4 Τυπική διαδικασία

1. Ανοίξτε το HTML τοπικά.
2. Φορτώστε τον φάκελο εργασίας ή φορτώστε χειροκίνητα τα τέσσερα απαιτούμενα JSON αρχεία.
3. Επιλέξτε company και asset.
4. Επιλέξτε phase, workstream, document type, deliverable stage, status και date.
5. Συμπληρώστε τα description inputs, περιλαμβάνοντας counterparties όπου το document type το απαιτεί.
6. Ελέγξτε το generated filename και το destination path.
7. Διαβάστε την περιοχή validation/explanation.
8. Αν το αποτέλεσμα είναι αποδεκτό, αντιγράψτε το filename και το path ή δημιουργήστε τους policy folders αν χρειάζεται.
9. Μετονομάστε και αρχειοθετήστε το έγγραφο ανάλογα.

### 4.5 Τι πρέπει να ελεγχθεί πριν χρησιμοποιηθεί το αποτέλεσμα

- Η company και το asset είναι τα σωστά records.
- Το phase και το document type είναι σωστά σε σχέση με την πραγματική σημασία του εγγράφου.
- Το description ακολουθεί τους κανόνες ονοματοδοσίας και δεν περιέχει junk words όπως `final`, `copy`, `scan` ή διπλές ημερομηνίες.
- Τα counterparty names είναι canonical όταν ένα FIN ή CNT document τα απαιτεί.
- Το προκύπτον path και filename δεν παραβιάζουν τα length limits.

### 4.6 Καλή πρακτική

- Χρησιμοποιείτε το naming assistant πριν κάνετε manual rename αρχείων.
- Προτιμήστε το nearest meaningful workstream και το σωστό document type αντί για ένα αόριστο generic bucket.
- Αν το output παραμένει αμφίσημο, σταματήστε και διορθώστε πρώτα τα metadata ή τα master data.

## 5. SOP για το 03_payment_priority_board_v4_20260318.html

### 5.1 Σκοπός

Το εργαλείο αυτό μετατρέπει τεχνικά αιτήματα σε ranked open-payment queue για το οικονομικό τμήμα. Η τεχνική πλευρά εισάγει το αίτημα, το ρίσκο και τις τιμές επίδρασης στην παραγωγή. Το app λύνει το επιλεγμένο asset, εφαρμόζει το economics configuration, υπολογίζει το impact του αιτήματος και διατηρεί ranked open queue μαζί με paid archive.

### 5.2 Αρχεία που αναμένονται στον φάκελο εργασίας

- `assets_master.json`
- `company_master.json`
- `asset_types.json`
- `payment_priority_config.json`
- προαιρετικά `payment_priority_jobs.json`

### 5.3 Ρόλοι

- Το τεχνικό τμήμα δημιουργεί και ενημερώνει request records.
- Το οικονομικό τμήμα ελέγχει το **Open ranking**, αποφασίζει τι θα πληρώσει πρώτο και σημειώνει τα πληρωμένα αιτήματα ως paid.
- Τα paid records αφαιρούνται από το open ranking και κρατούνται στο archive.

### 5.4 Τυπικό technical workflow

1. Ανοίξτε το HTML τοπικά.
2. Φορτώστε τον φάκελο εργασίας.
3. Ελέγξτε ότι το asset dropdown έχει γεμίσει.
4. Επιλέξτε το σχετικό asset.
5. Καταχωρήστε request title και σύντομη problem description.
6. Καταχωρήστε request amount σε EUR.
7. Καταχωρήστε effect on production ως ποσοστό.
8. Επιλέξτε Security likelihood και impact από τα verbal dropdowns.
9. Επιλέξτε HSE likelihood και impact από τα verbal dropdowns.
10. Τσεκάρετε **Critical business obligation** μόνο όταν το αίτημα πρέπει να θεωρηθεί mandatory για νομικούς, φορολογικούς, ασφαλιστικούς, supplier-stop, grid ή αντίστοιχους επιχειρησιακούς λόγους.
11. Ελέγξτε τα calculated impact cards.
12. Αποθηκεύστε το request.

### 5.5 Τυπικό economic workflow

1. Ανοίξτε το ίδιο board και φορτώστε τον ίδιο φάκελο εργασίας.
2. Ελέγξτε τη λίστα **Open ranking**.
3. Κάντε click σε μία γραμμή για να επιλέξετε το request και να δείτε τα πλήρη στοιχεία.
4. Διαβάστε το calculated impact, το payback, το score και το priority reason.
5. Αποφασίστε ποιο θα πληρωθεί πρώτο.
6. Σημειώστε τα πληρωμένα requests ως paid.
7. Επιβεβαιώστε ότι το request μετακινήθηκε από το open ranking στο paid archive.
8. Αποθηκεύστε το ενημερωμένο `payment_priority_jobs.json`.

### 5.6 Σημασία KPI cards και dashboard

- **Lost kWh/day**: εκτιμώμενη ημερήσια απώλεια παραγωγής που προκύπτει από capacity του asset, configured typical capacity factor και το καταχωρημένο production effect.
- **Lost revenue/day**: χρηματική αξία των χαμένων kWh/ημέρα.
- **Total exposure/day**: το τρέχον ημερήσιο οικονομικό exposure που χρησιμοποιείται στην κατάταξη.
- **Security risk** και **HSE risk**: likelihood επί impact σε κλίμακα 1 έως 5.
- **Payback**: simple payback σε ημέρες.
- **Score (0-100)**: stable absolute score που χρησιμοποιείται για ranking μέσα στο priority bucket.
- Τα γραφήματα στο κάτω μέρος συνοψίζουν τα σημαντικότερα open requests, το open exposure ανά asset και την κατανομή των requests ανά bucket.

## 6. Υπολογισμοί KPI, λογική κατάταξης και αιτιολόγηση

### 6.1 Παραδοχές capacity και type

Το payment board διαβάζει το επιλεγμένο asset από το `assets_master.json`. Ο τύπος του asset χρησιμοποιείται για να βρεθεί το αντίστοιχο economic model στο `payment_priority_config.json`. Για project types που βασίζονται σε MW, το board μπορεί να εκτιμήσει χαμένη παραγωγή. Για disabled ή μη υλοποιημένα calculation modes, το request εξακολουθεί να παρακολουθείται και να κατατάσσεται, αλλά το production-loss KPI μπορεί να είναι μηδενικό ή μερικώς διαθέσιμο.

### 6.2 Βασικοί τύποι που χρησιμοποιεί το payment board

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

### 6.3 Λογική priority class

Το app πρώτα δίνει bucket και μετά κάνει ranking μέσα στο bucket.

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

Αυτό σημαίνει ότι legal, insurance, tax, supplier-stop ή αντίστοιχες υποχρεώσεις μπορούν να μπουν υποχρεωτικά στο Mandatory ακόμα κι όταν η production-loss αξία είναι χαμηλή.

### 6.4 Stable absolute score

Μέσα στο bucket, το board χρησιμοποιεί stable absolute score και όχι score που εξαρτάται από το σημερινό μέγιστο της ουράς. Η προεπιλεγμένη λογική του v4 είναι:

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

### 6.5 Τελική σειρά ταξινόμησης

Η open queue ταξινομείται με τη σειρά:

1. `Mandatory`, μετά `Pay soon`, μετά `Normal`
2. business-critical items πρώτα μέσα στο bucket
3. υψηλότερο `priority_score`
4. υψηλότερο `total_exposure_day`
5. υψηλότερο max risk
6. παλαιότερο item πρώτα όταν τα παραπάνω είναι ίσα

### 6.6 Γιατί αυτή η αιτιολόγηση είναι σωστή

- Το ρίσκο χωρίζεται από τα οικονομικά μέσω του bucket system, ώστε σοβαρές HSE ή Security περιπτώσεις να μη θάβονται από μια καθαρά οικονομική κατάταξη.
- Το score είναι σταθερό επειδή χρησιμοποιεί fixed business scales και όχι τα μέγιστα της τρέχουσας ουράς.
- Η αποδοτικότητα συμπεριλαμβάνεται μέσω του 30-day avoided-loss ratio, που βοηθά να ξεχωρίσει μια πολύ αποτελεσματική πληρωμή από μια ακριβή πληρωμή χαμηλής απόδοσης.
- Το size penalty είναι ήπιο, ώστε το μοντέλο να μην τιμωρεί αυτόματα μεγάλες αλλά δικαιολογημένες πληρωμές.
- Το business-critical override δίνει στη διοίκηση ελεγχόμενο τρόπο να επιβάλλει mandatory treatment για μη τεχνικές αλλά πραγματικές υποχρεώσεις.

### 6.7 Όρια και προειδοποιήσεις

- Η ποιότητα των `lost_kwh_day` και `lost_revenue_day` εξαρτάται από την ποιότητα του asset master και του economics configuration.
- Datacenter, hotel, hydroponics, BESS και άλλα μη τυπικά project types μπορεί να χρειάζονται type-specific economic models αντί για την απλή μέθοδο MW-capacity.
- Το simple payback είναι μόνο δείκτης· υποθέτει ότι η πληρωμή αποκαθιστά τη χαμένη αξία και ότι η απώλεια είναι συνεχής.
- Αν επιλεγεί λάθος asset, όλα τα derived KPIs μπορεί να γίνουν παραπλανητικά.

## 7. Data governance και έλεγχοι

- Κρατήστε μόνο ένα ενεργό authoritative αντίγραφο για κάθε master JSON file.
- Χρησιμοποιήστε backups πριν από μαζικές αλλαγές.
- Καταγράψτε την ημερομηνία σημαντικών δομικών αλλαγών στα masters.
- Όπου είναι δυνατό, ενημερώστε πρώτα το admin tool και μετά χρησιμοποιήστε naming assistant και payment board πάνω στα ανανεωμένα masters.
- Μην επεξεργάζεστε χειροκίνητα το ίδιο JSON ταυτόχρονα σε πολλά σημεία.

## 8. Troubleshooting

### 8.1 Ο browser δεν διαβάζει ή δεν γράφει τον φάκελο

- Χρησιμοποιήστε browser τύπου Chromium που υποστηρίζει folder picker.
- Ανοίξτε το HTML τοπικά και μετά πατήστε **Open working folder**.
- Αν η άμεση πρόσβαση στον φάκελο δεν είναι διαθέσιμη, φορτώστε χειροκίνητα τα JSON και χρησιμοποιήστε τα download buttons.

### 8.2 Ένα dropdown είναι άδειο

- Ίσως δεν έχει φορτωθεί το απαιτούμενο JSON.
- Το JSON schema μπορεί να είναι ελλιπές ή malformed.
- Το record μπορεί να υπάρχει αλλά να είναι inactive ή να λείπει required field.

### 8.3 Ένα filename ή path φαίνεται λάθος

- Ελέγξτε την επιλεγμένη company και το asset.
- Ελέγξτε ξανά document type και workstream.
- Ελέγξτε ξανά το description και τους counterparties.
- Επιβεβαιώστε ότι τα underlying master data είναι σωστά.

### 8.4 Ένα payment request δείχνει μηδενική production loss

- Ο project type μπορεί να είναι ρυθμισμένος με `calc_mode = disabled`.
- Το asset μπορεί να μην έχει usable capacity value.
- Το production effect μπορεί να είναι μηδέν.
- Μπορεί να λείπει economics configuration για αυτόν τον asset type.

## 9. Παραδείγματα λειτουργίας

### Παράδειγμα 1 - Προσθήκη company και asset στο admin tool

Στόχος: δημιουργία master records πριν χρησιμοποιηθεί το naming assistant.

1. Ανοίξτε το `00_company_assets_admin_scroll_lists_v09_20260318.html`.
2. Φορτώστε τον φάκελο εργασίας.
3. Δημιουργήστε company `SCH SOLAR LARISA IKE` με σωστό legal type, VAT και company folder.
4. Δημιουργήστε asset `PVS1200-01_helios_larisa` συνδεδεμένο με αυτή την company και σημειώστε το ως active.
5. Αποθηκεύστε company και asset.
6. Αποθηκεύστε πίσω τα `company_master.json` και `assets_master.json`.

Αποτέλεσμα: τα νέα records είναι πλέον διαθέσιμα στα άλλα εργαλεία.

### Παράδειγμα 2 - Παραγωγή canonical filename με το naming assistant

Στόχος: παραγωγή σωστού contract filename για civil-works document.

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

Αναμενόμενο canonical output pattern:

```text
PVS1200-01_DEV_CNT_HABITATIO-to-MYTILINEOS-civil-works_2026-03-18_v01_draft.pdf
```

Στη συνέχεια ο χρήστης πρέπει να ελέγξει το destination folder, να επιβεβαιώσει ότι τηρούνται τα length limits και να αρχειοθετήσει το έγγραφο στο generated path.

### Παράδειγμα 3 - Καταχώρηση και ranking payment request

Στόχος: να φανεί πώς το τεχνικό τμήμα δημιουργεί request και πώς το οικονομικό τμήμα ερμηνεύει την κατάταξη.

Inputs:
- Asset capacity: 12 MW (προκύπτει από το επιλεγμένο asset/master)
- Type economics: typical CF = 0.15, value per kWh = EUR 0.02
- Request amount: EUR 18,000
- Production effect: 35%
- Security likelihood = 2, Security impact = 3
- HSE likelihood = 1, HSE impact = 2
- Business critical = No

Υπολογισμός:

```text
lost_kwh_day = 12 * 1000 * 24 * 0.15 * 0.35 = 15,120 kWh/day
lost_revenue_day = 15,120 * 0.02 = EUR 302.40/day
security_risk = 2 * 3 = 6
hse_risk = 1 * 2 = 2
payback_days = 18,000 / 302.40 = 59.5 days
```

Ερμηνεία:
- Το μέγιστο ρίσκο είναι 6, άρα το request μένει στο `Normal` και δεν πηγαίνει σε `Pay soon` ή `Mandatory`.
- Το board παρ' όλα αυτά του δίνει θετικό score επειδή έχει πραγματικό exposure και μετρήσιμο payback.
- Το οικονομικό τμήμα συγκρίνει αυτό το request με τα υπόλοιπα open items της κατάταξης και αποφασίζει αν θα το πληρώσει τώρα ή μετά από υψηλότερα buckets.

### Παράδειγμα 4 - Χρήση business-critical override

Στόχος: να μεταφερθεί μια νομικά απαιτούμενη πληρωμή στο Mandatory bucket.

Inputs:
- Request title: annual insurance renewal
- Production effect: 0%
- Security και HSE risks: χαμηλά
- Business critical: Yes

Ερμηνεία:
- Ακόμα κι αν η production loss είναι μηδενική, το request γίνεται `Mandatory` επειδή η διοίκηση το αναγνώρισε ως critical business obligation.
- Έτσι αποφεύγεται να καθυστερούν νομικές, φορολογικές, ασφαλιστικές ή αντίστοιχες υποχρεώσεις λόγω ενός καθαρά technical-loss ranking.
