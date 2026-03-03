# Aufgabe 2
# Erstelle eine Basisklasse namens Form mit der Methode flaeche() 
# (die kann leer sein: pass).

# Erstelle eine Klasse Kreis(radius) und 
# eine Klasse RechtwinkligesDreieck(breite, hoehe), 
# die von Form erben und jeweils die Methode flaeche() implementieren (überschreiben).

# Erstelle anschließend eine Liste aus Objekten der beiden Klassen,
# z.B. formen = [Kreis(..), Kreis(..), RechtwinkligesDreieck(..), Kreis, ....].

# Durchlaufe diese Liste in einer Schleife und berechne die Summe 
# aller Flächeninhalte dieser Formen.

# Hinweis: Quadratwurzeln (square roots) kann man mit sqrt() 
# aus dem math Modul berechnen.
import math

class Form:
    def flaeche():
        pass
    
    
class Kreis(Form):
    def __init__(self, radius):
        self._radius = radius 
    
    def flaeche():
        return math.pi * self._radius ** 2
        
        
        
class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        self._breite = breite
        self._hoehe = hoehe
        
    def flaeche():
        return math.sqrt(self._breite ** 2 + self._hoehe ** 2)
    
    
        
formen = [Kreis(3), Kreis(5), RechtwinkligesDreieck(5,7), Kreis(7), RechtwinkligesDreieck(4,9)]
flaechensumme = 0

for form in formen:
        flaechensumme = flaechensumme + form.flaeche()
        
print(flaechensumme)

     