import random

class Unternehmen:
    def __init__(self, name : str):
        self.name = name
        self.abteilungen = [] # list[Abteilung]
    
    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    def abteilung_entfernen(self, abteilung):
        self.abteilungen.remove(abteilung)


class Abteilung:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = [] # list[Mitarbeiter]

    def mitarbeiter_hinzufügen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def mitarbeiter_entfernen(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)


class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name


unternehmen = Unternehmen("Print GmbH")

abteilungen = [
    Abteilung("Entwicklung"),
    Abteilung("Vertrieb"),
    Abteilung("Produktion"),
    Abteilung("Buchhaltung"),
]

mitarbeiter = [
    Mitarbeiter("001", "Tunahan"),
    Mitarbeiter("002", "Anne"),
    Mitarbeiter("003", "Katja"),
    Mitarbeiter("004", "Mohamad"),
    Mitarbeiter("005", "Sebastian"),
    Mitarbeiter("006", "Ihor"),
    Mitarbeiter("007", "Ruwen"),
    Mitarbeiter("008", "Nataliya"),
    Mitarbeiter("009", "Andreas"),
    Mitarbeiter("010", "Efkan")
]

# Abteilungen hinzufügen
for abteilung in abteilungen:
    unternehmen.abteilung_hinzufügen(abteilung)

# Mitarbeiter hinzufügen (hier zufällig)
for mitarbeiter in mitarbeiter:
    zufällige_abteilung = random.choice(unternehmen.abteilungen)
    zufällige_abteilung.mitarbeiter_hinzufügen(mitarbeiter)

