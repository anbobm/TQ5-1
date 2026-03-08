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
        print("Keine Abteilung gefunden")
        
    def mitarbeiter_anzeigen(self):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                print(f"Mitarbeiter: {mitarbeiter.personalnummer}: {mitarbeiter.name}")
        
    def mitarbeiter_suchen(self, personalnummer):
        for abteilung in self.abteilungen:
            for mitarbeiter in self.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    print(f"Mitarbeiter mit Personalnummer {personalnummer} ist {mitarbeiter.name}.")
                else:
                    print(f"Keinen Mitarbeiter mit Personalnummer {personalnummer} gefunden.")

    # Aufgabe 3
    # Ergänze die Klasse Unternehmen um eine Methode info(), die alle Informationen zum Unternehmen, den Abteilungen und ihrer Mitarbeiter ausgibt, z.B. so:
    def info(self):
        print(f"Unternehmen: \n {self.name}")
    # Unternehmen X
    # Abteilung A
    # Mitarbeiter 1
    # Mitarbeiter 2
    # Abteilung B
    # Mitarbeiter 3
    # Abteilung C
    # Mitarbeiter 4
    # Mitarbeiter 5
    # Mitarbeiter 6


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

# Abteilung finden



# Mitarbeiter suchen
# firma1.mitarbeiter_suchen(2)
(firma1.abteilungen.mitarbeiter_suchen(2))