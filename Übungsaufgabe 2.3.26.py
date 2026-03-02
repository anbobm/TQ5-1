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
    def __init__(self, seitenlaenge):
        super().__init__(seitenlaenge, seitenlaenge)
    
    def set_breite(self, wert):
        if wert <= 0:
            print("Nur positive Werte als Breite erlaubt")
            return
      
        self._breite = wert
        self._hoehe = wert
    
    def set_hoehe(self, wert):
        if wert <= 0:
            print("Nur positive Werte als Höhe erlaubt")
            return
      
        self._hoehe = wert
        self._breite = wert

class Form:
    def flaeche(self):
        pass

class Kreis(Form):
    def __init__(self, radius):
        self._radius = radius
    
    def flaeche(self):
        return 3.14 * self._radius ** 2

class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        self._breite = breite
        self._hoehe = hoehe
    
    def flaeche(self):
        return 0.5 * self._breite * self._hoehe

formen = [Kreis(5), Kreis(8),RechtwinkligesDreieck(8, 6), RechtwinkligesDreieck(4, 6)]
summe = 0

for form in formen:
    summe = summe + form.flaeche()

print(summe)