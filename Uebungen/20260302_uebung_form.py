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
    def __init__(self):
        
    def flaeche():
        pass
    
    
class Kreis(Form):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius 
    
    def flaeche_kreis():
        if radius <= 0:
            print("Der Radius muß größer 0 sein.")
        flaeche_kreis = math.pi * radius**2
        
        
        
class RechtwinkligesDreieck(Form):
    def __init__(self, breite, hoehe):
        super().__init__()
        self.breite = breite
        self.hoehe = hoehe
        
    def flaeche_dreieck():
        flaeche_dreieck = breite * hoehe
        
formen = [Kreis(3), Kreis(5,5), RechtwinkligesDreieck(5,7), Kreis(7), RechtwinkligesDreieck(4,9)]
flaechensumme = 0

for form in formen:
    if form == Kreis:
        flaechensumme = flaechensumme + flaeche_kreis
    elif:
        flaechensumme = flaechensumme + 

     