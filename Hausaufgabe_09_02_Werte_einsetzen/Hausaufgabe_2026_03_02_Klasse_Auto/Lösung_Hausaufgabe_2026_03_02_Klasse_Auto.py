# Aufgabe Fahrzeug_AUTO_FAHRRAD


class Fahrzeug:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

    def info(self):
        print(f"Dieses Fahrzeug hat die Farbe {self._farbe} "
              f"und die Maximalgeschwindigkeit {self._max_geschwindigkeit} km/h. "
              f"Aktuelle Geschwindigkeit ist {self._geschwindigkeit} km/h.")

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

    def set_farbe(self, farbe):
        if farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self._farbe = farbe
        else:
            print("Farbe in diesem Universum nicht möglich!")


class Auto(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit):
        super().__init__(farbe, max_geschwindigkeit)
        self._motor_läuft = False

    def motor_starten(self):
        self._motor_läuft = True
        print("Motor läuft")

    def motor_stoppen(self):
        self._motor_läuft = False
        print("Motor gestoppt")

    def beschleunigen(self, betrag):
        if self._motor_läuft:
            super().beschleunigen(betrag)
        else:
            print("Motor ist nicht gestartet!")



class Fahrrad(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit, gaenge):
        super().__init__(farbe, max_geschwindigkeit)
        self._gang = 1
        self._gaenge = gaenge
        self._licht_an = False

    def hochschalten(self):
        if self._gang < self._gaenge:
            self._gang += 1
            print(f"Du bist jetzt im {self._gang}. Gang.")
        else:
            print("So viele Gänge hat dein Fahrrad nicht.")

    def runterschalten(self):
        if self._gang > 1:
            self._gang -= 1
            print(f"Du bist jetzt im {self._gang}. Gang.")
        else:
            print("Du kannst nicht mehr runterschalten.")

    def licht_einschalten(self):
        self._licht_an = True
        print("Licht ist an")

    def licht_ausschalten(self):
        self._licht_an = False
        print("Licht ist aus")


auto1 = Auto("weiß", 235)
auto1.motor_starten()
auto1.beschleunigen(100)
auto1.info()

bike1 = Fahrrad("blau", 40, 7)
bike1.hochschalten()
bike1.licht_einschalten()
bike1.info()

