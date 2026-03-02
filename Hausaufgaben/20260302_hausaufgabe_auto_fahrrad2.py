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
            
    # Implementiere jetzt eine Klasse Auto und eine Klasse Fahrrad, 
    # die von der Klasse Fahrzeug erben.
    # Auto soll ein privates Attribut _motor_läuft (bool) mit dem Startwert False haben.
class Auto(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit):
        super().__init__(farbe, max_geschwindigkeit)
        self._motor_läuft = False
        self._geschwindigkeit = 0
    
    # Geändert wird dieses Attribut durch die Methoden motor_starten() und motor_stoppen().
    def motor_starten(self):
        print("Motor läuft")
        self._motor_läuft = True
        
    def motor_stoppen(self):
        print("Motor gestoppt")
        self._motor_läuft = False
        self._geschwindigkeit = 0
    
    # Die Methode beschleunigen() aus der Basisklasse Fahrzeug soll überschrieben werden, so dass das Beschleunigen nur dann einen Effekt hat, wenn _motor_läuft wahr ist.    
    def beschleunigen(self, betrag):
        if self._motor_läuft == True:
            super().beschleunigen()
              

# Fahrrad soll zwei private Attribute _gang und _gänge haben. _gang wird im Konstruktor auf 1 gesetzt. _gänge soll auf den übergebenen Parameter gänge gesetzt werden, und hält fest wie viele Gänge das Fahrrad besitzt.
class Fahrrad(Fahrzeug):
    def __init__(self, gänge):
        self._gänge = gänge
        self._gang = 1
        self._licht_an = False

    # Geändert wird das Attribut _gang über die Methoden hochschalten() und runterschalten(), die den aktuellen _gang jeweils um 1 erhöhen oder verringern, aber nur zwischen 1 und _gänge.
    def hochschalten(self):
        if self._gang <= self._gänge:
            self._gang = self._gang + 1
            print(f"Du bist jetzt im {self._gang}ten Gang.")
        else:
            print("So viele Gänge hat das Fahrrad nicht.")
            
    def runterschalten(self):
        if self._gang == 1:
            self._gang = 1
        else:
            self._gang = self._gang - 1
            print(f"Du bist jetzt im {self._gang}ten Gang.")
        
    # Außerdem soll Fahrrad ein Attribut _licht_an (bool) besitzen, welches über licht_einschalten() und licht_ausschalten() geändert wird.    
    def licht_einschalten(self):
        print("Licht ist an")
        self._licht_an == True
        
    def licht_ausschalten(self):      
        print("Licht ist aus")
        self._licht_an == False
        
bike1 = Fahrrad(7)
bike2 = Fahrrad(21)
bike1._gang = 3
bike2._gang = 13
bike1.hochschalten()
bike1.licht_einschalten()
bike2.runterschalten()
bike1.licht_ausschalten()

      
        
auto1 = Auto("weiß", 235)
auto2 = Auto("orange", 180)
auto1._motor_läuft == True
auto2.beschleunigen(78)


print(auto1.info())
print(auto2.info())



