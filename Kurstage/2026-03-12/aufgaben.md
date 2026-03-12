# Aufgabe 1

Das folgende Listing definiert eine Verbungsbeziehung zwischen Form, Kreis, RechtwinkligesDreieck, Quadrat und Rechteck.

Wie man sehen kann, definiert die Basisklasse Form eine Methode `flaeche()`, ohne bereits eine Basisimplementierung vorzugeben. Das macht auch Sinn, denn eine `Form` ist zu allgemein, um einen Flächeninhalt berechnen zu können.

Die Klasse Form ist also ein guter Kandidat für eine abstrakte Klasse.

Benutze die Klasse `ABC` und den decorator `abstractmethod` aus dem `abc`-Modul, um die Klasse `Form` und ihre Methode `flaeche()` als abstrakt zu deklarieren.

Alle abgeleiteten Klassen (die nicht selbst abstrakt sein sollen) sind dann gezwungen, die Methode `flaeche()` zu implementieren (zu überschreiben) und man kann von `Form` keine Objekte erzeugen.

Überzeuge dich selbst davon, dass das der Fall ist.

```python
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

class Rechteck(Form):
    def __init__(self, hoehe, breite):
        self._hoehe = hoehe
        self._breite = breite
     
    def flaeche(self):
        return self._breite * self._hoehe
    
class Quadrat(Rechteck):
    def __init__(self, kantenlänge):
        super().__init__(kantenlänge, kantenlänge)
```