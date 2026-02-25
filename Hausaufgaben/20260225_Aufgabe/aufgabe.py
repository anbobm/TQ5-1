class Fahrzeug:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

    def info(self):
        print(f"Dieses Fahrzeug hat die Farbe {self._farbe} und die Maximalgeschwindigkeit {self._max_geschwindigkeit}. \nAktuelle Geschwindigkeit ist {self._geschwindigkeit}")

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
        if farbe in ["Rot", "Grün", "Blau", "Schwarz", "Weiß"]:
            self._farbe = farbe

class Auto(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit):
        super().__init__(farbe, max_geschwindigkeit)
        self._motor_läuft = False

    def motor_starten(self):
        print("Motor läuft")
        self._motor_läuft = True

    def motor_stoppen(self):
        print("Motor nicht läuft")
        self._motor_läuft = False
        self._geschwindigkeit = 0

    def beschleunigen(self, betrag):
        if self._motor_läuft:
            super().beschleunigen(betrag)

class Fahrrad(Fahrzeug):
    def __init__(self, farbe, max_geschwindigkeit, gänge):
        super().__init__(farbe, max_geschwindigkeit)
        self._gang = 1
        self._gänge = gänge
        self._licht_an = False

    def hochschalten(self):
        self._gang = self._gang + 1
        if self._gang > self._gänge:
            self._gang = self._gänge
        print(f"Gang ist {self._gang}")

    def runterschalten(self):
        self._gang = self._gang - 1
        if self._gang <= 0:
            self._gang = 1
        print(f"Gang ist {self._gang}")
    
    def licht_einschalten(self):
        print("Das Licht ist eingeschaltet")
        self._licht_an = True

    def licht_ausschalten(self):
        print("Das Licht ist ausgeschaltet")
        self._licht_an = False

def auto_menu(auto):
    while True:
        print("1. Infos anzeigen")
        print("2. Motor starten")
        print("3. Motor stoppen")
        print("4. Beschleunigen")
        print("5. Bremsen")
        print("6. Zurück")

        eingabe = int(input("Wählen Sie ein Punkt von AutoMenu aus: "))

        match eingabe:
            case 1:
                auto.info()
            case 2:
                auto.motor_starten() 
            case 3:
                auto.motor_stoppen()
            case 4:
                print("Geben Sie die Geschwindigkeit für Beschleunigung ein: ")
                betrag = int(input("Betrag: "))
                auto.beschleunigen(betrag)
                auto.info()
            case 5:
                print("Geben Sie die Geschwindigkeit für Bremsen ein: ")
                betrag = int(input("Betrag: "))
                auto.bremsen(betrag)
                auto.info()
            case 6:
                break
            
def fahrrad_menu(fahrrad):

    while True:

        print("1. Infos anzeigen")
        print("2. Hochschalten")
        print("3. Runterschalten")
        print("4. Das Licht einschalten")
        print("5. Das Licht ausschalten")
        print("6. Zurück")

        eingabe = int(input("Wählen Sie ein Punkt von FahrradMenu aus: "))

        match eingabe:
            case 1:
                fahrrad.info()
            case 2:
                fahrrad.hochschalten()
                fahrrad.beschleunigen(10)
            case 3:
                fahrrad.runterschalten()
                fahrrad.bremsen(10)
            case 4:
                fahrrad.licht_einschalten()
            case 5:
                fahrrad.licht_ausschalten()
            case 6:
                break
        
def hauptmenu_anzeigen():
    print("1. Das Auto erstellen")
    print("2. Das Fahrrad erstellen")
    print("3. Beenden")

def main():
    while True:

        hauptmenu_anzeigen()

        eingabe = int(input("Wählen Sie ein Punkt von Menu aus: "))

        match eingabe:
            case 1:
                auto = Auto("Rot", 220)
                print("Das Auto ist erstellt.")
                auto.info()
                auto_menu(auto)
            case 2:
                fahrrad = Fahrrad("Blau", 60, 6)
                print("Das Fahrrad ist erstellt.")
                fahrrad.info()
                fahrrad_menu(fahrrad)
            case 3:
                break;

main()
