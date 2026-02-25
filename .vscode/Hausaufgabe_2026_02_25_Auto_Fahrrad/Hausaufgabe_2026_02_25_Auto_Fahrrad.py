# Hausaufgabe Fahrrad( Fahrzeug )

class Fahrzeug:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

    def info(self):
        print(
            f"Dieses Fahrzeug hat die Farbe {self._farbe} "
            f"und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. "
            f"Aktuelle Geschwindigkeit ist {self._geschwindigkeit}"
        )

    def beschleunigen(self, betrag):
        if betrag < 0:
            return
        self._geschwindigkeit += betrag
        if self._geschwindigkeit > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit

    def bremsen(self, betrag):
        if betrag < 0:
            return
        self._geschwindigkeit -= betrag
        if self._geschwindigkeit < 0:
            self._geschwindigkeit = 0

    def get_farbe(self):
        return self._farbe

    def set_farbe(self, farbe):
        if farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self._farbe = farbe


class Auto(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit):
        super().__init__(farbe, max_geschwindigkeit)
        self._motor_laeuft = False

    def motor_starten(self):
        self._motor_laeuft = True

    def motor_stoppen(self):
        self._motor_laeuft = False

    def beschleunigen(self, betrag):
        if not self._motor_laeuft:
            return
        super().beschleunigen(betrag)


class Fahrrad(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit, gaenge):
        super().__init__(farbe, max_geschwindigkeit)
        self._gang = 1
        self._gaenge = gaenge
        self._licht_an = False

    def hochschalten(self):
        if self._gang < self._gaenge:
            self._gang += 1

    def runterschalten(self):
        if self._gang > 1:
            self._gang -= 1

    def licht_einschalten(self):
        self._licht_an = True

    def licht_ausschalten(self):
        self._licht_an = False

        # --- Mini-Test ---

auto = Auto("rot", 180)
auto.info()
auto.beschleunigen(50)      # Motor läuft noch nicht → keine Wirkung
auto.motor_starten()
auto.beschleunigen(50)
auto.info()
auto.motor_stoppen()
auto.beschleunigen(50)      
auto.info()

print("-----")

fahrrad = Fahrrad("blau", 40, 5)
fahrrad.info()
fahrrad.hochschalten()
fahrrad.hochschalten()
fahrrad.runterschalten()
fahrrad.licht_einschalten()
fahrrad.beschleunigen(10)
fahrrad.info()