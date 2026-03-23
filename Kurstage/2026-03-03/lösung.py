from random import randint

class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
        self._schaden = 10
        self.effekte : list[StatusEffekt] = []
    
    def angreifen(self, ziel):
        schaden = self._schaden - randint(0, int(self._schaden * 0.5))

        # Effekte können schaden beeinflussen
        for effekt in self.effekte:
            schaden = effekt.beim_angreifen(schaden)

        print(f"{self._name} hat {schaden} Schaden verteilt.")
        ziel.erleiden_schaden(schaden)
    
    def erleiden_schaden(self, schaden):
        # Effekte können erlittenen Schaden beeinflussen
        for effekt in self.effekte:
            schaden = effekt.beim_schaden_erleiden(schaden)

        self._leben -= schaden

        if self._leben < 0:
            self._leben = 0

        if self._leben == 0:
            print(f"{self._name} hat {schaden} Schaden erlitten und ist gestorben")
        else:
            print(f"{self._name} hat {schaden} Schaden erlitten und jetzt noch {self._leben} Leben übrig")

    def ist_tot(self):
        return self._leben <= 0
    
    def effekt_hinzufuegen(self, effekt):
        self.effekte.append(effekt)

    def neue_runde(self):
        verbleibende_effekte = []

        for effekt in self.effekte:
            effekt.beim_rundenstart(self)
            effekt.runde_verringern()
            if not effekt.ist_abgelaufen():
                verbleibende_effekte.append(effekt)
        
        self.effekte = verbleibende_effekte

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

class StatusEffekt:
    def __init__(self, dauer):
        self.dauer = dauer
    
    def beim_rundenstart(self, charakter):
        pass

    def beim_angreifen(self, schaden):
        return schaden
    
    def beim_schaden_erleiden(self, schaden):
        return schaden
    
    def runde_verringern(self):
        self.dauer -= 1

    def ist_abgelaufen(self):
        return self.dauer <= 0
    
class Schwäche(StatusEffekt):
    def beim_angreifen(self, schaden):
        return int(schaden * 0.9)
    
class Vergiftet(StatusEffekt):
    def beim_rundenstart(self, charakter):
        charakter._leben -= 3
        print(f"{charakter._name} ist vergiftet und verliert 3 Lebenspunkte und hat jetzt noch {charakter._leben} Lebenspunkte")

magier = Magier("Gandalf", 100, 100)
krieger = Krieger("Aragorn", 100, 0)

krieger.effekt_hinzufuegen(Vergiftet(5))

runde = 1
while not magier.ist_tot() and not krieger.ist_tot():
    print(f"Runde: {runde}")

    magier.neue_runde()
    krieger.neue_runde()

    # kämpfen
    magier.angreifen(krieger)

    if krieger.ist_tot():
        break

    krieger.angreifen(magier)

    runde += 1

