import random

class Unternehmen:
    def __init__(self, name : str):
        self.name = name
        self.abteilungen = [] # list[Abteilung]
    
    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    def abteilung_entfernen(self, abteilung):
        self.abteilungen.remove(abteilung)

    def abteilung_finden(self, bezeichnung):
        for abteilung in self.abteilungen:
            if abteilung.bezeichnung == bezeichnung:
                return abteilung

    def alle_mitarbeiter_anzeigen(self):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"{mitarbeiter.personalnummer}: {mitarbeiter.name}")

    def mitarbeiter_suchen(self, personalnummer):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter
                
    def info(self):
        print(f"{self.name}")
        for abteilung in self.abteilungen:
            print(f"    {abteilung.bezeichnung}")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"        {mitarbeiter.personalnummer}: {mitarbeiter.name}")


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

# Abteilung suchen
gesuchte_abteilung = "Vertrieb"
if unternehmen.abteilung_finden(gesuchte_abteilung):
    print(f"Abteilung {gesuchte_abteilung} gefunden")
else:
    print(f"Abteilung {gesuchte_abteilung} nicht gefunden")

# Alle Mitarbeiter anzeigen
unternehmen.alle_mitarbeiter_anzeigen()

# Einen Mitarbeiter suchen
personalnummer = "001"
mitarbeiter = unternehmen.mitarbeiter_suchen(personalnummer)
if mitarbeiter:
    print(f"Mitarbeiter gefunden:")
    print(f"Personalnummer: {personalnummer}")
    print(f"Name: {mitarbeiter.name}")
else:
    print(f"Mitarbeiter mit Nummer {personalnummer} nicht gefunden")

# Unternehmensinfo ausgeben
unternehmen.info()