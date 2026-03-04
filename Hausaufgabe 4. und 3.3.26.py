import random


class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
    
    def angreifen(self, ziel : Charakter):
        random_schaden = random.randint(1, 10)
        ziel.erleiden_schaden(random_schaden)  
        print(f"{self._name} greift {ziel._name} an und verursacht {random_schaden} Schaden!")      
    
    def erleiden_schaden(self, schaden):
        self._leben = self._leben - schaden
        if self._leben < 0:
            self._leben = 0
            self.ist_tod()
        else:
            print(f"{self._name} erleidet {schaden} Schaden und hat noch {self._leben} Leben übrig.")

    def ist_tod(self):
        if self._leben <= 0:
            print(f"{self._name} ist tot!")
        else:
            print(f"{self._name} hat noch {self._leben} Leben übrig.")

class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self._mana = mana

    def zaubern(self, ziel : Charakter):
        if self._mana >= 10:
            self._mana = self._mana - 10
            random_schaden = random.randint(15, 25)
            ziel.erleiden_schaden(random_schaden)
            print(f"{self._name} zaubert einen Zauber auf {ziel._name} und verursacht {random_schaden} Schaden! Mana übrig: {self._mana}")
        else:
            print("Nicht genug Mana zum Zaubern!")
            
class Krieger(Charakter):
    def __init__(self, name, leben, rüstung):
        super().__init__(name, leben)
        self._rüstung = rüstung

    def angreifen(self, ziel : Charakter):
        random_schaden = random.randint(10, 20)
        ziel.erleiden_schaden(random_schaden)
        print(f"{self._name} greift {ziel._name} mit einem Schwert an und verursacht {random_schaden} Schaden!")
    
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
            self.ist_tod()
        

Richard = Magier("Richard", 100, 50)
Gustav = Krieger("Gustav", 120, 5)

while Richard._leben > 0 and Gustav._leben > 0:
    Richard.angreifen(Gustav)
    if Gustav._leben <= 0:
        print("Gustav ist tot! Richard gewinnt!")
        break
    Gustav.angreifen(Richard)
    if Richard._leben <= 0:
        print("Richard ist tot! Gustav gewinnt!")
        break
    Richard.zaubern(Gustav)
    if Gustav._leben <= 0:
        print("Gustav ist tot! Richard gewinnt!")
        break
    Gustav.angreifen(Richard)
    if Richard._leben <= 0:
        print("Richard ist tot! Gustav gewinnt!")
        break
