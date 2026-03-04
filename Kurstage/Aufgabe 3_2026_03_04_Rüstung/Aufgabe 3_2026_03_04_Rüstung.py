# Aufgabe 3_Rüstung.

# Aufgabe 1 + Aufgabe 2 + Aufgabe 3


class Charakter:

    def __init__(self, name, leben):
        self.name = name
        self.leben = leben

    def angreifen(self, ziel):
        schaden = 10
        print(self.name, "greift", ziel.name, "an und macht", schaden, "Schaden")
        ziel.erleiden_schaden(schaden)

    def erleiden_schaden(self, schaden):

        self.leben = self.leben - schaden

        if self.leben < 0:
            self.leben = 0

        print(self.name, "hat", schaden, "Schaden bekommen. Leben:", self.leben)



class Magier(Charakter):

    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self.mana = mana

    def zaubern(self, ziel):

        if self.mana >= 5:

            self.mana -= 5
            schaden = 25

            print(self.name, "zaubert und macht", schaden, "Schaden")

            ziel.erleiden_schaden(schaden)

        else:
            print("Nicht genug Mana")



class Krieger(Charakter):

    def __init__(self, name, leben, ruestung):
        super().__init__(name, leben)
        self.ruestung = ruestung


    def angreifen(self, ziel):

        schaden = 15

        print(self.name, "greift stark an und macht", schaden, "Schaden")

        ziel.erleiden_schaden(schaden)


    def erleiden_schaden(self, schaden):

        schaden = schaden - self.ruestung

        if schaden < 0:
            schaden = 0

        self.leben = self.leben - schaden

        if self.leben < 0:
            self.leben = 0

        print(self.name, "hat", schaden, "Schaden bekommen. Leben:", self.leben)


    


# Test

magier = Magier("Gandalf", 100, 20)
krieger = Krieger("Aragorn", 120, 5)

magier.angreifen(krieger)
krieger.angreifen(magier)
magier.zaubern(krieger)



