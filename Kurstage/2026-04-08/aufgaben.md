# Aufgabe 1 - Sequenzdiagramm mit Loop-Fragment

Zeichne ein UML-Sequenzdiagramm für den Methodenaufruf `vormerken()` der `Bibliothek`-Klasse. Benutze dafür das `loop`- und das `alt`-Fragment.

```python
class Bibliothek:
    def vormerken(self, nutzer : Nutzer, buecher : list[Buch]):
        nutzer.update()
        for buch in buecher:
            if buch.ist_verfügbar():
                buch.vormerken()
            else:
                self.show_error("Vormerken nicht möglich")
    
    def show_error(self):
        pass
            
class Nutzer:
    def update(self):
        pass

class Buch:
    def ist_verfügbar(self):
        pass
    def vormerken(self):
        pass
```