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

    def info(self):
        print(f"Unternehmen: {self.name}")
        print("Abteilungen:")
        for abteilung in self.abteilung:
            print(f"  - {abteilung.name}")
            print("    Mitarbeiter:")
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"      - {mitarbeiter.name} (Personalnummer: {mitarbeiter.personalnummer})")

class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name
    
