import random


class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
    
    def angreifen(self, ziel : Charakter):
        random_schaden = random.randint(1, 10)
        print(f"{self._name} greift {ziel._name} an und verursacht {random_schaden} Schaden!")     
        ziel.erleiden_schaden(random_schaden)   
    
    def erleiden_schaden(self, schaden):
        self._leben = self._leben - schaden
        if self._leben < 0:
            self._leben = 0
        else:
            print(f"{self._name} erleidet {schaden} Schaden und hat noch {self._leben} Leben übrig.")

    def ist_tod(self):
            print(f"{self._name} ist tot!")
            ist_tod = True

class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self._mana = mana

    def zaubern(self, ziel : Charakter):
        if self._mana >= 10:
            self._mana = self._mana - 10
            random_schaden = random.randint(15, 25)
            print(f"{self._name} zaubert einen Zauber auf {ziel._name} und verursacht {random_schaden} Schaden! Mana übrig: {self._mana}")
            ziel.erleiden_schaden(random_schaden)
        else:
            print("Nicht genug Mana zum Zaubern!")
            
class Krieger(Charakter):
    def __init__(self, name, leben, rüstung):
        super().__init__(name, leben)
        self._rüstung = rüstung

    def angreifen(self, ziel : Charakter):
        random_schaden = random.randint(10, 20)
        print(f"{self._name} greift {ziel._name} mit einem Schwert an und verursacht {random_schaden} Schaden!")
        ziel.erleiden_schaden(random_schaden)
        
    def erleiden_schaden(self, schaden):
        reduzierter_schaden = schaden - self._rüstung
        if reduzierter_schaden < 0:
            reduzierter_schaden = 0
            print(f"{self._name} hat die Rüstung erfolgreich eingesetzt und keinen Schaden erlitten!")
        else:
            print(f"{self._name} erleidet {reduzierter_schaden} Schaden!")
        self._leben = self._leben - reduzierter_schaden
        if self._leben < 0:
            self._leben = 0
        
ist_tod = False

Richard = Magier("Richard", 100, 50)
Gustav = Krieger("Gustav", 120, 5)

# Eigene Erweiterung

Name = input("Wie soll dein Charakter heißen? ")
Auswahl = input("Möchtest du ein Magier (1) oder ein Krieger (2) sein? ")

print("Dein Gegner ist Gustav, ein Krieger mit 120 Leben und 5 Rüstung.")

while Auswahl != "1" and Auswahl != "2":
    print("Ungültige Auswahl! Bitte wähle 1 für Magier oder 2 für Krieger.")
    Auswahl = input("Möchtest du ein Magier (1) oder ein Krieger (2) sein? ")
if Auswahl == "1":
    Spieler_Magier = Magier(Name, 100, 50)
    while ist_tod == False:
        Spieler_Magier.angreifen(Gustav)
        if Gustav._leben <= 0:
            Gustav.ist_tod()
            break
        Gustav.angreifen(Spieler_Magier)
        if Spieler_Magier._leben <= 0:
             Spieler_Magier.ist_tod()
             break
        Spieler_Magier.zaubern(Gustav)
        if Gustav._leben <= 0:
             Gustav.ist_tod()
             break
        Gustav.angreifen(Spieler_Magier)
        if Spieler_Magier._leben <= 0:
             Spieler_Magier.ist_tod()
             break
       

elif Auswahl == "2":
    Spieler_Krieger = Krieger(Name, 120, 5)
    while ist_tod == False:
        Spieler_Krieger.angreifen(Gustav)
        if Gustav._leben <= 0:
             Gustav.ist_tod()
             break
        Gustav.angreifen(Spieler_Krieger)
        if Spieler_Krieger._leben <= 0:
             Spieler_Krieger.ist_tod()
             break
    






