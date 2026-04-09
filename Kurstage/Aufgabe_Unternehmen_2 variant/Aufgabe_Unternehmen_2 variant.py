# Aufgabe_UNTERNEHMEN_VAR.2


# Klasse Unternehmen

class Unternehmen:

    def __init__(self, name):
        # Name des Unternehmens
        self.name = name
        # Liste aller Abteilungen
        self.abteilungen = []

    def abteilung_hinzufügen(self, abteilung):
        # Abteilung zum Unternehmen hinzufügen
        self.abteilungen.append(abteilung)

    def abteilung_finden(self, bezeichnung):
        # Abteilung nach Namen suchen
        for abteilung in self.abteilungen:
            if abteilung.bezeichnung == bezeichnung:
                return abteilung
        return None

    def mitarbeiter_suchen(self, personalnummer):
        # Mitarbeiter in allen Abteilungen suchen
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter
        return None

    def info(self):
        # Struktur des Unternehmens ausgeben
        print(self.name)
        for abteilung in self.abteilungen:
            print(f"  {abteilung.bezeichnung}")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"    {mitarbeiter.personalnummer}: {mitarbeiter.name}")



# Klasse Abteilung

class Abteilung:

    def __init__(self, bezeichnung):
        # Name der Abteilung
        self.bezeichnung = bezeichnung
        # Liste der Mitarbeiter
        self.mitarbeiter = []  # list[Mitarbeiter]

    def mitarbeiter_hinzufügen(self, mitarbeiter):

        # aktuelle Abteilung des Mitarbeiters speichern
        abteilung = mitarbeiter.abteilung

        # prüfen ob Mitarbeiter schon in einer Abteilung ist
        if abteilung:
            print("Der Mitarbeiter ist bereits in einer Abteilung")
            print("Mitarbeiter wird verschoben")

            # Mitarbeiter aus alter Abteilung entfernen
            abteilung.mitarbeiter_entfernen(mitarbeiter)

        # Mitarbeiter in neue Abteilung hinzufügen
        self.mitarbeiter.append(mitarbeiter)

        # neue Abteilung beim Mitarbeiter speichern
        mitarbeiter.abteilung = self

    def mitarbeiter_entfernen(self, mitarbeiter):
        # Mitarbeiter aus der Liste entfernen
        self.mitarbeiter.remove(mitarbeiter)



# Klasse Mitarbeiter

class Mitarbeiter:

    def __init__(self, personalnummer, name):
        # Personalnummer des Mitarbeiters
        self.personalnummer = personalnummer
        # Name des Mitarbeiters
        self.name = name
        # Referenz auf die Abteilung
        self.abteilung = None



# Unternehmen erstellen

unternehmen = Unternehmen("Print GmbH")



# Abteilungen erstellen

entwicklung = Abteilung("Entwicklung")
produktion = Abteilung("Produktion")
buchhaltung = Abteilung("Buchhaltung")



# Abteilungen zum Unternehmen hinzufügen

unternehmen.abteilung_hinzufügen(entwicklung)
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

entwicklung.mitarbeiter_hinzufügen(m2)
entwicklung.mitarbeiter_hinzufügen(m7)
entwicklung.mitarbeiter_hinzufügen(m8)

produktion.mitarbeiter_hinzufügen(m3)
produktion.mitarbeiter_hinzufügen(m4)
produktion.mitarbeiter_hinzufügen(m5)

buchhaltung.mitarbeiter_hinzufügen(m1)
buchhaltung.mitarbeiter_hinzufügen(m6)

# Unternehmensstruktur anzeigen

unternehmen.info()