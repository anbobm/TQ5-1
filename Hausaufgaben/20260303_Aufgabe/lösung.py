import random

class Charakter:
    def __init__(self, name, leben, damage):
        self._name = name
        self._leben = leben
        self._damage = damage

    @property
    def name(self):
        return self._name

    @property
    def leben(self):
        return self._leben

    def angreifen(self):
        return self._damage

    def erleiden_schaden(self, schaden):
        self._leben -= schaden
        if self._leben < 0:
            self._leben = 0


class Magier(Charakter):
    def __init__(self, name, leben, damage, mana):
        super().__init__(name, leben, damage)
        self._mana = mana

    @property
    def mana(self):
        return self._mana

    def zaubern(self):
        if self._mana >= 10:
            self._mana -= 10
            schaden = self._damage + random.randint(10, 20)
            print(f"{self._name} benutzt Magie! (-10 Mana)")
            print(f"Mana übrig: {self._mana}")
            return schaden
        else:
            print(f"{self._name} hat nicht genug Mana!")
            return self.angreifen()


class Krieger(Charakter):
    def __init__(self, name, leben, damage, ruestung):
        super().__init__(name, leben, damage)
        self._ruestung = ruestung

    def angreifen(self):
        return self._damage + random.randint(5, 10)

    def erleiden_schaden(self, schaden):
        reduzierter_schaden = schaden - self._ruestung
        if reduzierter_schaden < 0:
            reduzierter_schaden = 0
        super().erleiden_schaden(reduzierter_schaden)


def kampf_simulation(kämpfer_1, kämpfer_2):
    print("\nKampf startet!\n")

    while kämpfer_1.leben > 0 and kämpfer_2.leben > 0:

        # kämpfer_1 
        if isinstance(kämpfer_1, Magier) and random.choice([True, False]) == True:
            schaden = kämpfer_1.zaubern()
        else:
            schaden = kämpfer_1.angreifen()

        kämpfer_2.erleiden_schaden(schaden)
        print(f"{kämpfer_1.name} macht {schaden} Schaden. {kämpfer_2.name} hat HP: {kämpfer_2.leben}")

        if kämpfer_2.leben <= 0:
            break

        # kämpfer_2
        if isinstance(kämpfer_2, Magier) and random.choice([True, False]) == True:
            schaden = kämpfer_2.zaubern()
        else:
            schaden = kämpfer_2.angreifen()

        kämpfer_1.erleiden_schaden(schaden)
        print(f"{kämpfer_2.name} macht {schaden} Schaden. {kämpfer_1.name} hat HP: {kämpfer_1.leben}")

    if kämpfer_1.leben > 0:
        print(f"\n{kämpfer_1.name} gewinnt!")
    else:
        print(f"\n{kämpfer_2.name} gewinnt!")


def display_menu():
    print("1. Kampf starten")
    print("2. Beenden")


def main():

    while True:
        display_menu()
        auswahl = input("Wähle eine Option: ")

        match auswahl:
            case "1":
                magier = Magier("Magier", 100, 15, 50)
                krieger = Krieger("Krieger", 120, 20, 5)
                kampf_simulation(magier, krieger)
            case "2":
                print("Spiel beendet.")
                break
            case _:
                print("Ungültige Eingabe!")

main()