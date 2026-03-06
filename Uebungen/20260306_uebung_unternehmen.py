# Aufgabe 1
# Klasse Unternehmen
# Attribute: name, abteilungen: Liste von Objekten vom Typ Abteilung ist
# Methoden: abteilung_hinzufügen(abteilung), abteilung_entfernen(abteilung)
class Unternehmen:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []
        
    def abteilung_hinzufuegen(self, abteilung):
        self.abteilungen.append(abteilung)
        
    def abteilung_entfernen(self, abteilung):
        self.abteilungen.remove(abteilung)


    # Aufgabe 2
    # Ergänze die Klasse Unternehmen um folgende Methoden:
    def abteilung_finden(self, bezeichnung):
        for abteilung in self.abteilungen:
            if abteilung.bezeichnung == bezeichnung:
                return abteilung
        return None
        
    def mitarbeiter_anzeigen(self):
        print(f"Mitarbeiter: {self.mitarbeiter}")
        
    def mitarbeiter_suchen(self, personalnummer):
        for mitarbeiter in self.mitarbeiter:
            if mitarbeiter.personalnummer == personalnummer:
                print(f"Mitarbeiter mit Personalnummer {personalnummer} ist {mitarbeiter.name}.")
        return None

# Klasse Abteilung
# Attribute: bezeichnung, mitarbeiter: Liste von Objekten vom Typ Mitarbeiter
# Methoden: mitarbeiter_hinzufügen(mitarbeiter), mitarbeiter_entfernen(mitarbeiter)
class Abteilung:
    def __init(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = [] # : list[Abteilung]

    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
 
    def mitarbeiter_entfernen(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)
        

# Klasse Mitarbeiter
# Attribute: personalnummer, name
class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name    
        

 
        
# Unternehmen erzeugen
firma1 = Unternehmen("Maler Gmbh")
firma2 = Unternehmen("Incognito Spy Co.KG Ltd.")
firma3 = Unternehmen("bodycare")

print(firma1.name)
print(firma2.name)
print(firma3.name)

firma1.abteilung_hinzufuegen("Geschäftsführung")
firma1.abteilung_hinzufuegen("Projektplanung")
firma2.abteilung_hinzufuegen("CEO")
firma2.abteilung_hinzufuegen("Außendienst")
firma2.abteilung_hinzufuegen("IT")
firma2.abteilung_hinzufuegen("Cleaning") 

ma1 = Mitarbeiter(1, "Sabine Sonne")
ma2 = Mitarbeiter(2, "Olaf Schneemann")

# Mitarbeiter hinzufuegen


# Mitarbeiter suchen
firma1.mitarbeiter_suchen(2)