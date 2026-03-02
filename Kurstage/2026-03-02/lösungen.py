# Aufgabe 1

class Rechteck:
    def __init__(self, hoehe, breite):
        self._hoehe = hoehe
        self._breite = breite

    def set_breite(self, wert):
        if wert <= 0:
            print("Nur positive Werte als Breite erlaubt")
            return
      
        self._breite = wert

    def set_hoehe(self, wert):
        if wert <= 0:
            print("Nur positive Werte als Höhe erlaubt")
            return
      
        self._hoehe = wert
        
    def flaeche(self):
        return self._breite * self._hoehe
  
    def umfang(self):
        return 2 * (self._hoehe + self._breite)
    
class Quadrat(Rechteck):
    def __init__(self, kantenlänge):
        super().__init__(kantenlänge, kantenlänge)
    
    def set_breite(self, wert):
        if wert <= 0:
            print("Nur positive Werte als Breite erlaubt")
            return
      
        self._breite = wert
        self._hoehe = wert

    def set_hoehe(self, wert):
        self.set_breite(wert)

rechteck = Rechteck(100, 50)

print(rechteck.umfang())
print(rechteck.flaeche())

quadrat = Quadrat(100)
quadrat.set_breite(50)
print(quadrat.umfang())
print(quadrat.flaeche())
