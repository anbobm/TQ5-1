class Auto:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._geschwindigkeit = 0
        self._max_geschwindigkeit = max_geschwindigkeit

    def info(self):
        print(f"Dieses Auto hat die Farbe {self._farbe} "
              f"und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. "
              f"Aktuelle Geschwindigkeit ist {self._geschwindigkeit}")
        
auto = Auto("grün", 220)
auto._geschwindigkeit = 30
auto.info()
