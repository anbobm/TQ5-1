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
        self.ausgeliehen_von = None

    def ausleihen(self):
        self.ist_ausgeliehen = True
        print(f"{self.titel} wurde ausgeliehen.")  
            
    def zurueckgeben(self):
        self.ist_ausgeliehen = False
        print(f"{self.titel} wurde zurueckgegeben.")
        
    # Erweitere die Klasse Medium um das Attribut ausgeliehen_von, welches den ausleihenden Benutzer speichert. Füge die Methoden ausleihen(benutzer) und zurückgeben() hinzu.
    def ausleihen_von(self, benutzer):
        if self.ist_ausgeliehen == False:
            self.ausgeliehen_von = benutzer
            self.ist_ausgeliehen = True
            print(f"Das Medium {self.titel} wurde von {benutzer} ausgeliehen.")
        else:
            print(f"Das gewünschte Medium {self.titel} ist bereits verliehen.")
        
    def zurueckgeben(self):
        print(f"Das Medium {self.titel} wurde von {benutzer} zurückgegeben.")
        
           
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

    # Aufgabe 2
    # Erweitere die Klasse Bibliothek so, dass man mit hinzufuegen(medium) neue Medien hinzufügen kann.
    def hinzufuegen(self, medium):
        self.medien.append(medium)
        print(f"Das Medium {medium.titel} wurde in die Bibliothek eingepflegt.")
    
    
    # Aufgabe 4
    # Füge der Klasse Bibliothek hinzu:    
    # anzahl_medien(): gibt die Anzahl aller Medien zurück
    # anzahl_buecher(): gibt die Anzahl aller Bücher zurück (type(..))
    # anzahl_dvds(): gibt die Anzahl aller Dvds zurück
    # anzahl_ausgeliehen(): gibt die Anzahl der ausgeliehenen Medien zurück
    # anzahl_verfügbar(): gibt die Anzahl der verfügbaren Medien zurück
    def anzahl_medien(self):
        return len(self.medien)
        
    def anzahl_buecher(self):
        count = 0
        for medium in self.medien:
            if type(medium) == Buch:
                count = count + 1
        return count
    
    def anzahl_dvds(self):
        count = 0
        for medium in self.medien:
            if type(medium) == DVD:
                count = count + 1
        return count
    
    def anzahl_ausgeliehen(self):
        # return len(self.ausgeliehene_medien)
        count = 0
        for medium in self.medien:
            if medium.ist_ausgeliehen:
                count = count + 1
        return count
    
    def anzahl_verfuegbar(self):
        # return self.anzahl_medien() - anzahl_ausgeliehen()
        count = 0
        for medium in self.medien:
            if not medium.ist_ausgeliehen:
                count = count + 1
        return count
    
    # Aufgabe 3
    # Erstelle eine Klasse Benutzer mit dem Attribut name.
class benutzer:
    def __init__(self, name):
        self.name = name
        
    



   
    
buch1 = Buch("Leichenblässe", 435, "Arielle die Meerjungfrau")
buch2 = Buch("Taubendreck", 255, "Freund Doktor")
film1 = DVD("Sneakers - Die Lautlosen", 95, "Phil Alden Robinson")
film2 = DVD("Dr. Doolittle", 90, "Betty Thomas")
buch3 = Buch("Alice im Wunderland", 395, "Fred Feuerstein")
film3 = DVD("Tinkerbell und die Feenschwestern", 80, "Anna & Elsa")


buch1.ausleihen_von("Karl")
film1.ausleihen_von("Katja")

biblio = Bibliothek()
biblio.medien = [buch1, buch2, film1, film2]

ausgeliehen = biblio.ausgeliehene_medien()

print("Bibliotheksfunktion auslesen")
print("Ausgeliehene Medien:")
for medium in ausgeliehen:
    print(medium.titel)
    
biblio.hinzufuegen(film3)

print(biblio.anzahl_medien())