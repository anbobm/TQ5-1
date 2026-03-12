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
        return (self._breite * self._hoehe) / 2

class Rechteck(Form):
    def __init__(self, hoehe, breite):
        self._hoehe = hoehe
        self._breite = breite
     
    def flaeche(self):
        return self._breite * self._hoehe
    
class Quadrat(Rechteck):
    def __init__(self, kantenlänge):
        super().__init__(kantenlänge, kantenlänge)

k = Kreis(5)
print(k.flaeche())

r = Rechteck(4, 3)
print(r.flaeche())

d = RechtwinkligesDreieck(3, 4)
print(d.flaeche())

q = Quadrat(5)
print(q.flaeche())