# Aufgabe 1

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
    
class Quadrat(Rechteck):
    def __init__(self, seite):
        super().__init__(seite, seite)

    # optional: sicherstellen, dass Quadrat bleibt
    def set_breite(self, wert):
        super().set_breite(wert)
        super().set_hoehe(wert)

    def set_hoehe(self, wert):
        super().set_hoehe(wert)
        super().set_breite(wert)

        print("=== Rechteck Test ===")
r = Rechteck(4, 6)
print("Fläche:", r.flaeche())   # 24
print("Umfang:", r.umfang())    # 20

print("\n=== Quadrat Test ===")
q = Quadrat(5)
print("Fläche:", q.flaeche())   # 25
print("Umfang:", q.umfang())    # 20

print("\nSeite ändern auf 7")
q.set_breite(7)
print("Fläche:", q.flaeche())   # 49
print("Umfang:", q.umfang())    # 28


