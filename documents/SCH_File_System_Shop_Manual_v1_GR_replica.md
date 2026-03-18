# Εγχειρίδιο Λειτουργίας Συστήματος Αρχείων SCH

Λειτουργικό εγχειρίδιο για τη master πολιτική του συστήματος αρχείων, την εφαρμογή Company & Asset Admin και το SCH File Naming Assistant.

## 1. Τι καλύπτει αυτό το εγχειρίδιο
Το εγχειρίδιο εξηγεί πώς η SCH πρέπει να χρησιμοποιεί την πολιτική του συστήματος αρχείων στην καθημερινή εργασία, πώς να συντηρεί τα master δεδομένα εταιρειών και assets και πώς να δημιουργεί canonical ονόματα αρχείων και φακέλους προορισμού πριν από την αρχειοθέτηση.

## 2. Το λειτουργικό μοντέλο σε μία σελίδα
1. Δημιουργήστε ή συντηρήστε την εγγραφή της εταιρείας στο Company & Asset Admin.
2. Δημιουργήστε ή συντηρήστε την εγγραφή του asset στο Company & Asset Admin.
3. Χρησιμοποιήστε το SCH File Naming Assistant όταν πρόκειται να αρχειοθετήσετε ένα έγγραφο.
4. Επιλέξτε το asset, το workstream, το phase και το document type.
5. Αφήστε το assistant να δημιουργήσει το canonical filename και τον target folder.
6. Αποθηκεύστε το source document στον canonical folder του.
7. Χρησιμοποιήστε το `99_EXPORTS` μόνο ως προσωρινό outbox για αντίγραφα προς αποστολή, όχι ως τελική αποθήκευση.
8. Κρατήστε submissions, responses και receipts στον case folder για permitting· κρατήστε τα τελικά εκδοθέντα permits στον folder permits/licenses.

## 3. Βασικοί κανόνες ονοματοδοσίας και δομής
- Φάκελος εταιρείας: `{NAMECODE}-{TYP3}-{VAT9}`
- Φάκελος asset: `{TYPEID}_{PROJECT_NAME}_{LOCATION}`
- TYPEID: `{TYPE}{METRIC}-{SS}`
- Εσωτερικό όνομα αρχείου: `{TYPEID}_{PHASE}_{DOCTYPE}_{DESCRIPTION}_{DATE}_{VERSION}_{STATUS}.{EXT}`

## 4. Δομή φακέλων
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
- Ανοίγει έναν working folder που περιέχει τα `company_master.json`, `assets_master.json`, `legal_types.json` και `asset_types.json`.
- Δημιουργεί αυτόματα το `company_folder` από το `NAMECODE-TYP3-VAT9`.
- Δημιουργεί αυτόματα το `TYPEID` και το `asset_folder` από type, metric, sequence, project name και location.
- Επιβάλλει `NAMECODE` με κεφαλαία, έως 6 γράμματα.
- Χρησιμοποιεί dropdowns για legal types και asset types.
- Κανονικοποιεί το `project_name` σε πεζά και το `location` σε κεφαλαία.

## 6. SCH File Naming Assistant
- Φορτώνει τα `policy.json`, `company_master.json` και `assets_master.json`.
- Επιτρέπει στον χρήστη να επιλέξει asset, workstream, phase, doc type και conditional fields όπως stage ή counterparty.
- Επιστρέφει target folder, canonical filename, full path, routing explanation και validation output.
- Χρησιμοποιεί review badge για να δείξει στον χρήστη αν το αρχείο είναι έτοιμο για canonical filing.

## 7. Export packs έναντι canonical storage
- Τα canonical source files παραμένουν στους workstream folders τους.
- Το `03_PERMITTING_APPROVALS/02_SUBMISSIONS_RESPONSES` είναι ο case file για submissions και responses.
- Το `99_EXPORTS` είναι μόνο προσωρινό outbox.
- Τα τελικά εκδοθέντα permits πηγαίνουν στο `03_PERMITTING_APPROVALS/01_PERMITS_LICENSES`.

## 8. Εφαρμοσμένο παράδειγμα — Υποβολή για περιβαλλοντική έγκριση
- Τα source studies αναζητούνται στο 04_TECHNICAL_DESIGN/01_STUDIES.
- Τα τοπογραφικά και κτηματολογικά αποδεικτικά αναζητούνται στο 02_LAND_SITE/01_OWNERSHIP_SURVEYS.
- Οι συμφωνίες γης ή τα δικαιώματα αναζητούνται στο 02_LAND_SITE/02_AGREEMENTS.
- Τα σχέδια αναζητούνται στο 04_TECHNICAL_DESIGN/02_DRAWINGS.
- Τα αποδεικτικά τελών permit αναζητούνται στο 03_PERMITTING_APPROVALS/04_FEES_PAYMENTS.
- Το επίσημο application package αποθηκεύεται στο 03_PERMITTING_APPROVALS/02_SUBMISSIONS_RESPONSES.
- Ένα zipped upload set μπορεί να δημιουργηθεί προσωρινά στο 99_EXPORTS για portal submission.
- Μετά την αποστολή, το receipt, ο αριθμός πρωτοκόλλου, το acknowledgement και κάθε request for clarification παραμένουν στο 03_PERMITTING_APPROVALS/02_SUBMISSIONS_RESPONSES.
- Αν ζητηθούν περισσότερες πληροφορίες, τα αναθεωρημένα studies παραμένουν στους source folders τους, ενώ το reply package και η αλληλογραφία παραμένουν στο 02_SUBMISSIONS_RESPONSES.
- Η τελική εκδοθείσα περιβαλλοντική έγκριση πηγαίνει στο 03_PERMITTING_APPROVALS/01_PERMITS_LICENSES.

## 9. Συχνά λάθη που πρέπει να αποφεύγονται
- Χρήση του `99_EXPORTS` ως μόνιμη αποθήκευση.
- Διπλή αποθήκευση αμετάβλητων source files σε πολλούς canonical folders.
- Δημιουργία νέων προσωπικών δέντρων φακέλων.
- Αγνόηση του review flag στο assistant.
