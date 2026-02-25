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
    def __init__(self, motort_läuft, farbe, max_geschwindigkeit):
        motort_läuft = False
        self._motor_läuft = motort_läuft
        self._geschwindigkeit = 0
        super().__init__(farbe, max_geschwindigkeit)
    
    def motor_starten(self):
        self._motor_läuft = True
        return
    
    def motor_stoppen(self):
        self._motor_läuft = False
        return
    
    def beschleunigen(self, betrag):
        if self._motor_läuft == True:
            if betrag < 0:
                return
            self._geschwindigkeit = self._geschwindigkeit + betrag

            if self._geschwindigkeit > self._max_geschwindigkeit:
                self._geschwindigkeit = self._max_geschwindigkeit
        if self._motor_läuft == False:
            return
    
    def info(self):
        motor_brumm = ""
        if self._motor_läuft == True:
            motor_brumm = "Der Motor ist an"
        if self._motor_läuft == False:
            motor_brumm = "Der Motor ist nicht an"
        print(f"Dieses Fahrzeug hat die Farbe {self._farbe} und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. Aktuelle Geschwindigkeit ist {self._geschwindigkeit}. {motor_brumm}")

class Fahrrad(Fahrzeug):
    def __init__(self, gang, gänge, licht_an, farbe, max_geschwindigkeit):
        self._licht_an = licht_an
        licht_an = bool
        self._gang = gang
        gang = 1
        self._gänge = gänge
        super().__init__(farbe, max_geschwindigkeit)
    
    def hochschalten(self):
        if self._gang == self._gänge:
            return "Der höchste Gang ist schon drinnen."
        else:
            self._gang = self._gang + 1
            return
    
    def runterschalten(self):
        if self._gang > 1:
            self._gang = self._gang - 1
            return
        else:
            return "Der kleinste Gang ist schon drinnen."
        
    def licht_einschalten(self):
        self._licht_an = True
        return

    def licht_ausschalten(self):
        self._licht_an = False
        return

auto1 = Auto(False, "rot", 100)
print(auto1.info())




        
    


    
    