# Aufgabe 2
# Erstelle eine Klasse Rechteck.

# Sie hat private Attribute für Breite und Höhe, die der Konstruktor als Parameter erwartet.

# Methoden:
# set_breite(wert): (nur positive Werte erlauben)
# set_hoehe(wert): (nur positive Werte erlauben)
# flaeche(): gibt Flächeninhalt zurück
# umfang(): gibt Umfang zurück

# Erstelle eine Klasse Quadrat, die von Rechteck erbt.
# Ein Quadrat hat im Gegensatz zum Rechteck nur eine Kantenlänge, 
# keine Breite und Höhe, die sich unterscheiden.

class Rechteck:
    def __init__(self, hoehe, breite):
        self._hoehe = hoehe
        self._breite = breite
    
    def set_breite(self, wert):
        if wert < 0:
            print(f"Nur positive Werte zur Berechnung eingeben!")
        else:
            self._breite = wert
            print(f"Breite: {self._breite} gesetzt")
    
    def set_hoehe(self, wert):
        if wert < 0:
            print(f"Nur positive Werte zur Berechnung eingeben!")
        else:
            self._hoehe = wert
            print(f"Höhe: {self._hoehe} gesetzt")
    
    def flaeche(self):
        flaeche = self._breite * self._hoehe
        print(f"Die Fläche beträgt {flaeche}.")
        return flaeche
        
    def umfang(self):
        umfang = (self._breite + self._hoehe)*2
        print(f"Der Umfang beträgt {umfang}.")
        return umfang
    
class Quadrat(Rechteck):
    def __init__(self, kantenlaenge):
        super().__init__(kantenlaenge, kantenlaenge)
        self.kantenlaenge = kantenlaenge
        
    
    def set_kantenlaenge(self):
        self.kantenlaenge = self._hoehe or self._breite
    
    def flaeche(self):
        flaeche = self.kantenlaenge * self.kantenlaenge
        print(f"Die Fläche beträgt {flaeche}.")
        return flaeche
        
    def umfang(self):
        umfang = (self.kantenlaenge + self.kantenlaenge)*2
        print(f"Der Umfang beträgt {umfang}.")
        return umfang    
         
rechteck1 = Rechteck(2, 4)
rechteck2 = Rechteck(7.5, 15)
rechteck3 = Rechteck(3, 7)

quadrat1 = Quadrat(3)


rechteck1.set_breite(6)

rechteck1.flaeche()
rechteck1.umfang()
rechteck2.flaeche()
rechteck2.umfang()
rechteck3.flaeche()
rechteck3.umfang()
quadrat1.flaeche()