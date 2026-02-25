# Aufgabe

Wir nehmen uns die Klasse `Auto` aus der vorherigen Aufgabe und nennen sie in `Fahrzeug` um. Außerdem passen wir die Ausgabe von `info()` entsprechend an:

```python
class Fahrzeug:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

    def info(self):
        print(f"Dieses Fahrzeug hat die Farbe {self._farbe} und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. Aktuelle Geschwindigkeit ist {self._geschwindigkeit}")

    def beschleunigen(self, betrag):
        if betrag < 0:
            return

        self._geschwindigkeit = self._geschwindigkeit + betrag

        if self._geschwindigkeit > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit

    def bremsen(self, betrag):
        if betrag < 0:
            return
        
        self._geschwindigkeit = self._geschwindigkeit - betrag

        if self._geschwindigkeit < 0:
            self._geschwindigkeit = 0
    
    def get_farbe(self):
        return self._farbe
    
    def set_farbe(self, farbe):
        if farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self._farbe = farbe
```

Implementiere jetzt eine Klasse `Auto` und eine Klasse `Fahrrad`, die von der Klasse `Fahrzeug` erben.

## `Auto`

`Auto` soll ein privates Attribut `_motor_läuft` (bool) mit dem Startwert `False` haben.

Geändert wird dieses Attribut durch die Methoden `motor_starten()` und `motor_stoppen()`.

Die Methode `beschleunigen()` aus der Basisklasse `Fahrzeug` soll überschrieben werden, so dass das Beschleunigen nur dann einen Effekt hat, wenn `_motor_läuft` wahr ist.

## `Fahrrad`

`Fahrrad` soll zwei private Attribute `_gang` und `_gänge` haben. `_gang` wird im Konstruktor auf `1` gesetzt. `_gänge` soll auf den übergebenen Parameter `gänge` gesetzt werden, und hält fest wie viele Gänge das Fahrrad besitzt.

Geändert wird das Attribut `_gang` über die Methoden `hochschalten()` und `runterschalten()`, die den aktuellen `_gang` jeweils um 1 erhöhen oder verringern, aber nur zwischen 1 und `_gänge`.

Außerdem soll `Fahrrad` ein Attribut `_licht_an` (bool) besitzen, welches über `licht_einschalten()` und `licht_ausschalten()` geändert wird.