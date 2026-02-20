class Auto:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._geschwindigkeit = 0
        self._max_geschwindigkeit = max_geschwindigkeit

    def get_farbe(self):
        return self._farbe

    def set_farbe(self, farbe):
        self._farbe = farbe

    def beschleunigen(self, betrag):
        self._geschwindigkeit = self._geschwindigkeit + betrag
        if self._geschwindigkeit > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit

    def bremsen(self, betrag):
        self._geschwindigkeit = self._geschwindigkeit - betrag
        if self._geschwindigkeit < 0:
            self._geschwindigkeit = 0

    def info(self):
        print(f"Dieses Auto hat die Farbe {self._farbe} "
              f"und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. "
              f"Aktuelle Geschwindigkeit ist {self._geschwindigkeit}")
        
auto = Auto("grün", 220)
auto._geschwindigkeit = 30
auto.info()

