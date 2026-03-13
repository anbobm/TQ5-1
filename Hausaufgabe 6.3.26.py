class Unternehmen:
    def __init__(self, name, abteilung):
        self.name = name
        self.abteilung = abteilung
    
    def abteilung_hinzufuegen(self, abteilung):
        self.abteilung.append(abteilung)
    
    def abteilung_entfernen(self, abteilung):
        self.abteilung.remove(abteilung)
    
    def abteilung_finden(self, bezeichnung):
        for abteilung in self.abteilung:
            if abteilung.name == bezeichnung:
                return abteilung
        return None

    def alle_mitarbeiter_anzeigen(self):
        for abteilung in self.abteilung:
            print(f"Abteilung: {abteilung.name}")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"  - {mitarbeiter.name} (Personalnummer: {mitarbeiter.personalnummer})")
    
    def mitarbeiter_suchen(self, personalnummer):
        for abteilung in self.abteilung:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter
        return None
     
    def mitarbeiter_erzeugen(self, personalnummer, name, abteilung):
        if self.mitarbeiter_suchen(personalnummer) is not None:
            print(f"Fehler: Ein Mitarbeiter mit der Personalnummer {personalnummer} existiert bereits.")
            return None
        neuer_mitarbeiter = Mitarbeiter(personalnummer, name, abteilung)
        abteilung.mitarbeiter_hinzufuegen(neuer_mitarbeiter)
        return neuer_mitarbeiter

    def info(self):
        print(f"Unternehmen: {self.name}")
        print("Abteilungen:")
        for abteilung in self.abteilung:
            print(f"  - {abteilung.name}")
            print("    Mitarbeiter:")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"      - {mitarbeiter.name} (Personalnummer: {mitarbeiter.personalnummer})")

class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
    
    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        abteilung = mitarbeiter.abteilung
        if abteilung:
            self.mitarbeiter.append(mitarbeiter)
    
    def mitarbeiter_entfernen(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)

class Mitarbeiter:
    def __init__(self, personalnummer, name, abteilung):
        self.personalnummer = personalnummer
        self.name = name
        self.abteilung = abteilung

# Aufgabe 5
# Wir wollen durchsetzen, dass die personalnummer des Mitarbeiters in einem Unternehmen eindeutig ist. Dazu erstellen wir eine mitarbeiter_erzeugen() Methode in Unternehmen, der einen Mitarbeiter nur erstellt, wenn es die übergebene personalnummer nicht gibt. Der Konstruktor von Mitarbeiter soll nur von dieser Methode aufgerufen werden.