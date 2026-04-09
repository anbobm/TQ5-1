class Auto:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

    def info(self):
        print(
            f"Dieses Auto hat die Farbe {self._farbe} "
            f"und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. "
            f"Aktuelle Geschwindigkeit ist {self._geschwindigkeit}"
        )

    def beschleunigen(self, betrag):
        self._geschwindigkeit = self._geschwindigkeit + betrag
        if self._geschwindigkeit > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit

    def bremsen(self, betrag):
        self._geschwindigkeit = self._geschwindigkeit - betrag
        if self._geschwindigkeit < 0:
            self._geschwindigkeit = 0

    def get_farbe(self):
        return self._farbe

    def set_farbe(self, farbe):
        if farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self._farbe = farbe


auto1 = Auto("grün", 220)
auto2 = Auto("rot", 150)

auto1.info()
auto1.beschleunigen(220)
auto1.info()
auto1.beschleunigen(1)
auto1.info()

auto1.bremsen(220)
auto1.info()
auto1.bremsen(1)
auto1.info()

auto1.set_farbe("foo")
auto1.info()
auto1.set_farbe("schwarz")
auto1.info()