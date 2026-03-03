class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
    
    def angreifen(self, ziel):
        ziel.erleiden_schaden(10)
    
    def erleiden_schaden(self, schaden):
        self._leben = self._leben - schaden
        if self._leben < 0:
            self._leben = 0
    
class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self._mana = mana

    def zaubern(self, ziel):
        if self._mana >= 10:
            self._mana = self._mana - 10
            ziel.erleiden_schaden(20)
        else:
            print("Nicht genug Mana zum Zaubern!")
    
    def erleiden_schaden(self, schaden):
        self._leben = self._leben - schaden
        if self._leben < 0:
            self._leben = 0
            
    
class Krieger(Charakter):
    def __init__(self, name, leben, rüstung):
        super().__init__(name, leben)
        self._rüstung = rüstung

    def angreifen(self, ziel):
        ziel.erleiden_schaden(15)
    
    def erleiden_schaden(self, schaden):
        reduzierter_schaden = schaden - self._rüstung
        if reduzierter_schaden < 0:
            reduzierter_schaden = 0
        self._leben = self._leben - reduzierter_schaden
        if self._leben < 0:
            self._leben = 0