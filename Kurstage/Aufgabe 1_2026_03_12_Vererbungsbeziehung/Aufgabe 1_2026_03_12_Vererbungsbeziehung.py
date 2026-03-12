# Aufgabe 1


from math import sqrt, pi
from abc import ABC, abstractmethod


class Form(ABC):

    @abstractmethod
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


class Rechteck(Form):

    def __init__(self, hoehe, breite):
        self._hoehe = hoehe
        self._breite = breite

    def flaeche(self):
        return self._breite * self._hoehe


class Quadrat(Rechteck):

    def __init__(self, kantenlaenge):
        super().__init__(kantenlaenge, kantenlaenge)


class Fünfeck(Form):

    def flaeche(self):
        return 3


quadrat = Quadrat(10)
rechteck = Rechteck(3, 4)
dreieck = RechtwinkligesDreieck(3, 4)
kreis = Kreis(5)

print(quadrat.flaeche())
print(rechteck.flaeche())
print(dreieck.flaeche())
print(kreis.flaeche())