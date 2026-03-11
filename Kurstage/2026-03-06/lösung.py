import random

class Unternehmen:
    def __init__(self, name : str):
        self.name = name
        self.abteilungen : list[Abteilung] = [] # list[Abteilung]
    
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

    def mitarbeiter_erzeugen(self, personalnummer, name, abteilung):
        mitarbeiter = self.mitarbeiter_suchen(personalnummer)

        if mitarbeiter:
            print(f"Mitarbeiter konnte nicht erzeugt werden: Personalnummer {personalnummer} existiert bereits")
            return None
        
        mitarbeiter = Mitarbeiter(personalnummer, name)
        abteilung.mitarbeiter_hinzufügen(mitarbeiter)

        return mitarbeiter


class Abteilung:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = [] # list[Mitarbeiter]

    def mitarbeiter_hinzufügen(self, mitarbeiter):
        abteilung = mitarbeiter.abteilung
        if abteilung:
            print(f"Der Mitarbeiter ist bereits Abteilung {abteilung.bezeichnung} zugewiesen.")
            print("Mitarbeiter wird verschoben")
            abteilung.mitarbeiter_entfernen(mitarbeiter)

        mitarbeiter.abteilung = self
        self.mitarbeiter.append(mitarbeiter)

    def mitarbeiter_entfernen(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)


class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name
        self.abteilung = None

# Unternehmensobjekt erzeugen
unternehmen = Unternehmen("Print GmbH")

# Abteilungen erzeugen
entwicklung = Abteilung("Entwicklung")
vertrieb = Abteilung("Vertrieb")
produktion = Abteilung("Produktion")
buchhaltung = Abteilung("Buchhaltung")

abteilungen = [entwicklung, vertrieb, produktion, buchhaltung]

# Abteilungen dem Unternehmen hinzufügen
for abteilung in abteilungen:
    unternehmen.abteilung_hinzufügen(abteilung)

# Mitarbeiter anlegen (und Abteilung zuweisen)
unternehmen.mitarbeiter_erzeugen("001", "Tunahan", entwicklung)
unternehmen.mitarbeiter_erzeugen("002", "Anne", vertrieb)
unternehmen.mitarbeiter_erzeugen("003", "Katja", produktion)
unternehmen.mitarbeiter_erzeugen("004", "Mohamad", produktion)
unternehmen.mitarbeiter_erzeugen("005", "Sebastian", random.choice(abteilungen))
unternehmen.mitarbeiter_erzeugen("006", "Ihor", buchhaltung)
unternehmen.mitarbeiter_erzeugen("007", "Ruwen", vertrieb)
unternehmen.mitarbeiter_erzeugen("008", "Nataliya", entwicklung)
unternehmen.mitarbeiter_erzeugen("009", "Andreas", produktion)
unternehmen.mitarbeiter_erzeugen("010", "Efkan", entwicklung)

# Soll fehlschlagen, da Mitarbeiter mit Nummer 009 bereits existiert
unternehmen.mitarbeiter_erzeugen("009", "Max Mustermann", vertrieb)

# Abteilung suchen
gesuchte_abteilung = unternehmen.abteilung_finden("Vertrieb")

if gesuchte_abteilung:
    print(f"Abteilung gefunden: {abteilung.bezeichnung}")
else:
    print(f"Abteilung {gesuchte_abteilung} nicht gefunden")

# Alle Mitarbeiter anzeigen
unternehmen.alle_mitarbeiter_anzeigen()

# Testen, dass Mitarbeiter nur einer Abteilung gleichzeitig zugewiesen sein kann
mitarbeiter1 = Mitarbeiter("xxx", "Doppelgänger")
unternehmen.abteilungen[0].mitarbeiter_hinzufügen(mitarbeiter1)
unternehmen.abteilungen[1].mitarbeiter_hinzufügen(mitarbeiter1)

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

# Mitarbeiter erzeugen mit Personalnummer die es bereits gibt, sollte fehlschlagen
mitarbeiter = unternehmen.mitarbeiter_erzeugen("001", "Max Mustermann", abteilungen[0])