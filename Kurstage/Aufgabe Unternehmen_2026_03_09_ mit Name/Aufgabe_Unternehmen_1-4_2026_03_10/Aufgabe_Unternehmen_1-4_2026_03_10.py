import random
# Klasse Mitarbeiter
class Mitarbeiter:

    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name
        self.abteilung = None


# Klasse Abteilung
class Abteilung:

    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = []

    def mitarbeiter_hinzufügen(self, mitarbeiter):

        if mitarbeiter.abteilung is not None:
            print(f"{mitarbeiter.name} gehört bereits zur Abteilung {mitarbeiter.abteilung.bezeichnung}")
            return

        self.mitarbeiter.append(mitarbeiter)
        mitarbeiter.abteilung = self

# Klasse Unternehmen
class Unternehmen:

    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    def abteilung_finden(self, bezeichnung):
        for abteilung in self.abteilungen:
            if abteilung.bezeichnung == bezeichnung:
                return abteilung
        return None

    def mitarbeiter_suchen(self, personalnummer):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter
        return None

    def info(self):
        print(self.name)
        for abteilung in self.abteilungen:
            print(f"  {abteilung.bezeichnung}")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"    {mitarbeiter.personalnummer}: {mitarbeiter.name}")


# Unternehmen erstellen
unternehmen = Unternehmen("Unternehmen X")


# Abteilungen erstellen
vertrieb = Abteilung("Vertrieb")
produktion = Abteilung("Produktion")
buchhaltung = Abteilung("Buchhaltung")


# Abteilungen zum Unternehmen hinzufügen
unternehmen.abteilung_hinzufügen(vertrieb)
unternehmen.abteilung_hinzufügen(produktion)
unternehmen.abteilung_hinzufügen(buchhaltung)


# Mitarbeiter erstellen
m1 = Mitarbeiter("001", "Tunahan")
m2 = Mitarbeiter("002", "Anne")
m3 = Mitarbeiter("004", "Mohamad")
m4 = Mitarbeiter("006", "Ihor")
m5 = Mitarbeiter("007", "Ruwen")
m6 = Mitarbeiter("008", "Nataliya")
m7 = Mitarbeiter("009", "Andreas")
m8 = Mitarbeiter("010", "Efkan")


# Mitarbeiter zu Abteilungen hinzufügen
vertrieb.mitarbeiter_hinzufügen(m2)
vertrieb.mitarbeiter_hinzufügen(m7)
vertrieb.mitarbeiter_hinzufügen(m8)

produktion.mitarbeiter_hinzufügen(m3)
produktion.mitarbeiter_hinzufügen(m4)
produktion.mitarbeiter_hinzufügen(m5)

buchhaltung.mitarbeiter_hinzufügen(m1)
buchhaltung.mitarbeiter_hinzufügen(m6)


# Unternehmensstruktur anzeigen
unternehmen.info()

