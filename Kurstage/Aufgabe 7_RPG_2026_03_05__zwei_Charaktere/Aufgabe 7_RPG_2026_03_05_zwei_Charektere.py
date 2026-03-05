# Aufgabe 7_RPG_zwei_Charaktere

from random import randint


class Charakter:

    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
        self._schaden = 10

    def angreifen(self, ziel):

        schaden = self._schaden - randint(0, int(self._schaden * 0.5))

        print(f"{self._name} hat {schaden} Schaden verteilt.")

        ziel.erleiden_schaden(schaden)

    def erleiden_schaden(self, schaden):

        self._leben -= schaden

        if self._leben < 0:
            self._leben = 0

        print(f"{self._name} hat {schaden} Schaden erlitten und jetzt noch {self._leben} Leben")

    def ist_tot(self):

        return self._leben <= 0


class Magier(Charakter):

    def __init__(self, name, leben, mana):

        super().__init__(name, leben)

        self._mana = mana

    def zaubern(self, ziel):

        if self._mana >= 5:

            self._mana -= 5

            schaden = self._schaden + randint(5, 15)

            print(f"{self._name} zaubert auf {ziel._name} und verursacht {schaden} Schaden")

            ziel.erleiden_schaden(schaden)

        else:

            print(f"{self._name} hat nicht genug Mana")


class Krieger(Charakter):

    def __init__(self, name, leben, ruestung):

        super().__init__(name, leben)

        self._ruestung = ruestung

    def erleiden_schaden(self, schaden):

        schaden = schaden - self._ruestung

        if schaden < 0:
            schaden = 0

        self._leben -= schaden

        if self._leben < 0:
            self._leben = 0

        print(f"{self._name} blockt mit Rüstung. Schaden reduziert auf {schaden}. Leben: {self._leben}")


# Aufgabe 7


magier = Magier("Gandalf", 100, 50)
krieger = Krieger("Aragorn", 120, 3)

print("Der Kampf beginnt!")
print("-------------------")

runde = 1

while not magier.ist_tot() and not krieger.ist_tot():

    print(f"Runde: {runde}")

    magier.zaubern(krieger)

    if krieger.ist_tot():
        print(f"{krieger._name} ist tot!")
        break

    krieger.angreifen(magier)

    if magier.ist_tot():
        print(f"{magier._name} ist tot!")
        break

    runde += 1

    print("Der Kampf ist beendet!")


