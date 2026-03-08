# Aufgabe 1: RPG-System
# Erstelle eine Basisklasse Charakter mit:
# name
# leben
from random import randint

class Charakter:
    def __init__(self, name, leben):
        self._name = name
        self._leben = leben
        self._schaden = 10
    
    # Methode angreifen(), die z.B. 10 Schaden zurückgibt
    # def angreifen(self):
    #     print(f"{self._name} hat {self._schaden} Schaden verteilt.")
   
    # Schreibe die angreifen() Methode so um, dass sie jetzt nicht mehr den Schaden zurückgibt, sondern das angegriffene Objekt (Ziel) übergeben bekommt und dort den Schaden anrichtet.
    # Aufgabe 5
    # Angriffe sollen jetzt eine Zufallskomponente beinhalten. Es soll nicht immer der volle Schaden bewirkt werden. Benutze dazu random.randint(..).
    def angreifen(self, ziel):
        schaden = self._schaden - randint(0, 5)
                
        print(f"{self._name} greift {ziel._name} an! Es wurden {schaden} Schaden verteilt!") 
        ziel.schaden_erleiden(schaden)
    
    # Bonus
    # Baue eine Methode erleiden_schaden(schaden) ein.
    def schaden_erleiden(self, schaden):
        if self._leben < 0:
            self._leben = 0
        else:
            self._leben = self._leben - schaden
            print(f"{self._name} hat {self._schaden} Schaden erlitten und noch {self._leben} Leben übrig.")
        
    # Aufgabe 6
    # Schreibe eine Methode ist_tot() die zurückgibt ob der Charakter tot ist (keine Lebenspunkte mehr hat).
    def gestorben(self):
        if self._leben <= 0:
            return True
        else:
            return False
    
    
    # Magier - zusätzlich: mana
    # Methode zaubern() (verbraucht Mana und macht mehr Schaden)         
class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self._mana = mana
    
    def zaubern(self):
        if self._mana >= 5:
            self._mana = self._mana - 5
            faktor = random.randint(10, 25) / 100
            schaden = int(self._schaden * 2.5 * faktor)
            print(f"{self._name} hat einen Zauber auf {ziel._name} angewendet! Schaden: {schaden}, Mana übrig: {self._mana}")
            ziel.schaden_erleiden(schaden)
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

    # Aufgabe 7
    # Erstelle zwei Charaktere und lasse sie in einer Schleife gegeneinander Kämpfen, bis einer von ihnen tot ist.
char1 = Charakter("Wilbert", 100)
char2 = Charakter("Marsha", 100)
char3 = Magier("Idefix", 200, 50)
char4 = Krieger("Gary", 110, 50)
    
runde = 1

while not char3.gestorben() and not char4.gestorben():
    print(f"Runde: {runde}")
    char3.angreifen(char4)
    if char4.gestorben():
        print("char4 ist gestorben.")
        break
    char4.angreifen(char3)
    
    runde = runde + 1

    



char3.zaubern()
char3.angreifen(char4)
char3.angreifen(char4)

# magier.angreifen(krieger)
schaden = char3.angreifen(char4)
char4.schaden_erleiden(schaden)
