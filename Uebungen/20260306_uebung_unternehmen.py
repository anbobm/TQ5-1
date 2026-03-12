# Aufgabe 1
# Klasse Unternehmen
# Attribute: name, abteilungen: Liste von Objekten vom Typ Abteilung ist
# Methoden: abteilung_hinzufügen(abteilung), abteilung_entfernen(abteilung)
from random import randint, choice
class Unternehmen:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []
        self.mitarbeiter = []
        
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
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    print(f"Mitarbeiter mit Personalnummer {personalnummer} ist {mitarbeiter.name}.")
                    return mitarbeiter
                else:
                    print(f"Keinen Mitarbeiter mit Personalnummer {personalnummer} gefunden.")

    # Aufgabe 5
    # Wir wollen durchsetzen, dass die personalnummer des Mitarbeiters in einem Unternehmen eindeutig ist. Dazu erstellen wir eine mitarbeiter_erzeugen() Methode in Unternehmen, der einen Mitarbeiter nur erstellt, wenn es die übergebene personalnummer nicht gibt. Der Konstruktor von Mitarbeiter soll nur von dieser Methode aufgerufen werden.
    def mitarbeiter_erzeugen(self, personalnummer, name):
        for m in self.mitarbeiter:
            if m.personalnummer == personalnummer:
                print(f"Fehler: Die Personalnummer {personalnummer} ist bereits vergeben.")
                return None
            
        mitarbeiter_neu = Mitarbeiter(personalnummer, name)
        self.mitarbeiter.append(mitarbeiter_neu)
        return mitarbeiter_neu
    
    
    # # Aufgabe 3
    # # Ergänze die Klasse Unternehmen um eine Methode info(), die alle Informationen zum Unternehmen, den Abteilungen und ihrer Mitarbeiter ausgibt
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
        if mitarbeiter.abteilung is not None:
            print(f"{mitarbeiter.name} ist bereits in Abteilung {mitarbeiter.abteilung.bezeichnung}")
            return
        self.mitarbeiter.append(mitarbeiter)
        return self.mitarbeiter
 
    def mitarbeiter_entfernen(self, mitarbeiter):
        if mitarbeiter in self.mitarbeiter:
            self.mitarbeiter.remove(mitarbeiter)
            mitarbeiter.abteilung = None

# Klasse Mitarbeiter
# Attribute: personalnummer, name
class Mitarbeiter:
    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name
        self.abteilung = None    
        
# Aufgabe 4
# Ergänze die Klasse Mitarbeiter um ein Attribut abteilung. Mit diesem soll sichergestellt werden, dass man einen Mitarbeiter nur einer Abteilung zuweisen kann.
 
        
# Unternehmen erzeugen
firma1 = Unternehmen("Maler Gmbh")
firma2 = Unternehmen("Incognito Spy Co.KG Ltd.")
firma3 = Unternehmen("bodycare")

print(firma1.name)
print(firma2.name)
print(firma3.name)

# Abteilungen erzeugen
firma1.abteilung_hinzufuegen(Abteilung("Geschäftsführung"))
firma1.abteilung_hinzufuegen(Abteilung("Projektplanung"))
firma2.abteilung_hinzufuegen(Abteilung("CEO"))
firma2.abteilung_hinzufuegen(Abteilung("Außendienst"))
firma2.abteilung_hinzufuegen(Abteilung("IT"))
firma2.abteilung_hinzufuegen(Abteilung("Cleaning")) 

# Mitarbeiter erzeugen
ma1 = firma2.mitarbeiter_erzeugen(1, "Sabine Sonne")
ma2 = firma2.mitarbeiter_erzeugen(2, "Olaf Schneemann")
ma3 = firma2.mitarbeiter_erzeugen("001", "Tunahan")
ma4 = firma2.mitarbeiter_erzeugen("002", "Anne")
ma5 = firma2.mitarbeiter_erzeugen("003", "Katja")
ma6 = firma2.mitarbeiter_erzeugen("004", "Mohamad")
ma7 = firma2.mitarbeiter_erzeugen("005", "Sebastian")
ma8 = firma2.mitarbeiter_erzeugen("006", "Ihor")
ma9 = firma2.mitarbeiter_erzeugen("007", "Ruwen")
ma10 = firma2.mitarbeiter_erzeugen("008", "Nataliya")
ma11 = firma2.mitarbeiter_erzeugen("009", "Andreas")
ma12 = firma2.mitarbeiter_erzeugen("010", "Efkan")
mitarbeiter = [ma1, ma2, ma3, ma4, ma5, ma6, ma7, ma8, ma9, ma10, ma11, ma12]

ma1 = firma1.mitarbeiter_erzeugen(1, "Sabine Sonne")
ma2 = firma1.mitarbeiter_erzeugen(2, "Olaf Schneemann")
ma3 = firma1.mitarbeiter_erzeugen("001", "Tunahan")
ma4 = firma1.mitarbeiter_erzeugen("002", "Anne")
ma5 = firma1.mitarbeiter_erzeugen("003", "Katja")
ma6 = firma1.mitarbeiter_erzeugen("004", "Mohamad")
ma7 = firma1.mitarbeiter_erzeugen("005", "Sebastian")
ma8 = firma1.mitarbeiter_erzeugen("006", "Ihor")
ma9 = firma1.mitarbeiter_erzeugen("007", "Ruwen")
ma10 = firma1.mitarbeiter_erzeugen("008", "Nataliya")
ma11 = firma1.mitarbeiter_erzeugen("009", "Andreas")
ma12 = firma1.mitarbeiter_erzeugen("010", "Efkan")

# Abteilungen hinzufügen
for abteilung in abteilungen:
    firma1.abteilung_hinzufügen(abteilung)

# Abteilung suchen
gesuchte_abteilung = "Projektplanung"
if firma1.abteilung_finden(gesuchte_abteilung):
    print(f"Abteilung {gesuchte_abteilung} gefunden")
else:
    print(f"Abteilung {gesuchte_abteilung} nicht gefunden")

# Alle Mitarbeiter anzeigen
firma2.alle_mitarbeiter_anzeigen()

# Mitarbeiter hinzufuegen
for mitarbeiter in mitarbeiter:
    zufällige_abteilung = choice(firma2.abteilungen)
    zufällige_abteilung.mitarbeiter_hinzufuegen(mitarbeiter)

for mitarbeiter in mitarbeiter:
    zufällige_abteilung = choice(firma1.abteilungen)
    zufällige_abteilung.mitarbeiter_hinzufuegen(mitarbeiter)   


firma1.info()
firma2.info()
