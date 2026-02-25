class Fahrzeug:
    def __init__(self, kategorie, _farbe, max_geschwindigkeit):
        self.kategorie = kategorie
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
        if _farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self._farbe = _farbe
class Auto(Fahrzeug):
    def __init__(self, _motor_läuft):
        super().__init__(self, _farbe, max_geschwindigkeit)
        self._motor_läuft = False
    
    def motor_starten(self):
        print("Motor läuft")
        self.motor_läuft = True
        
    def motor_stoppen(self):
        print("Motor läuft nicht")
        self.motor_läuft = False
    
    def beschleunigen(self, betrag):
        if self.motor_starten == True:
            beschleunigen(self, betrag)
            
            
auto1 = Auto(Fahrzeug)
auto1._farbe = ("blau")
auto1.max_geschwindigkeit = 230
auto1.motorstarten = True
auto1.geschwindigkeit(88)

auto1.info()

# // Implementiere jetzt eine Klasse Auto und eine Klasse Fahrrad, die von der Klasse Fahrzeug erben.

# // Auto
# // Auto soll ein privates Attribut _motor_läuft (bool) mit dem Startwert False haben.

# // Geändert wird dieses Attribut durch die Methoden motor_starten() und motor_stoppen().

# // Die Methode beschleunigen() aus der Basisklasse Fahrzeug soll überschrieben werden, so dass das Beschleunigen nur dann einen Effekt hat, wenn _motor_läuft wahr ist.

# // Fahrrad
# // Fahrrad soll zwei private Attribute _gang und _gänge haben. _gang wird im Konstruktor auf 1 gesetzt. _gänge soll auf den übergebenen Parameter gänge gesetzt werden, und hält fest wie viele Gänge das Fahrrad besitzt.

# // Geändert wird das Attribut _gang über die Methoden hochschalten() und runterschalten(), die den aktuellen _gang jeweils um 1 erhöhen oder verringern, aber nur zwischen 1 und _gänge.

# // Außerdem soll Fahrrad ein Attribut _licht_an (bool) besitzen, welches über licht_einschalten() und licht_ausschalten() geändert wird.