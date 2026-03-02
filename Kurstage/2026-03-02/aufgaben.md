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
´´´