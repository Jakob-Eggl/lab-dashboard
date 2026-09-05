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
