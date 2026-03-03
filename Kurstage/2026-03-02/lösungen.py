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


# Aufgabe 2

from math import sqrt, pi

class Form:
    def flaeche(self):
        pass

class Kreis(Form):
    def __init__(self, radius):
        self._radius = radius

    def flaeche(self):
        return pi * self._radius ** 2


class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        self._breite = breite
        self._hoehe = hoehe

    def flaeche(self):
        return sqrt(self._breite ** 2 + self._hoehe ** 2)


kreis = Kreis(2)
print(kreis.flaeche())

dreieck = RechtwinkligesDreieck(4, 5)
print(dreieck.flaeche())

formen = [Kreis(1), Kreis(2), RechtwinkligesDreieck(3, 4), Kreis(5), RechtwinkligesDreieck(1, 2)]

summe = 0

for form in formen:
    summe = summe + form.flaeche()

print(summe)


