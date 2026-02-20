class Auto:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._geschwindigkeit = 0
        self._max_geschwindigkeit = max_geschwindigkeit

    @property
    def farbe(self):
        return self._farbe
    
    @farbe.setter
    def farbe(self, farbe):
        farbe_liste = ["rot", "blau", "grün", "schwarz", "weiß"]
        if farbe in farbe_liste:
            self._farbe = farbe
        else:
            print("Die Farbe wurde nicht gefunden!")

    def beschleunigen(self, betrag):
        self._geschwindigkeit = self._geschwindigkeit + betrag
        if self._geschwindigkeit > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit

    def bremsen(self, betrag):
        self._geschwindigkeit = self._geschwindigkeit - betrag
        if self._geschwindigkeit < 0:
            self._geschwindigkeit = 0

    def info(self):
         return f"Dieses Auto hat die Farbe {self._farbe} " \
              f"und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. " \
              f"Aktuelle Geschwindigkeit ist {self._geschwindigkeit}"
        
auto = Auto("grün", 220)
auto._geschwindigkeit = 30
print(auto.info())

auto.beschleunigen(200) #warten auf 230 aber bekommen 220
print(f"Die Geschwindigkeit mit Beschleunigung ist: {auto._geschwindigkeit}") # 220, weil max_speed 220 ist

auto.bremsen(300)
print(f"Die Geschwindigkeit mit Bremsen ist: {auto._geschwindigkeit}") #0

auto.farbe = "gelb" # Nicht gefunden!