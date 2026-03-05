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

class Bibliothek:
    def __init__(self):
        self._medien = []
    
    def ausgeliehene_medien(self):
        print("Ausgeliehene Medien:")
        for medium in self._medien:
            if medium._ist_ausgeliehen:
                print(f"- {medium._titel}")

