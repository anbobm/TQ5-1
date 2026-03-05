# Aufgabe 1
# Schreibe folgende Klassen:

# Medium
# Basisklasse für Medien, die in der Bibliothek zur Verfügung stehen
# Attribute: titel,ist_ausgeliehen
# Methoden: ausleihen(), zurueckgeben()
class Medium:
    def __init__(self, titel):
        self.titel = titel
        self.ist_ausgeliehen = False

    def ausleihen(self):
        self.ist_ausgeliehen = True
        print(f"{self.titel} wurde ausgeliehen.")  
            
    def zurueckgeben(self):
        self.ist_ausgeliehen = False
        print(f"{self.titel} wurde zurueckgegeben.")
        
# Buch
# Erbt von Medium
# Attribute: # seitenzahl, autor        
class Buch(Medium):
    def __init__(self, titel, seitenzahl, autor):
        super().__init__(titel)
        self.seitenzahl = seitenzahl
        self.autor = autor


# Dvd
# Erbt von Medium
# Attribute: laufzeit,regisseur
class DVD(Medium):
    def __init__(self, titel, laufzeit, regisseur):
        super().__init__(titel)
        self.laufzeit = laufzeit
        self.regisseur = regisseur
        

# Bibliothek
# Attribute: medien (Liste von Medien)
# Methoden: ausgeliehene_medien(): gibt Liste von Medien zurück, die ausgeliehen sind
class Bibliothek:
    def __init__(self):
        self.medien = []
     
    def ausgeliehene_medien(self):
        ausgeliehen = []
        for medium in self.medien:
            if medium.ist_ausgeliehen:
                ausgeliehen.append(medium)
                # print(f"{medium.titel} ist ausgeliehen.")
        return ausgeliehen
    
    
buchkrimi = Buch("Leichenblässe", 435, "Arielle die Meerjungfrau")
buchromanze = Buch("Taubendreck", 255, "Freund Doktor")
filmaction = DVD("Sneakers - Die Lautlosen", 95, "Phil Alden Robinson")
filmromanze = DVD("Dr. Doolittle", 90, "Betty Thomas")

buchkrimi.ausleihen()
filmaction.ausleihen()

biblio = Bibliothek()
biblio.medien = [buchkrimi, buchromanze, filmaction, filmromanze]

ausgeliehen = biblio.ausgeliehene_medien()
print("Bibliothesfunktion auslesen")
print("Ausgeliehene Medien:")
for medium in ausgeliehen:
    print(medium.titel)