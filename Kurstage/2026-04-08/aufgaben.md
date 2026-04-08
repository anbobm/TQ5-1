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

# Aufgabe 2 - Docstrings

Schreibe Docstrings für Module, Klassen und Methoden in folgenden beiden Modulen:

[Bibliothek](https://github.com/anbobm/TQ5-1/blob/main/Kurstage/2026-03-05/l%C3%B6sung.py)

[Unternehmen](https://github.com/anbobm/TQ5-1/blob/main/Kurstage/2026-03-06/l%C3%B6sung.py)

[Shop (Aufgabe 2)](https://github.com/anbobm/TQ5-1/blob/main/Kurstage/2026-04-01/aufgaben.md#aufgabe-2)