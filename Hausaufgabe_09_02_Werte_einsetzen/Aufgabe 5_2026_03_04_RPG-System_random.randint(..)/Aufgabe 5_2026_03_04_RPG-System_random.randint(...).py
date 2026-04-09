# Aufgabe 5_RPG-System_random_randint(...)

import random

class Charakter:

    def __init__(self, name, leben, schaden):
        self.name = name
        self.leben = leben
        self.schaden = schaden


    def angreifen(self, ziel):
        schaden = random.randint(1, self.schaden)
        print(f"{self.name} greift {ziel.name} an und verursacht {schaden} Schaden.")
        ziel.erleiden_schaden(schaden)


    def erleiden_schaden(self, schaden):
        self.leben -= schaden
        if self.leben < 0:
            self.leben = 0
        print(f"{self.name} hat noch {self.leben} Leben.")



class Magier(Charakter):

    def __init__(self, name, leben, schaden, mana):
        super().__init__(name, leben, schaden)
        self.mana = mana

    def zaubern(self, ziel):

        if self.mana >= 10:
            self.mana -= 10
            schaden = random.randint(self.schaden, self.schaden + 20)

            print(f"{self.name} zaubert auf {ziel.name} und verursacht {schaden} Schaden.")
            ziel.erleiden_schaden(schaden)

        else:
            print("Nicht genug Mana!")



class Krieger(Charakter):

    def __init__(self, name, leben, schaden, ruestung):
        super().__init__(name, leben, schaden)
        self.ruestung = ruestung

    def angreifen(self, ziel):

        schaden = random.randint(self.schaden, self.schaden + 10)

        print(f"{self.name} schlägt {ziel.name} und verursacht {schaden} Schaden.")
        ziel.erleiden_schaden(schaden)

    def erleiden_schaden(self, schaden):

        schaden = schaden - self.ruestung

        if schaden < 0:
            schaden = 0

        self.leben -= schaden

        print(f"{self.name} blockt mit Rüstung. Schaden: {schaden}")
        print(f"{self.name} hat noch {self.leben} Leben.")



# Test

magier = Magier("Gandalf", 100, 15, 50)
krieger = Krieger("Aragorn", 120, 20, 5)

magier.zaubern(krieger)
krieger.angreifen(magier)






    