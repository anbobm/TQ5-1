class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
        self._schaden = 10
    
    def angreifen(self, ziel):
        print(f"{self._name} hat {self._schaden} Schaden verteilt.")
        ziel.erleiden_schaden(self._schaden)
    
    def erleiden_schaden(self, schaden):
        self._leben -= schaden

        if self._leben < 0:
            self._leben = 0

        print(f"{self._name} hat {schaden} Schaden erlitten und jetzt noch {self._leben} Leben übrig")

class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self._mana = mana

    def zaubern(self, ziel : Charakter):
        if self._mana >= 5:
            self._mana = self._mana - 5
            schaden = int(self._schaden * 2.5)
            print(f"{self._name} hat einen Zauber angewendet! Schaden: {schaden}, Mana übrig: {self._mana}")
            ziel.erleiden_schaden(schaden)
        else:
            print(f"Nicht genug Mana {self._name}!")

        # if self.mana < 10:
        #     print("Nicht genug Mana")
        #     return 0
        
        # self.mana -= 10
        # return 25

class Krieger(Charakter):
    def __init__(self, name, leben, ruestung):
        super().__init__(name, leben)
        self._ruestung = ruestung
        self._schaden = 15

    def erleiden_schaden(self, schaden):
        if self._ruestung >= schaden:
            reduzierter_schaden = 0
        else:
            reduzierter_schaden = schaden - self._ruestung

        super().erleiden_schaden(reduzierter_schaden)


magier = Magier("Gandalf", 100, 100)
krieger = Krieger("Aragorn", 100, 20)

magier.zaubern(krieger)