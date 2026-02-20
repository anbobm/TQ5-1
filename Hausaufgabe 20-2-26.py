class auto:
    def __init__(self, _farbe, _geschwindigkeit, _max_geschwindigkeit):
        self._farbe = ""
        self._geschwindigkeit = 0
        self._max_geschwindigkeit = 0

    def info(self):
        return f"Das Auto hat die Farbe {self._farbe}, fährt mit {self._geschwindigkeit} km/h und hat eine maximale Geschwindigkeit von {self._max_geschwindigkeit} km/h."
    
    def beschleunigen(self, geschwindigkeit):
        if self._geschwindigkeit + geschwindigkeit <= self._max_geschwindigkeit and self._geschwindigkeit + geschwindigkeit >= 0:
            self._geschwindigkeit += geschwindigkeit
        elif self._geschwindigkeit + geschwindigkeit < 0:
            self._geschwindigkeit = 0
            return "Das Auto kommt zum Stillstand."
        else:
            self._geschwindigkeit = self._max_geschwindigkeit
            return "Das Auto erreicht die maximale Geschwindigkeit."
    
    def set_max_geschwindigkeit(self, max_geschwindigkeit):
        self._max_geschwindigkeit = max_geschwindigkeit
    
    def set_geschwindigkeit(self, geschwindigkeit):
        self._geschwindigkeit = geschwindigkeit
    
    def bremsen(self, bremsen):
        if self._geschwindigkeit - bremsen >= 0 and bremsen >= 0:
            self._geschwindigkeit -= bremsen
        elif bremsen < 0:
            return "Das ist Physikalisch nicht möglich."
        else:
            self._geschwindigkeit = 0
            return "Das Auto kommt zum Stillstand."
    
    def get_farbe(self):
        return self._farbe
    
    def set_farbe(self, farbe):
        farben = ["rot", "blau", "grün", "schwarz", "weiß"]
        if farbe in farben:
            self._farbe = farbe
        else:
            return "Ungültige Farbe."

auto1 = auto("", 0, 200)
auto2 = auto("", 0, 250)

auto1.set_farbe("rot")
auto1.set_geschwindigkeit(50)
auto1.set_max_geschwindigkeit(200)

print(auto1.info())

auto1.beschleunigen(30)
print(auto1.info())

auto1.bremsen(-90)
print(auto1.info())


