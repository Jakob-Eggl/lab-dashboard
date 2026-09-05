"""
Curated catalog of common blood test parameters.

Reference ranges are general orientation values compiled from widely used
German lab standards (e.g. typical ranges used by Roche/LADR-affiliated
laboratories, Pschyrembel Klinisches Woerterbuch). They are NOT a substitute
for the reference range printed on an individual's actual lab report, since
ranges can vary slightly between laboratories and measurement methods.

Each parameter has one or more "ranges" entries. A range applies if the
person's gender matches (or the range is for "all") AND their age in years
falls within [min_age, max_age].
"""

PARAMETERS = [
    # ---------------- Leberwerte ----------------
    {
        "code": "ggt",
        "name": "GGT",
        "full_name": "Gamma-Glutamyltransferase",
        "unit": "U/l",
        "category": "Leber",
        "description": (
            "Ein Enzym, das vor allem in der Leber und den Gallengaengen vorkommt. "
            "Gilt als empfindlicher Marker fuer Erkrankungen der Leber und Gallenwege."
        ),
        "high_meaning": (
            "Erhoehte Werte koennen auf eine Belastung der Leber hinweisen, etwa durch "
            "Alkohol, bestimmte Medikamente, Fettleber oder Gallenwegserkrankungen."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 10, "high": 71},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 6, "high": 42},
        ],
    },
    {
        "code": "got_ast",
        "name": "GOT (AST)",
        "full_name": "Glutamat-Oxalacetat-Transaminase (Aspartat-Aminotransferase)",
        "unit": "U/l",
        "category": "Leber",
        "description": (
            "Ein Enzym, das in Leber-, Herz- und Muskelzellen vorkommt. Wird bei "
            "Zellschaeden in diesen Geweben ins Blut freigesetzt."
        ),
        "high_meaning": (
            "Erhoehte Werte koennen auf eine Leberzellschaedigung hindeuten, aber auch "
            "durch intensiven Sport oder Muskelverletzungen verursacht sein."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 10, "high": 50},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 10, "high": 35},
        ],
    },
    {
        "code": "gpt_alt",
        "name": "GPT (ALT)",
        "full_name": "Glutamat-Pyruvat-Transaminase (Alanin-Aminotransferase)",
        "unit": "U/l",
        "category": "Leber",
        "description": (
            "Ein Enzym, das ueberwiegend in der Leber vorkommt und als spezifischerer "
            "Marker fuer Leberzellschaeden gilt als die GOT."
        ),
        "high_meaning": (
            "Erhoehte Werte deuten meist auf eine Belastung oder Schaedigung der "
            "Leberzellen hin, z. B. durch Fettleber, Virushepatitis, Alkohol oder Medikamente."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 10, "high": 50},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 10, "high": 35},
        ],
    },
    {
        "code": "bilirubin",
        "name": "Bilirubin gesamt",
        "full_name": "Gesamtbilirubin",
        "unit": "mg/dl",
        "category": "Leber",
        "description": (
            "Ein Abbauprodukt des roten Blutfarbstoffs Haemoglobin, das ueber die Leber "
            "und Galle ausgeschieden wird."
        ),
        "high_meaning": (
            "Erhoehte Werte koennen auf eine Leber- oder Gallenwegserkrankung, "
            "vermehrten Blutzellabbau (Haemolyse) oder eine Bilirubin-Stoffwechselstoerung "
            "(z. B. Morbus Meulengracht) hinweisen."
        ),
        "low_meaning": "Niedrige Werte haben in der Regel keine klinische Bedeutung.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0.2, "high": 1.2},
        ],
    },
    {
        "code": "albumin",
        "name": "Albumin",
        "full_name": "Albumin",
        "unit": "g/dl",
        "category": "Leber",
        "description": (
            "Das wichtigste Bluteiweiss, das ueberwiegend in der Leber gebildet wird und "
            "u. a. fuer den Fluessigkeitshaushalt und den Transport von Stoffen im Blut wichtig ist."
        ),
        "high_meaning": "Erhoehte Werte sind selten und meist durch Fluessigkeitsmangel bedingt.",
        "low_meaning": (
            "Niedrige Werte koennen auf eine eingeschraenkte Leberfunktion, "
            "Mangelernaehrung, Entzuendungen oder Eiweissverlust (z. B. ueber die Niere) hinweisen."
        ),
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 3.5, "high": 5.2},
        ],
    },
    # ---------------- Nierenwerte ----------------
    {
        "code": "kreatinin",
        "name": "Kreatinin",
        "full_name": "Kreatinin",
        "unit": "mg/dl",
        "category": "Niere",
        "description": (
            "Ein Abbauprodukt des Muskelstoffwechsels, das ueber die Nieren ausgeschieden "
            "wird. Gilt als klassischer Marker der Nierenfunktion."
        ),
        "high_meaning": (
            "Erhoehte Werte koennen auf eine eingeschraenkte Nierenfunktion hinweisen, "
            "haengen aber auch von der Muskelmasse ab."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 0.7, "high": 1.2},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 0.5, "high": 0.9},
        ],
    },
    {
        "code": "harnstoff",
        "name": "Harnstoff",
        "full_name": "Harnstoff (Urea)",
        "unit": "mg/dl",
        "category": "Niere",
        "description": "Ein Endprodukt des Eiweissstoffwechsels, das ueber die Nieren ausgeschieden wird.",
        "high_meaning": (
            "Erhoehte Werte koennen auf eine eingeschraenkte Nierenfunktion, "
            "Fluessigkeitsmangel oder eine sehr eiweissreiche Ernaehrung hinweisen."
        ),
        "low_meaning": "Niedrige Werte koennen bei eiweissarmer Ernaehrung oder Lebererkrankungen auftreten.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 17, "high": 43},
        ],
    },
    {
        "code": "egfr",
        "name": "eGFR",
        "full_name": "geschaetzte glomerulaere Filtrationsrate",
        "unit": "ml/min/1,73m²",
        "category": "Niere",
        "description": (
            "Ein aus Kreatinin, Alter und Geschlecht berechneter Schaetzwert dafuer, wie "
            "viel Blut die Nieren pro Minute filtern."
        ),
        "high_meaning": "Hohe Werte sind unauffaellig.",
        "low_meaning": (
            "Niedrigere Werte deuten auf eine eingeschraenkte Nierenfunktion hin; "
            "Werte unter 60 ueber laengere Zeit gelten als abklaerungsbeduerftig."
        ),
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 90, "high": 130},
        ],
    },
    {
        "code": "harnsaeure",
        "name": "Harnsäure",
        "full_name": "Harnsaeure",
        "unit": "mg/dl",
        "category": "Niere",
        "description": "Ein Abbauprodukt des Purinstoffwechsels, das ueber die Nieren ausgeschieden wird.",
        "high_meaning": (
            "Erhoehte Werte koennen auf Gicht hinweisen oder durch purinreiche Ernaehrung, "
            "Alkohol oder Uebergewicht beguenstigt werden."
        ),
        "low_meaning": "Niedrige Werte haben meist keine klinische Bedeutung.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 3.4, "high": 7.0},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 2.4, "high": 5.7},
        ],
    },
    # ---------------- Blutfette ----------------
    {
        "code": "cholesterin_gesamt",
        "name": "Cholesterin gesamt",
        "full_name": "Gesamtcholesterin",
        "unit": "mg/dl",
        "category": "Blutfette",
        "description": "Summe aller Cholesterinanteile im Blut (LDL, HDL und weitere Fraktionen).",
        "high_meaning": (
            "Erhoehte Werte gelten als ein Risikofaktor fuer Herz-Kreislauf-Erkrankungen, "
            "wobei die Aufteilung in LDL und HDL aussagekraeftiger ist als der Gesamtwert allein."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 200},
        ],
    },
    {
        "code": "ldl",
        "name": "LDL-Cholesterin",
        "full_name": "Low Density Lipoprotein Cholesterin",
        "unit": "mg/dl",
        "category": "Blutfette",
        "description": (
            "Wird umgangssprachlich als 'schlechtes' Cholesterin bezeichnet, da es "
            "Cholesterin zu den Koerperzellen transportiert und bei erhoehten Werten zu "
            "Ablagerungen in Gefaesswaenden beitragen kann."
        ),
        "high_meaning": (
            "Erhoehte Werte gelten als Risikofaktor fuer Arteriosklerose und "
            "Herz-Kreislauf-Erkrankungen. Der individuelle Zielwert haengt vom "
            "Gesamtrisiko ab und sollte aerztlich eingeordnet werden."
        ),
        "low_meaning": "Niedrige Werte gelten allgemein als guenstig.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 130},
        ],
    },
    {
        "code": "hdl",
        "name": "HDL-Cholesterin",
        "full_name": "High Density Lipoprotein Cholesterin",
        "unit": "mg/dl",
        "category": "Blutfette",
        "description": (
            "Wird umgangssprachlich als 'gutes' Cholesterin bezeichnet, da es "
            "Cholesterin aus dem Gewebe zurueck zur Leber transportiert."
        ),
        "high_meaning": "Hohe Werte gelten allgemein als guenstig.",
        "low_meaning": (
            "Niedrige Werte gelten als Risikofaktor fuer Herz-Kreislauf-Erkrankungen und "
            "koennen z. B. durch Bewegungsmangel oder Rauchen beguenstigt werden."
        ),
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 40, "high": 999},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 50, "high": 999},
        ],
    },
    {
        "code": "triglyceride",
        "name": "Triglyceride",
        "full_name": "Triglyceride",
        "unit": "mg/dl",
        "category": "Blutfette",
        "description": "Neutralfette, die als Energiespeicher dienen und stark von der Ernaehrung beeinflusst werden.",
        "high_meaning": (
            "Erhoehte Werte koennen durch Ernaehrung (Zucker, Alkohol, Fett), Uebergewicht "
            "oder Stoffwechselerkrankungen bedingt sein und gelten als Risikofaktor fuer "
            "Herz-Kreislauf-Erkrankungen."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 150},
        ],
    },
    # ---------------- Blutzucker ----------------
    {
        "code": "glukose",
        "name": "Glukose (nuechtern)",
        "full_name": "Nuechternblutzucker",
        "unit": "mg/dl",
        "category": "Blutzucker",
        "description": "Der Blutzuckerwert, gemessen nach mindestens 8 Stunden ohne Nahrungsaufnahme.",
        "high_meaning": (
            "Erhoehte Nuechternwerte koennen auf eine gestoerte Glukosetoleranz oder "
            "einen Diabetes mellitus hinweisen."
        ),
        "low_meaning": "Niedrige Werte koennen auf eine Unterzuckerung (Hypoglykaemie) hinweisen.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 70, "high": 99},
        ],
    },
    {
        "code": "hba1c",
        "name": "HbA1c",
        "full_name": "Glykiertes Haemoglobin",
        "unit": "%",
        "category": "Blutzucker",
        "description": (
            "Zeigt den durchschnittlichen Blutzuckerspiegel der letzten 2-3 Monate an, "
            "da sich Zucker dauerhaft an das Haemoglobin bindet."
        ),
        "high_meaning": (
            "Erhoehte Werte deuten auf laengerfristig erhoehte Blutzuckerwerte hin und "
            "werden zur Diagnose und Verlaufskontrolle bei Diabetes verwendet."
        ),
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 4.0, "high": 5.6},
        ],
    },
    # ---------------- Schilddruese ----------------
    {
        "code": "tsh",
        "name": "TSH",
        "full_name": "Thyreoidea-stimulierendes Hormon",
        "unit": "mU/l",
        "category": "Schilddruese",
        "description": (
            "Ein in der Hirnanhangsdruese gebildetes Hormon, das die Schilddruese zur "
            "Produktion von Schilddruesenhormonen anregt. Gilt als wichtigster erster "
            "Suchparameter fuer Schilddruesenfunktionsstoerungen."
        ),
        "high_meaning": "Erhoehte Werte koennen auf eine Schilddruesenunterfunktion hinweisen.",
        "low_meaning": "Niedrige Werte koennen auf eine Schilddruesenueberfunktion hinweisen.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0.4, "high": 4.0},
        ],
    },
    {
        "code": "ft3",
        "name": "fT3",
        "full_name": "freies Trijodthyronin",
        "unit": "pg/ml",
        "category": "Schilddruese",
        "description": "Das aktive Schilddruesenhormon in seiner freien, ungebundenen Form.",
        "high_meaning": "Erhoehte Werte koennen auf eine Schilddruesenueberfunktion hinweisen.",
        "low_meaning": "Niedrige Werte koennen auf eine Schilddruesenunterfunktion hinweisen.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 2.0, "high": 4.4},
        ],
    },
    {
        "code": "ft4",
        "name": "fT4",
        "full_name": "freies Thyroxin",
        "unit": "ng/dl",
        "category": "Schilddruese",
        "description": "Das Speicherhormon der Schilddruese in seiner freien, ungebundenen Form.",
        "high_meaning": "Erhoehte Werte koennen auf eine Schilddruesenueberfunktion hinweisen.",
        "low_meaning": "Niedrige Werte koennen auf eine Schilddruesenunterfunktion hinweisen.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0.8, "high": 1.8},
        ],
    },
    # ---------------- Blutbild ----------------
    {
        "code": "haemoglobin",
        "name": "Haemoglobin",
        "full_name": "Haemoglobin (Hb)",
        "unit": "g/dl",
        "category": "Blutbild",
        "description": "Der rote Blutfarbstoff, der Sauerstoff in den roten Blutkoerperchen transportiert.",
        "high_meaning": "Erhoehte Werte koennen z. B. durch Fluessigkeitsmangel oder in grosser Hoehe auftreten.",
        "low_meaning": "Niedrige Werte deuten auf eine Blutarmut (Anaemie) hin, z. B. durch Eisenmangel.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 14.0, "high": 17.5},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 12.3, "high": 15.3},
        ],
    },
    {
        "code": "haematokrit",
        "name": "Haematokrit",
        "full_name": "Haematokrit (Hkt)",
        "unit": "%",
        "category": "Blutbild",
        "description": "Der Anteil der roten Blutkoerperchen am Gesamtblutvolumen.",
        "high_meaning": "Erhoehte Werte koennen durch Fluessigkeitsmangel oder vermehrte Blutbildung bedingt sein.",
        "low_meaning": "Niedrige Werte koennen auf eine Blutarmut hinweisen.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 40, "high": 52},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 36, "high": 46},
        ],
    },
    {
        "code": "erythrozyten",
        "name": "Erythrozyten",
        "full_name": "Rote Blutkoerperchen",
        "unit": "Mio/µl",
        "category": "Blutbild",
        "description": "Die Anzahl der roten Blutkoerperchen, die Sauerstoff im Koerper transportieren.",
        "high_meaning": "Erhoehte Werte koennen z. B. durch Fluessigkeitsmangel oder in grosser Hoehe auftreten.",
        "low_meaning": "Niedrige Werte koennen auf eine Blutarmut hinweisen.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 4.5, "high": 5.9},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 4.0, "high": 5.2},
        ],
    },
    {
        "code": "leukozyten",
        "name": "Leukozyten",
        "full_name": "Weisse Blutkoerperchen",
        "unit": "/nl",
        "category": "Blutbild",
        "description": "Zellen des Immunsystems, die der Abwehr von Infektionen dienen.",
        "high_meaning": (
            "Erhoehte Werte koennen auf Infektionen, Entzuendungen oder in seltenen "
            "Faellen auf Erkrankungen des Blutsystems hinweisen."
        ),
        "low_meaning": "Niedrige Werte koennen auf eine geschwaechte Immunabwehr hinweisen.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 4.0, "high": 10.0},
        ],
    },
    {
        "code": "thrombozyten",
        "name": "Thrombozyten",
        "full_name": "Blutplaettchen",
        "unit": "/nl",
        "category": "Blutbild",
        "description": "Zellfragmente, die fuer die Blutgerinnung wichtig sind.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Entzuendungen oder nach Blutverlust auftreten.",
        "low_meaning": (
            "Niedrige Werte koennen die Blutgerinnung beeintraechtigen und sollten "
            "abgeklaert werden."
        ),
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 150, "high": 400},
        ],
    },
    {
        "code": "mcv",
        "name": "MCV",
        "full_name": "Mittleres corpuskulaeres Volumen",
        "unit": "fl",
        "category": "Blutbild",
        "description": "Das durchschnittliche Volumen eines einzelnen roten Blutkoerperchens.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Vitamin-B12- oder Folsaeuremangel auftreten.",
        "low_meaning": "Niedrige Werte koennen auf Eisenmangel hinweisen.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 80, "high": 96},
        ],
    },
    # ---------------- Entzuendung ----------------
    {
        "code": "crp",
        "name": "CRP",
        "full_name": "C-reaktives Protein",
        "unit": "mg/l",
        "category": "Entzuendung",
        "description": "Ein Eiweiss, dessen Konzentration bei Entzuendungen im Koerper rasch ansteigt.",
        "high_meaning": (
            "Erhoehte Werte deuten auf eine akute Entzuendung, Infektion oder Gewebeschaedigung hin."
        ),
        "low_meaning": "Niedrige Werte sind der Normalfall.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 5},
        ],
    },
    # ---------------- Elektrolyte ----------------
    {
        "code": "natrium",
        "name": "Natrium",
        "full_name": "Natrium",
        "unit": "mmol/l",
        "category": "Elektrolyte",
        "description": "Ein wichtiges Elektrolyt fuer den Fluessigkeitshaushalt und die Nervenfunktion.",
        "high_meaning": "Erhoehte Werte koennen auf Fluessigkeitsmangel hinweisen.",
        "low_meaning": "Niedrige Werte koennen z. B. bei starkem Schwitzen, Erbrechen oder bestimmten Medikamenten auftreten.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 135, "high": 145},
        ],
    },
    {
        "code": "kalium",
        "name": "Kalium",
        "full_name": "Kalium",
        "unit": "mmol/l",
        "category": "Elektrolyte",
        "description": "Ein wichtiges Elektrolyt fuer die Funktion von Muskel- und Nervenzellen, insbesondere des Herzens.",
        "high_meaning": "Erhoehte Werte koennen die Herzfunktion beeintraechtigen und sollten abgeklaert werden.",
        "low_meaning": "Niedrige Werte koennen z. B. bei starkem Erbrechen, Durchfall oder bestimmten Medikamenten auftreten.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 3.6, "high": 5.2},
        ],
    },
    {
        "code": "calcium",
        "name": "Calcium",
        "full_name": "Calcium",
        "unit": "mmol/l",
        "category": "Elektrolyte",
        "description": "Ein Mineralstoff, der u. a. fuer Knochen, Muskel- und Nervenfunktion wichtig ist.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Ueberfunktion der Nebenschilddruese auftreten.",
        "low_meaning": "Niedrige Werte koennen z. B. bei Vitamin-D-Mangel auftreten.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 2.2, "high": 2.6},
        ],
    },
    # ---------------- Eisenhaushalt ----------------
    {
        "code": "eisen",
        "name": "Eisen",
        "full_name": "Serumeisen",
        "unit": "µg/dl",
        "category": "Eisenhaushalt",
        "description": "Die Menge an Eisen, die aktuell im Blutserum zirkuliert. Schwankt stark tageszeitlich.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Eisenueberladung auftreten.",
        "low_meaning": "Niedrige Werte koennen auf einen Eisenmangel hinweisen.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 60, "high": 180},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 40, "high": 160},
        ],
    },
    {
        "code": "ferritin",
        "name": "Ferritin",
        "full_name": "Ferritin",
        "unit": "ng/ml",
        "category": "Eisenhaushalt",
        "description": (
            "Das wichtigste Eisenspeicherprotein im Koerper und ein zuverlaessigerer "
            "Marker fuer die Eisenspeicher als das Serumeisen."
        ),
        "high_meaning": (
            "Erhoehte Werte koennen auf Eisenueberladung hinweisen, steigen aber auch "
            "bei Entzuendungen unspezifisch an."
        ),
        "low_meaning": "Niedrige Werte sprechen fuer leere Eisenspeicher (Eisenmangel).",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 30, "high": 400},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 15, "high": 150},
        ],
    },
    # ---------------- Vitamine ----------------
    {
        "code": "vitamin_d",
        "name": "Vitamin D",
        "full_name": "25-Hydroxy-Vitamin D",
        "unit": "ng/ml",
        "category": "Vitamine",
        "description": "Die Speicherform von Vitamin D im Blut, wichtig fuer Knochen und Immunsystem.",
        "high_meaning": "Sehr hohe Werte sind selten und meist auf eine Ueberdosierung durch Praeparate zurueckzufuehren.",
        "low_meaning": (
            "Niedrige Werte sind vor allem im Winterhalbjahr in Mitteleuropa haeufig, "
            "da die koerpereigene Bildung von der Sonnenbestrahlung abhaengt."
        ),
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 30, "high": 100},
        ],
    },
    {
        "code": "vitamin_b12",
        "name": "Vitamin B12",
        "full_name": "Cobalamin",
        "unit": "pg/ml",
        "category": "Vitamine",
        "description": "Ein Vitamin, das fuer die Blutbildung und das Nervensystem wichtig ist.",
        "high_meaning": "Erhoehte Werte sind meist unauffaellig, oft durch Nahrungsergaenzung bedingt.",
        "low_meaning": (
            "Niedrige Werte koennen auf einen Mangel hinweisen, z. B. bei veganer/vegetarischer "
            "Ernaehrung oder Aufnahmestoerungen."
        ),
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 200, "high": 900},
        ],
    },
    {
        "code": "folsaeure",
        "name": "Folsaeure",
        "full_name": "Folsaeure (Vitamin B9)",
        "unit": "ng/ml",
        "category": "Vitamine",
        "description": "Ein B-Vitamin, das u. a. fuer die Zellteilung und Blutbildung wichtig ist.",
        "high_meaning": "Erhoehte Werte sind meist unauffaellig.",
        "low_meaning": "Niedrige Werte koennen auf einen Mangel hinweisen, z. B. durch einseitige Ernaehrung.",
        "ranges": [
            {"gender": "all", "min_age": 0, "max_age": 200, "low": 3.0, "high": 20.0},
        ],
    },
    {
        "code": "vitamin_a",
        "name": "Vitamin A",
        "full_name": "Retinol",
        "unit": "µg/dl",
        "category": "Vitamine",
        "description": "Ein fettloesliches Vitamin, wichtig u. a. fuer Sehvermoegen, Haut und Immunsystem.",
        "high_meaning": "Erhoehte Werte koennen bei ueberhoehter Zufuhr ueber Praeparate auftreten.",
        "low_meaning": "Niedrige Werte koennen z. B. bei Fettverdauungsstoerungen auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 30, "high": 65}],
    },
    {
        "code": "vitamin_e",
        "name": "Vitamin E",
        "full_name": "Alpha-Tocopherol",
        "unit": "mg/l",
        "category": "Vitamine",
        "description": "Ein fettloesliches Vitamin mit antioxidativer Funktion.",
        "high_meaning": "Erhoehte Werte sind meist unauffaellig.",
        "low_meaning": "Niedrige Werte koennen z. B. bei Fettverdauungsstoerungen auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 5.5, "high": 17.0}],
    },
    {
        "code": "vitamin_b6",
        "name": "Vitamin B6",
        "full_name": "Pyridoxalphosphat",
        "unit": "µg/l",
        "category": "Vitamine",
        "description": "Ein B-Vitamin, wichtig u. a. fuer den Eiweissstoffwechsel und das Nervensystem.",
        "high_meaning": "Erhoehte Werte sind meist auf Nahrungsergaenzung zurueckzufuehren.",
        "low_meaning": "Niedrige Werte koennen z. B. bei einseitiger Ernaehrung oder bestimmten Medikamenten auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 4.6, "high": 18.6}],
    },
    # ---------------- Spurenelemente ----------------
    {
        "code": "zink",
        "name": "Zink",
        "full_name": "Zink",
        "unit": "µg/dl",
        "category": "Spurenelemente",
        "description": "Ein Spurenelement, wichtig u. a. fuer Immunsystem, Wundheilung und Enzymfunktionen.",
        "high_meaning": "Erhoehte Werte sind meist auf Nahrungsergaenzung zurueckzufuehren.",
        "low_meaning": "Niedrige Werte koennen z. B. bei einseitiger Ernaehrung oder erhoehtem Bedarf auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 70, "high": 120}],
    },
    {
        "code": "selen",
        "name": "Selen",
        "full_name": "Selen",
        "unit": "µg/l",
        "category": "Spurenelemente",
        "description": "Ein Spurenelement mit antioxidativer Funktion, wichtig u. a. fuer die Schilddruese.",
        "high_meaning": "Erhoehte Werte sind meist auf Nahrungsergaenzung zurueckzufuehren.",
        "low_meaning": "Niedrige Werte koennen bei einseitiger Ernaehrung auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 60, "high": 120}],
    },
    {
        "code": "kupfer",
        "name": "Kupfer",
        "full_name": "Kupfer",
        "unit": "µg/dl",
        "category": "Spurenelemente",
        "description": "Ein Spurenelement, wichtig u. a. fuer die Blutbildung und Bindegewebe.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Entzuendungen unspezifisch ansteigen.",
        "low_meaning": "Niedrige Werte koennen bei einseitiger Ernaehrung auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 70, "high": 140}],
    },
    {
        "code": "magnesium",
        "name": "Magnesium",
        "full_name": "Magnesium",
        "unit": "mmol/l",
        "category": "Elektrolyte",
        "description": "Ein Mineralstoff, wichtig u. a. fuer Muskel- und Nervenfunktion sowie den Energiestoffwechsel.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei eingeschraenkter Nierenfunktion auftreten.",
        "low_meaning": "Niedrige Werte koennen z. B. bei Alkoholkonsum, Durchfall oder bestimmten Medikamenten auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.66, "high": 1.07}],
    },
    {
        "code": "phosphat",
        "name": "Phosphat",
        "full_name": "Anorganisches Phosphat",
        "unit": "mmol/l",
        "category": "Elektrolyte",
        "description": "Ein Mineralstoff, wichtig u. a. fuer Knochen und den Energiestoffwechsel.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei eingeschraenkter Nierenfunktion auftreten.",
        "low_meaning": "Niedrige Werte koennen z. B. bei Mangelernaehrung auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.87, "high": 1.45}],
    },
    {
        "code": "chlorid",
        "name": "Chlorid",
        "full_name": "Chlorid",
        "unit": "mmol/l",
        "category": "Elektrolyte",
        "description": "Ein Elektrolyt, das eng mit dem Natriumhaushalt und dem Saeure-Basen-Gleichgewicht zusammenhaengt.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Fluessigkeitsmangel auftreten.",
        "low_meaning": "Niedrige Werte koennen z. B. bei starkem Erbrechen auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 98, "high": 107}],
    },
    # ---------------- Leber (weitere) ----------------
    {
        "code": "ap",
        "name": "Alkalische Phosphatase",
        "full_name": "Alkalische Phosphatase (AP)",
        "unit": "U/l",
        "category": "Leber",
        "description": "Ein Enzym, das in Leber, Galle und Knochen vorkommt.",
        "high_meaning": "Erhoehte Werte koennen auf Gallenwegs-, Leber- oder Knochenerkrankungen hinweisen.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 40, "high": 130},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 35, "high": 105},
        ],
    },
    {
        "code": "che",
        "name": "Cholinesterase",
        "full_name": "Cholinesterase (CHE)",
        "unit": "kU/l",
        "category": "Leber",
        "description": "Ein von der Leber gebildetes Enzym, das Rueckschluesse auf die Syntheseleistung der Leber zulaesst.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Fettleber auftreten.",
        "low_meaning": "Niedrige Werte koennen auf eine eingeschraenkte Leberfunktion hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 4.6, "high": 11.5}],
    },
    {
        "code": "ldh",
        "name": "LDH",
        "full_name": "Laktatdehydrogenase",
        "unit": "U/l",
        "category": "Sonstiges",
        "description": "Ein Enzym, das in vielen Geweben vorkommt und bei Zellschaeden allgemein ansteigt.",
        "high_meaning": (
            "Erhoehte Werte sind unspezifisch und koennen z. B. bei Leber-, Muskel- oder "
            "Blutzellschaeden auftreten."
        ),
        "low_meaning": "Niedrige Werte haben in der Regel keine klinische Bedeutung.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 120, "high": 246}],
    },
    # ---------------- Niere (weitere) ----------------
    {
        "code": "cystatin_c",
        "name": "Cystatin C",
        "full_name": "Cystatin C",
        "unit": "mg/l",
        "category": "Niere",
        "description": "Ein von Kreatinin unabhaengiger Marker der Nierenfunktion, weniger von der Muskelmasse beeinflusst.",
        "high_meaning": "Erhoehte Werte koennen auf eine eingeschraenkte Nierenfunktion hinweisen.",
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.5, "high": 0.96}],
    },
    # ---------------- Muskel / Herz ----------------
    {
        "code": "ck",
        "name": "CK",
        "full_name": "Kreatinkinase",
        "unit": "U/l",
        "category": "Muskel & Herz",
        "description": "Ein Enzym aus Muskel-, Herz- und Hirngewebe, das bei Zellschaeden ansteigt.",
        "high_meaning": "Erhoehte Werte koennen z. B. nach intensivem Sport, Muskelverletzungen oder Herzinfarkt auftreten.",
        "low_meaning": "Niedrige Werte haben keine klinische Bedeutung.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 30, "high": 200},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 30, "high": 170},
        ],
    },
    {
        "code": "troponin",
        "name": "Troponin",
        "full_name": "Troponin (hs-cTnT)",
        "unit": "ng/l",
        "category": "Muskel & Herz",
        "description": "Ein hochspezifischer Marker fuer Schaeden am Herzmuskel.",
        "high_meaning": (
            "Erhoehte Werte deuten auf eine Schaedigung des Herzmuskels hin und sollten "
            "immer zeitnah aerztlich abgeklaert werden."
        ),
        "low_meaning": "Niedrige Werte sind der Normalfall.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 14}],
    },
    {
        "code": "homocystein",
        "name": "Homocystein",
        "full_name": "Homocystein",
        "unit": "µmol/l",
        "category": "Muskel & Herz",
        "description": "Eine Aminosaeure, deren erhoehte Werte als Risikofaktor fuer Gefaesserkrankungen gelten.",
        "high_meaning": (
            "Erhoehte Werte koennen z. B. bei Vitamin-B12- oder Folsaeuremangel auftreten und "
            "gelten als Risikofaktor fuer Herz-Kreislauf-Erkrankungen."
        ),
        "low_meaning": "Niedrige Werte sind unauffaellig.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 15}],
    },
    # ---------------- Pankreas ----------------
    {
        "code": "lipase",
        "name": "Lipase",
        "full_name": "Lipase",
        "unit": "U/l",
        "category": "Pankreas",
        "description": "Ein Verdauungsenzym der Bauchspeicheldruese.",
        "high_meaning": "Erhoehte Werte koennen auf eine Entzuendung der Bauchspeicheldruese hinweisen.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 13, "high": 60}],
    },
    {
        "code": "amylase",
        "name": "Amylase",
        "full_name": "Alpha-Amylase",
        "unit": "U/l",
        "category": "Pankreas",
        "description": "Ein Verdauungsenzym aus Bauchspeicheldruese und Speicheldruesen.",
        "high_meaning": "Erhoehte Werte koennen auf eine Entzuendung der Bauchspeicheldruese hinweisen.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 28, "high": 100}],
    },
    # ---------------- Gerinnung ----------------
    {
        "code": "quick",
        "name": "Quick-Wert",
        "full_name": "Thromboplastinzeit (Quick)",
        "unit": "%",
        "category": "Gerinnung",
        "description": "Ein Mass fuer die Blutgerinnung ueber den sogenannten extrinsischen Weg.",
        "high_meaning": "Hohe Werte sind unauffaellig.",
        "low_meaning": (
            "Niedrige Werte deuten auf eine verlangsamte Blutgerinnung hin, z. B. durch "
            "Lebererkrankungen, Vitamin-K-Mangel oder gerinnungshemmende Medikamente."
        ),
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 70, "high": 130}],
    },
    {
        "code": "inr",
        "name": "INR",
        "full_name": "International Normalized Ratio",
        "unit": "",
        "category": "Gerinnung",
        "description": "Standardisierte Kennzahl der Blutgerinnung, u. a. zur Ueberwachung von Blutverduennern.",
        "high_meaning": "Erhoehte Werte deuten auf eine verlangsamte Blutgerinnung hin.",
        "low_meaning": "Niedrige Werte sind in der Regel unauffaellig.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.8, "high": 1.2}],
    },
    {
        "code": "ptt",
        "name": "aPTT",
        "full_name": "Aktivierte partielle Thromboplastinzeit",
        "unit": "sec",
        "category": "Gerinnung",
        "description": "Ein Mass fuer die Blutgerinnung ueber den sogenannten intrinsischen Weg.",
        "high_meaning": "Erhoehte Werte deuten auf eine verlangsamte Blutgerinnung hin.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 25, "high": 38}],
    },
    {
        "code": "fibrinogen",
        "name": "Fibrinogen",
        "full_name": "Fibrinogen",
        "unit": "mg/dl",
        "category": "Gerinnung",
        "description": "Ein Gerinnungsfaktor, der auch als Entzuendungsmarker ansteigen kann.",
        "high_meaning": "Erhoehte Werte koennen bei Entzuendungen oder erhoehtem Gerinnungsrisiko auftreten.",
        "low_meaning": "Niedrige Werte koennen die Blutgerinnung beeintraechtigen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 180, "high": 350}],
    },
    # ---------------- Entzuendung / Immunsystem (weitere) ----------------
    {
        "code": "bsg",
        "name": "BSG",
        "full_name": "Blutsenkungsgeschwindigkeit",
        "unit": "mm/h",
        "category": "Entzuendung",
        "description": "Ein unspezifischer, traditioneller Marker fuer Entzuendungsprozesse im Koerper.",
        "high_meaning": "Erhoehte Werte koennen auf Entzuendungen, Infektionen oder andere Erkrankungen hinweisen.",
        "low_meaning": "Niedrige Werte sind der Normalfall.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 0, "high": 15},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 0, "high": 20},
        ],
    },
    {
        "code": "procalcitonin",
        "name": "Procalcitonin",
        "full_name": "Procalcitonin (PCT)",
        "unit": "ng/ml",
        "category": "Entzuendung",
        "description": "Ein Marker, der besonders bei bakteriellen Infektionen ansteigt.",
        "high_meaning": "Erhoehte Werte koennen auf eine bakterielle Infektion hinweisen.",
        "low_meaning": "Niedrige Werte sind der Normalfall.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0, "high": 0.05}],
    },
    {
        "code": "igg",
        "name": "IgG",
        "full_name": "Immunglobulin G",
        "unit": "g/l",
        "category": "Immunsystem",
        "description": "Die haeufigste Antikoerperklasse, wichtig fuer die langfristige Immunabwehr.",
        "high_meaning": "Erhoehte Werte koennen bei chronischen Entzuendungen oder Infektionen auftreten.",
        "low_meaning": "Niedrige Werte koennen auf eine Abwehrschwaeche hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 7.0, "high": 16.0}],
    },
    {
        "code": "iga",
        "name": "IgA",
        "full_name": "Immunglobulin A",
        "unit": "g/l",
        "category": "Immunsystem",
        "description": "Eine Antikoerperklasse, die besonders auf Schleimhaeuten aktiv ist.",
        "high_meaning": "Erhoehte Werte koennen bei chronischen Entzuendungen auftreten.",
        "low_meaning": "Niedrige Werte koennen auf einen angeborenen Mangel hinweisen (haeufig, oft ohne Beschwerden).",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.7, "high": 4.0}],
    },
    {
        "code": "igm",
        "name": "IgM",
        "full_name": "Immunglobulin M",
        "unit": "g/l",
        "category": "Immunsystem",
        "description": "Die Antikoerperklasse, die bei einer akuten Immunantwort zuerst gebildet wird.",
        "high_meaning": "Erhoehte Werte koennen auf eine akute Infektion hinweisen.",
        "low_meaning": "Niedrige Werte koennen auf eine Abwehrschwaeche hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.4, "high": 2.3}],
    },
    # ---------------- Hormone ----------------
    {
        "code": "testosteron",
        "name": "Testosteron",
        "full_name": "Testosteron gesamt",
        "unit": "ng/dl",
        "category": "Hormone",
        "description": "Das wichtigste maennliche Geschlechtshormon, wird aber auch bei Frauen in geringer Menge gebildet.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei bestimmten hormonellen Stoerungen auftreten.",
        "low_meaning": (
            "Niedrige Werte koennen u. a. Muedigkeit, verminderte Libido oder Muskelabbau "
            "begleiten und sollten aerztlich eingeordnet werden."
        ),
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 264, "high": 916},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 8, "high": 60},
        ],
    },
    {
        "code": "shbg",
        "name": "SHBG",
        "full_name": "Sexualhormon-bindendes Globulin",
        "unit": "nmol/l",
        "category": "Hormone",
        "description": "Ein Transportprotein, das die Menge an frei verfuegbarem Testosteron/Oestrogen im Blut beeinflusst.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Schilddruesenueberfunktion auftreten.",
        "low_meaning": "Niedrige Werte koennen z. B. bei Uebergewicht auftreten.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 10, "high": 57},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 18, "high": 114},
        ],
    },
    {
        "code": "cortisol",
        "name": "Cortisol",
        "full_name": "Cortisol (morgens)",
        "unit": "µg/dl",
        "category": "Hormone",
        "description": "Das wichtigste Stresshormon der Nebennierenrinde, folgt einem Tagesrhythmus (morgens am hoechsten).",
        "high_meaning": "Erhoehte Werte koennen u. a. bei Stress oder Nebennierenerkrankungen auftreten.",
        "low_meaning": "Niedrige Werte koennen auf eine Nebenniereninsuffizienz hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 6.2, "high": 19.4}],
    },
    {
        "code": "prolaktin",
        "name": "Prolaktin",
        "full_name": "Prolaktin",
        "unit": "ng/ml",
        "category": "Hormone",
        "description": "Ein Hormon der Hirnanhangsdruese, u. a. bekannt fuer seine Rolle beim Stillen.",
        "high_meaning": "Erhoehte Werte koennen z. B. durch Stress, Medikamente oder einen Hypophysentumor bedingt sein.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [
            {"gender": "m", "min_age": 0, "max_age": 200, "low": 2.5, "high": 17},
            {"gender": "f", "min_age": 0, "max_age": 200, "low": 2.8, "high": 29.2},
        ],
    },
    {
        "code": "insulin",
        "name": "Insulin",
        "full_name": "Insulin (nuechtern)",
        "unit": "µU/ml",
        "category": "Hormone",
        "description": "Ein Hormon der Bauchspeicheldruese, das den Blutzucker senkt.",
        "high_meaning": "Erhoehte Nuechternwerte koennen auf eine Insulinresistenz hinweisen.",
        "low_meaning": "Niedrige Werte koennen bei Insulinmangel auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 2.6, "high": 24.9}],
    },
    # ---------------- Blutbild: Differenzialblutbild ----------------
    {
        "code": "mch",
        "name": "MCH",
        "full_name": "Mittleres corpuskulaeres Haemoglobin",
        "unit": "pg",
        "category": "Blutbild",
        "description": "Die durchschnittliche Haemoglobinmenge pro rotem Blutkoerperchen.",
        "high_meaning": "Erhoehte Werte koennen z. B. bei Vitamin-B12-Mangel auftreten.",
        "low_meaning": "Niedrige Werte koennen auf Eisenmangel hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 27, "high": 33}],
    },
    {
        "code": "mchc",
        "name": "MCHC",
        "full_name": "Mittlere corpuskulaere Haemoglobinkonzentration",
        "unit": "g/dl",
        "category": "Blutbild",
        "description": "Die Haemoglobinkonzentration bezogen auf das Volumen der roten Blutkoerperchen.",
        "high_meaning": "Erhoehte Werte sind selten und meist messtechnisch bedingt.",
        "low_meaning": "Niedrige Werte koennen auf Eisenmangel hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 32, "high": 36}],
    },
    {
        "code": "retikulozyten",
        "name": "Retikulozyten",
        "full_name": "Retikulozyten",
        "unit": "%",
        "category": "Blutbild",
        "description": "Unreife rote Blutkoerperchen, ein Mass fuer die Aktivitaet der Blutbildung im Knochenmark.",
        "high_meaning": "Erhoehte Werte deuten auf eine gesteigerte Blutbildung hin, z. B. nach Blutverlust.",
        "low_meaning": "Niedrige Werte koennen auf eine eingeschraenkte Blutbildung hinweisen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 0.5, "high": 2.0}],
    },
    {
        "code": "neutrophile",
        "name": "Neutrophile",
        "full_name": "Neutrophile Granulozyten",
        "unit": "%",
        "category": "Blutbild",
        "description": "Die haeufigste Untergruppe der weissen Blutkoerperchen, wichtig bei der Abwehr bakterieller Infektionen.",
        "high_meaning": "Erhoehte Werte koennen bei bakteriellen Infektionen oder Stress auftreten.",
        "low_meaning": "Niedrige Werte koennen die Infektabwehr beeintraechtigen.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 40, "high": 75}],
    },
    {
        "code": "lymphozyten",
        "name": "Lymphozyten",
        "full_name": "Lymphozyten",
        "unit": "%",
        "category": "Blutbild",
        "description": "Weisse Blutkoerperchen, die u. a. fuer die spezifische Immunabwehr wichtig sind.",
        "high_meaning": "Erhoehte Werte koennen bei viralen Infektionen auftreten.",
        "low_meaning": "Niedrige Werte koennen bei Stress, Infektionen oder Immunschwaeche auftreten.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 20, "high": 45}],
    },
    {
        "code": "monozyten",
        "name": "Monozyten",
        "full_name": "Monozyten",
        "unit": "%",
        "category": "Blutbild",
        "description": "Weisse Blutkoerperchen, die u. a. Krankheitserreger und Zelltruemmer beseitigen.",
        "high_meaning": "Erhoehte Werte koennen bei chronischen Entzuendungen oder Infektionen auftreten.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 2, "high": 10}],
    },
    {
        "code": "eosinophile",
        "name": "Eosinophile",
        "full_name": "Eosinophile Granulozyten",
        "unit": "%",
        "category": "Blutbild",
        "description": "Weisse Blutkoerperchen, die u. a. bei Allergien und Parasitenbefall eine Rolle spielen.",
        "high_meaning": "Erhoehte Werte koennen bei Allergien, Asthma oder Parasitenbefall auftreten.",
        "low_meaning": "Niedrige Werte haben selten klinische Bedeutung.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 1, "high": 4}],
    },
    # ---------------- Koerpermasse ----------------
    {
        "code": "groesse",
        "name": "Größe",
        "full_name": "Körpergröße",
        "unit": "cm",
        "category": "Körpermaße",
        "description": "Deine Körpergröße, wird zusammen mit dem Gewicht zur automatischen BMI-Berechnung genutzt.",
        "high_meaning": "",
        "low_meaning": "",
        "ranges": [],
    },
    {
        "code": "gewicht",
        "name": "Gewicht",
        "full_name": "Körpergewicht",
        "unit": "kg",
        "category": "Körpermaße",
        "description": "Dein Körpergewicht, wird zusammen mit der Größe zur automatischen BMI-Berechnung genutzt.",
        "high_meaning": "",
        "low_meaning": "",
        "ranges": [],
    },
    {
        "code": "bmi",
        "name": "BMI",
        "full_name": "Body-Mass-Index",
        "unit": "kg/m²",
        "category": "Körpermaße",
        "description": (
            "Ein aus Größe und Gewicht berechneter Richtwert. Wird automatisch berechnet, "
            "sobald du in einem Eintrag beides gleichzeitig eintraegst."
        ),
        "high_meaning": "Werte ueber 25 gelten allgemein als Uebergewicht, ueber 30 als Adipositas.",
        "low_meaning": "Werte unter 18,5 gelten allgemein als Untergewicht.",
        "ranges": [{"gender": "all", "min_age": 0, "max_age": 200, "low": 18.5, "high": 24.9}],
        "computed": True,
    },
]

PARAMETERS_BY_CODE = {p["code"]: p for p in PARAMETERS}


def resolve_range(parameter_code: str, age_years: int | None, gender: str | None):
    """Return the best-matching {low, high} reference range for a parameter,
    given the user's age (in years) and gender ('m' / 'f' / None)."""
    param = PARAMETERS_BY_CODE.get(parameter_code)
    if not param:
        return None

    candidates = param["ranges"]
    best = None
    for r in candidates:
        if r["gender"] != "all" and gender and r["gender"] != gender:
            continue
        if age_years is not None and not (r["min_age"] <= age_years <= r["max_age"]):
            continue
        # Prefer a range that explicitly matches gender over a generic "all" one
        if best is None or (r["gender"] != "all" and best["gender"] == "all"):
            best = r
    if best is None and candidates:
        best = candidates[0]
    return {"low": best["low"], "high": best["high"]} if best else None
