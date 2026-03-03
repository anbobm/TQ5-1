class Fahrzeug:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

    def info(self):
        print(f"Dieses Fahrzeug hat die Farbe {self._farbe} und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. Aktuelle Geschwindigkeit ist {self._geschwindigkeit}")

    def beschleunigen(self, betrag):
        if betrag < 0:
            return

        self._geschwindigkeit = self._geschwindigkeit + betrag

        if self._geschwindigkeit > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit

    def bremsen(self, betrag):
        if betrag < 0:
            return
        
        self._geschwindigkeit = self._geschwindigkeit - betrag

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
        self._motor_läuft = False

    def motor_starten(self):
        self._motor_läuft = True

    def motor_stoppen(self):
        self._motor_läuft = False

    def beschleunigen(self, betrag):
        if self._motor_läuft:
            super().beschleunigen(betrag)


class Fahrrad(Fahrzeug):
    # zwei private Attribute: _gang und _gänge
    def __init__(self, farbe, max_geschwindigkeit, gänge):
        super().__init__(farbe, max_geschwindigkeit)
        self._gang = 1
        self._gänge = gänge
        self._licht_an = False

    def hochschalten(self):
        self._gang += 1

        if self._gang > self._gänge:
            self._gang = self._gänge

        print(f"Du bist im {self._gang}-ten Gang.")

    def runterschalten(self):
        if self._gang == 1:
            print("Du kannst nicht mehr runterschalten")
        else:
            self._gang -= 1
            print(f"Du bist im {self._gang}-ten Gang.")

    def licht_einschalten(self):
        self._licht_an = True
        print("Licht ist an")

    def licht_ausschalten(self):
        self._licht_an = False
        print("Licht ist aus")


fahrrad1 = Fahrrad("grün", 100, 7)

fahrrad1.info()

fahrrad1.hochschalten()
fahrrad1.hochschalten()
fahrrad1.hochschalten()
fahrrad1.hochschalten()
fahrrad1.hochschalten()
fahrrad1.hochschalten()
fahrrad1.hochschalten()
print(fahrrad1._gang)

fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
fahrrad1.runterschalten()
print(fahrrad1._gang)

fahrrad1.licht_einschalten()
print(fahrrad1._licht_an)

fahrrad1.licht_ausschalten()
print(fahrrad1._licht_an)

auto = Auto("grün", 250)

auto.beschleunigen(100)
auto.info()
auto.motor_starten()
auto.beschleunigen(100)
auto.info()