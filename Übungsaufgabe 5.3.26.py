class Medium:
    def __init__(self, titel, ist_ausgeliehen):
        self._titel = titel
        self._ist_ausgeliehen = ist_ausgeliehen
    
    def ausleihen(self):
        if not self._ist_ausgeliehen:
            self._ist_ausgeliehen = True
            print(f"{self._titel} wurde ausgeliehen.")
        else:
            print(f"{self._titel} ist bereits ausgeliehen.")
    
    def zurückgeben(self):
        if self._ist_ausgeliehen:
            self._ist_ausgeliehen = False
            print(f"{self._titel} wurde zurückgegeben.")
        else:
            print(f"{self._titel} ist nicht ausgeliehen.")
    
class Buch(Medium):
    def __init__(self, titel, ist_ausgeliehen, seitenzahl, autor):
        super().__init__(titel, ist_ausgeliehen)
        self._seitenzahl = seitenzahl
        self._autor = autor

class DVD(Medium):
    def __init__(self, titel, ist_ausgeliehen, laufzeit, regisseur):
        super().__init__(titel, ist_ausgeliehen)
        self._laufzeit = laufzeit
        self._regisseur = regisseur

class Bibliothek(Medium):
    def __init__(self):
        self._medien = []
 
    def hinzufügen_medium(self, medium : Medium):
        self._medien.append(medium)
        print(f"{medium._titel} wurde zur Bibliothek hinzugefügt.")
    
    def ausgeliehene_medien(self):
        ausgeliehen = []

        for medium in self._medien:
            if medium._ist_ausgeliehen:
                ausgeliehen.append(medium)
        
        return ausgeliehen
    
        

Buch1 = Buch("Der Herr der Ringe", True, 1178, "J.R.R. Tolkien")

ausgeliehene_medien = Bibliothek()
ausgeliehene_medien.hinzufügen_medium(Buch1)
ausgeliehene_medien.ausgeliehene_medien()

print("Ausgeliehene Medien")
for medium in ausgeliehene_medien.ausgeliehene_medien():
    print(medium._titel)
