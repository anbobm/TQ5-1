# Aufgabe 1: RPG-System
# Erstelle eine Basisklasse Charakter mit:
# name
# leben

class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
        self._schaden = 10
    
    # Methode angreifen(), die z.B. 10 Schaden zurückgibt
    def angreifen(self):
        print(f"{self._name} hat {self._schaden} Schaden verteilt.")
   
    # Magier - zusätzlich: mana
    # Methode zaubern() (verbraucht Mana und macht mehr Schaden)         
class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self._mana = mana
    
    def zaubern(self):
        if self._mana >= 5:
            self._mana = self._mana - 5
            schaden = self._schaden * 2.5
            print(f"{self._name} hat einen Zauber angewendet! Schaden: {self._schaden}, Mana übrig: {self._mana}")
            return schaden
        else:
            print(f"Nicht genug Mana {self._name}!")
            return 0
      
    # Krieger - zusätzlich: ruestung
    # Überschreibt angreifen() (mehr Schaden)  
class Krieger(Charakter):
    def __init__(self, name, leben, ruestung):
        super().__init__(name, leben)
        self._ruestung = ruestung
        
    def angreifen(self):
        schaden = self._schaden + 5
        print(f"{self._name} hat {schaden} Schaden verteilt.")


    
char1 = Charakter("Wilbert", 100)
char2 = Charakter("Marsha", 100)
char3 = Magier("Idefix", 200, 50)
char4 = Krieger("Gary", 110, 50)

char1.angreifen()
char3.zaubern()
char4.angreifen()