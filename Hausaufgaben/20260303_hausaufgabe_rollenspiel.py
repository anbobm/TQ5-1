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
    # def angreifen(self):
    #     print(f"{self._name} hat {self._schaden} Schaden verteilt.")
   
    # Schreibe die angreifen() Methode so um, dass sie jetzt nicht mehr den Schaden zurückgibt, sondern das angegriffene Objekt (Ziel) übergeben bekommt und dort den Schaden anrichtet.
    
    def angreifen(self, ziel):
        print(f"{self._name} hat {self._schaden} verteilt!") 
        ziel.schaden_erleiden(self._schaden)
    
    # Bonus
    # Baue eine Methode erleiden_schaden(schaden) ein.
    def schaden_erleiden(self, schaden):
        if self._leben < 0:
            self._leben = 0
        else:
            self._leben = self._leben - schaden
            print(f"{self._name} hat {self._schaden} Schaden erlitten und noch {self._leben} Leben übrig.")
        
    
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
            print(f"{self._name} hat einen Zauber angewendet! Schaden: {schaden}, Mana übrig: {self._mana}")
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

    def schaden_erleiden(self, schaden):
        if self._ruestung >= schaden:
            reduzierter_schaden  = 0
        else:
            reduzierter_schaden = schaden - self._ruestung
            self._leben = self._leben - schaden + self._ruestung/10
            print(f"{self._name} hat {self._schaden} Schaden erlitten und noch {self._leben} Lebnen übrig.")
        super().schaden_erleiden(reduzierter_schaden)


    
char1 = Charakter("Wilbert", 100)
char2 = Charakter("Marsha", 100)
char3 = Magier("Idefix", 200, 50)
char4 = Krieger("Gary", 110, 50)


char3.zaubern()
char3.angreifen(char4)
char3.angreifen(char4)

# magier.angreifen(krieger)
schaden = char3.angreifen(char4)
char4.schaden_erleiden(schaden)
