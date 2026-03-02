# Aufgabe 1

Erstelle eine Klasse Quadrat, die von Rechteck erbt. Ein Quadrat hat im Gegensatz zum Rechteck nur eine Kantenlänge, keine Breite und Höhe die sich unterscheiden.

```python
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
```

# Aufgabe 2

Erstelle eine Basisklasse namens `Form` mit der Methode `flaeche()` (die kann leer sein: `pass`).

Erstelle eine Klasse `Kreis(radius)` und eine Klasse `RechtwinkligesDreieck(breite, hoehe)`, die von `Form` erben und jeweils die Methode `flaeche()` implementieren (überschreiben).

Erstelle anschließend eine Liste aus Objekten der beiden Klassen, z.B. `formen = [Kreis(..), Kreis(..), RechtwinkligesDreieck(..), Kreis, ....]`.

Durchlaufe diese Liste in einer Schleife und berechne die Summe aller Flächeninhalte dieser Formen.

**Hinweis**: Quadratwurzeln (square roots) kann man mit `sqrt()` aus dem `math` Modul berechnen.