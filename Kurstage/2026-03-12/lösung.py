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
    def __init__(self, kantenlänge):
        super().__init__(kantenlänge, kantenlänge)

class Fünfeck(Form):
    pass


quadrat = Quadrat(10)
rechteck = Rechteck(3, 4)
dreieck = RechtwinkligesDreieck(3, 4)
kreis = Kreis(5)

# schlägt fehl, weil man von abstrakten Klassen keine Objekte erzeugen kann
# form = Form()

# schlägt fehl, weil abgleitete Klasse die abstrakte Methode flaeche() nicht implementiert hat
# fünfeck = Fünfeck()