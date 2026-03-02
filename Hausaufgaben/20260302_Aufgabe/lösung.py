#Aufgabe 1
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
    def __init__(self, kantenlaenge):
        super().__init__(kantenlaenge, kantenlaenge)

    def set_breite(self, wert):
        if wert <= 0:
            print("Nur positive Werte erlaubt")
            return
        self._breite = wert
        self._hoehe = wert

    def set_hoehe(self, wert):
        if wert <= 0:
            print("Nur positive Werte erlaubt")
            return
        self._breite = wert
        self._hoehe = wert

q = Quadrat(5)
print("Fläche:", q.flaeche())
print("Umfang:", q.umfang())

q.set_breite(10)
print("Neue Fläche:", q.flaeche())
print("Neue Höhe:", q._hoehe)

#Aufgabe 2
import math

class Form:
    def flaeche(self):
        pass

class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return math.pi * self.radius ** 2

class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        return 0.5 * self.breite * self.hoehe

formen = [Kreis(3), Kreis(5), RechtwinkligesDreieck(4, 6), Kreis(2)]

gesamt = 0

for form in formen:
    flaeche = form.flaeche()
    print("Fläche:", flaeche)
    gesamt += flaeche

print("Gesamtfläche aller Formen:", gesamt)