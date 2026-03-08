# Aufgabe 1
# Klasse Unternehmen
# Attribute: name, abteilungen: Liste von Objekten vom Typ Abteilung ist
# Methoden: abteilung_hinzufügen(abteilung), abteilung_entfernen(abteilung)
from random import randint, choice
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
                    return mitarbeiter
                else:
                    print(f"Keinen Mitarbeiter mit Personalnummer {personalnummer} gefunden.")

    # Aufgabe 3
    # Ergänze die Klasse Unternehmen um eine Methode info(), die alle Informationen zum Unternehmen, den Abteilungen und ihrer Mitarbeiter ausgibt
    # def info(self):
    #     print(f"Unternehmen: \n {self.name}")
    #     print("Abteilungen:")
    #     for abteilung in self.abteilungen:
    #         print(f"Abteilung: {abteilung.bezeichnung}")
    #         print("Mitarbeiter:")
    #         for mitarbeiter in abteilung.mitarbeiter:
    #             print(f"{mitarbeiter.personalnummer}: {mitarbeiter.name}")
    
    def info(self): 
        print(f"\n=== Unternehmen: {self.name} ===") 
        if not self.abteilungen: 
            print("Keine Abteilungen vorhanden.") 
            return 
        for abteilung in self.abteilungen: 
            print(f"\nAbteilung: {abteilung.bezeichnung}") 
            if not abteilung.mitarbeiter: 
                print(" Keine Mitarbeiter in dieser Abteilung.") 
            else: 
                print(" Mitarbeiter:") 
                for mitarbeiter in abteilung.mitarbeiter: 
                    print(f" - {mitarbeiter.personalnummer}: {mitarbeiter.name}")


# Klasse Abteilung
# Attribute: bezeichnung, mitarbeiter: Liste von Objekten vom Typ Mitarbeiter
# Methoden: mitarbeiter_hinzufügen(mitarbeiter), mitarbeiter_entfernen(mitarbeiter)
class Abteilung:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = [] # : list[Abteilung]

    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)
        return self.mitarbeiter
 
    def mitarbeiter_entfernen(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)
        return self.mitarbeiter

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

firma1.abteilung_hinzufuegen(Abteilung("Geschäftsführung"))
firma1.abteilung_hinzufuegen(Abteilung("Projektplanung"))
firma2.abteilung_hinzufuegen(Abteilung("CEO"))
firma2.abteilung_hinzufuegen(Abteilung("Außendienst"))
firma2.abteilung_hinzufuegen(Abteilung("IT"))
firma2.abteilung_hinzufuegen(Abteilung("Cleaning")) 

ma1 = Mitarbeiter(1, "Sabine Sonne")
ma2 = Mitarbeiter(2, "Olaf Schneemann")
ma3 = Mitarbeiter("001", "Tunahan")
ma4 = Mitarbeiter("002", "Anne")
ma5 = Mitarbeiter("003", "Katja")
ma6 = Mitarbeiter("004", "Mohamad")
ma7 = Mitarbeiter("005", "Sebastian")
ma8 = Mitarbeiter("006", "Ihor")
ma9 = Mitarbeiter("007", "Ruwen")
ma10 = Mitarbeiter("008", "Nataliya")
ma11 = Mitarbeiter("009", "Andreas")
ma12 = Mitarbeiter("010", "Efkan")
mitarbeiter = [ma1, ma2, ma3, ma4, ma5, ma6, ma7, ma8, ma9, ma10, ma11, ma12]

# Mitarbeiter hinzufuegen
for mitarbeiter in mitarbeiter:
    zufällige_abteilung = choice(firma2.abteilungen)
    zufällige_abteilung.mitarbeiter_hinzufuegen(mitarbeiter)
    
# Abteilungen hinzufügen
# for abteilung in abteilungen:
#     unternehmen.abteilung_hinzufügen(abteilung)
       
# Abteilung finden



# Mitarbeiter suchen
# firma1.mitarbeiter_suchen(2)

firma1.info()
firma2.info()
