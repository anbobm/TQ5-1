import random


# Klasse Mitarbeiter
class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name


# Klasse Abteilung
class Abteilung:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = []

    # Mitarbeiter zur Abteilung hinzufügen
    def mitarbeiter_hinzufügen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)


# Klasse Unternehmen
class Unternehmen:

    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    # Abteilung zum Unternehmen hinzufügen
    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    # Alle Mitarbeiter anzeigen
    def alle_mitarbeiter_anzeigen(self):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"{mitarbeiter.personalnummer}: {mitarbeiter.name}")

    # Mitarbeiter suchen nach Personalnummer
    def mitarbeiter_suchen(self, personalnummer):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter
        return None

    # Informationen über Unternehmen ausgeben
    def info(self):
        print(self.name)
        for abteilung in self.abteilungen:
            print(f"    {abteilung.bezeichnung}")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"        {mitarbeiter.personalnummer}: {mitarbeiter.name}")

    # Mitarbeiter erzeugen und Abteilung zuweisen
    def mitarbeiter_erzeugen(self, personalnummer, name, abteilung):

        # prüfen ob Personalnummer bereits existiert
        mitarbeiter = self.mitarbeiter_suchen(personalnummer)

        if mitarbeiter:
            print(
                f"Mitarbeiter konnte nicht erzeugt werden: Personalnummer {personalnummer} existiert bereits")
            return None

        # neuen Mitarbeiter erzeugen
        mitarbeiter = Mitarbeiter(personalnummer, name)

        # Mitarbeiter der Abteilung hinzufügen
        abteilung.mitarbeiter_hinzufügen(mitarbeiter)

        return mitarbeiter


# Unternehmen erzeugen
unternehmen = Unternehmen("Print GmbH")

# Abteilungen erzeugen
abteilungen = [
    Abteilung("Entwicklung"),
    Abteilung("Vertrieb"),
    Abteilung("Produktion"),
    Abteilung("Buchhaltung"),
]

# Abteilungen hinzufügen
for abteilung in abteilungen:
    unternehmen.abteilung_hinzufügen(abteilung)

# Mitarbeiter erzeugen
mitarbeiter = [
    unternehmen.mitarbeiter_erzeugen("001", "Tunahan", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("002", "Anne", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("003", "Katja", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("004", "Mohamad", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("005", "Sebastian", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("006", "Ihor", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("007", "Ruwen", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("008", "Nataliya", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("009", "Andreas", random.choice(abteilungen)),
    unternehmen.mitarbeiter_erzeugen("010", "Efkan", random.choice(abteilungen)),

    # Doppelgänger (gleiche Personalnummer)
    unternehmen.mitarbeiter_erzeugen("009", "Max Mustermann", random.choice(abteilungen))
]

# Unternehmensinfo ausgeben
unternehmen.info()

# Mitarbeiter suchen
personalnummer = "001"
mitarbeiter = unternehmen.mitarbeiter_suchen(personalnummer)
if mitarbeiter:
    print("Mitarbeiter gefunden:")
    print(f"Personalnummer: {personalnummer}")
    print(f"Name: {mitarbeiter.name}")
else:
    print(f"Mitarbeiter mit Nummer {personalnummer} nicht gefunden")