# Aufgabe 1_Unternehmen

# -------- KLASSE MITARBEITER --------

class Mitarbeiter:

    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name


# -------- KLASSE ABTEILUNG --------

class Abteilung:

    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = []


    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)


    def mitarbeiter_entfernen(self, mitarbeiter):
        if mitarbeiter in self.mitarbeiter:
            self.mitarbeiter.remove(mitarbeiter)


# -------- KLASSE UNTERNEHMEN --------

class Unternehmen:

    def __init__(self, name):
        self.name = name
        self.abteilungen = []


    def abteilung_hinzufuegen(self, abteilung):
        self.abteilungen.append(abteilung)


    def abteilung_entfernen(self, abteilung):
        if abteilung in self.abteilungen:
            self.abteilungen.remove(abteilung)

# -------- TEST --------

firma = Unternehmen("Tech GmbH")

it = Abteilung("IT")
hr = Abteilung("HR")

firma.abteilung_hinzufuegen(it)
firma.abteilung_hinzufuegen(hr)

m1 = Mitarbeiter(101, "Max")
m2 = Mitarbeiter(102, "Anna")
m3 = Mitarbeiter(103, "Tom")

it.mitarbeiter_hinzufuegen(m1)
it.mitarbeiter_hinzufuegen(m2)

hr.mitarbeiter_hinzufuegen(m3)

print("Unternehmen:", firma.name)

for abteilung in firma.abteilungen:
    print("Abteilung:", abteilung.bezeichnung)

    for mitarbeiter in abteilung.mitarbeiter:
        print("   Mitarbeiter:", mitarbeiter.name)
