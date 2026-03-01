class Fahrzeug:
    def __init__(self, _farbe, max_geschwindigkeit):
        self._farbe = _farbe
        self.max_geschwindigkeit = max_geschwindigkeit
        self.geschwindigkeit = 0

    def info(self):
        print(f"Dieses Fahrzeug hat die Farbe {self._farbe} und eine Maximalgeschwindigkeit von {self.max_geschwindigkeit}. Die aktuelle Geschwindigkeit ist {self.geschwindigkeit}.")

    def beschleunigen(self, betrag):
        if betrag < 0:
            return

        self.geschwindigkeit = self.geschwindigkeit + betrag

        if self.geschwindigkeit > self.max_geschwindigkeit:
            self.geschwindigkeit = self.max_geschwindigkeit

    def bremsen(self, betrag):
        if betrag < 0:
            return
        
        self.geschwindigkeit = self.geschwindigkeit - betrag

        if self.geschwindigkeit < 0:
            self.geschwindigkeit = 0
    
    def get_farbe(self):
        return self._farbe
    
    def set_farbe(self, farbe):
        if self._farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self._farbe = self._farbe

class Fahrrad(Fahrzeug):
    def __init__(self, gänge):
        self._gang = 1
        self._gänge = gänge
        self._licht_an = False
    
    def hochschalten(self):
        if self._gang > self._gänge:
            self._gang = self._gänge
            print("Maximalen Gang erreicht")
        else:
            self._gang = self._gang + 1
            print(f"du bist jetzt im {self._gang}ten Gang")
    
    def runterschalten(self):
        if self._gang <= 0:
            self._gang = 1
            print("Kleinster Gang erreicht")
        else:
            self._gang = self._gang - 1
            print(f"du bist jetzt im {self._gang}ten Gang")
            
    def licht_einschalten(self):
        if self._licht_an == False:
            self._licht_an = True
            print("Das Licht ist an")
        
    def licht_ausschalten(self):    
        if self._licht_an == True:
            self._licht_an = False
            print("Das Licht ist wieder aus")
            
                 
bike1 = Fahrrad(7)
bike1.hochschalten()
bike1.licht_einschalten()

print(bike1)


class Auto(Fahrzeug):
    def __init__(self, _farbe, max_geschwindigkeit):
        super().__init__(self, _farbe, max_geschwindigkeit)
        self._motor_läuft = False
    
    def motor_starten(self):
        print("Motor läuft")
        self.motor_läuft = True
        
    def motor_stoppen(self):
        print("Motor läuft nicht")
        self.motor_läuft = False
        self.geschwindigkeit = 0
    
    def beschleunigen(self, betrag):
        if self.motor_läuft == True:
            super().beschleunigen(self, betrag)
            
            
auto1 = Auto(Fahrzeug("blau", 230))
auto1._farbe = ("blau")
auto1.motor_starten = True
auto1.geschwindigkeit(88)

print(auto1.info)

# // Implementiere jetzt eine Klasse Auto und eine Klasse Fahrrad, die von der Klasse Fahrzeug erben.

# // Auto
# // Auto soll ein privates Attribut _motor_läuft (bool) mit dem Startwert False haben.

# // Geändert wird dieses Attribut durch die Methoden motor_starten() und motor_stoppen().

# // Die Methode beschleunigen() aus der Basisklasse Fahrzeug soll überschrieben werden, so dass das Beschleunigen nur dann einen Effekt hat, wenn _motor_läuft wahr ist.

# // Fahrrad
# // Fahrrad soll zwei private Attribute _gang und _gänge haben. _gang wird im Konstruktor auf 1 gesetzt. _gänge soll auf den übergebenen Parameter gänge gesetzt werden, und hält fest wie viele Gänge das Fahrrad besitzt.

# // Geändert wird das Attribut _gang über die Methoden hochschalten() und runterschalten(), die den aktuellen _gang jeweils um 1 erhöhen oder verringern, aber nur zwischen 1 und _gänge.

# // Außerdem soll Fahrrad ein Attribut _licht_an (bool) besitzen, welches über licht_einschalten() und licht_ausschalten() geändert wird.