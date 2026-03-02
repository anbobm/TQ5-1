# Aufgabe 2 Kreis(radius)
# Class Form
import math
class Form:
    def flaeche(self):
        pass

class Kreis(Form):
    def __init__(self, radius):
        self._radius = radius

    def flaeche(self):
        return math.pi * self._radius ** 2
    
class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        self._breite = breite
        self._hoehe = hoehe

    def flaeche(self):
        return (self._breite * self._hoehe) / 2


  # Testbereich

formen = [
    Kreis(3),
    Kreis(5),
    RechtwinkligesDreieck(4, 6),
    Kreis(2)
]

summe = 0

for form in formen:
    summe += form.flaeche()

print("Summe der Flaechen:", summe)  