# Aufgabe 5
# Erstelle eine Klasse Mitarbeiter mit privaten Attributen für den Namen und das Gehalt, die der Konstruktor als Parameter erwartet.

# Methoden:
# get_gehalt() gibt das Gehalt zurück
# gehalt_erhoehen(prozent) erhöht das Gehalt um prozent. Nur positive Werte sind zugelassen.
# Erstelle nun eine Klasse Manager. Ein Manager ist ein Mitarbeiter, die Klasse Manager soll also von der Klasse Mitarbeiter erben.

# Darüber hinaus hat die Klasse Manager ein privates Attribut für den Bonus, welcher als Parameter im Konstruktor erwartet wird.

# Methoden:
# Die Methode get_gehalt() der Basisklasse wird überschrieben und berücksichtigt jetzt auch den zusätzlichen Bonus des Managers (Gehalt + Bonus).
# set_bonus(bonus) setzt den Bonus auf den Wert bonus. Negative Werte sind nicht erlaubt.

class Mitarbeiter:
    def __init__(self, name, gehalt):
        self._name = name
        self._gehalt = gehalt
        
    def get_gehalt(self):
        print(f"Das Gehalt von {self._name} beträgt: {self._gehalt} Euro.")
        
    def gehalt_erhoehen(self, prozent):
        if prozent <= 0:
            print("Nur positive Gehaltsänderung möglich")
        else:
            self._gehalt = self._gehalt * prozent
            print(f"Das Gehalt von {self._name} wurde um {prozent} Prozent erhöht und beträgt jetzt {self._gehalt/10} Euro.")
            
class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, bonus):
        super().__init__(name, gehalt)
        self._bonus = bonus
        
    def get_gehalt(self):
        super().get_gehalt + self._bonus
        print(f"Das Gehalt von {self._name} beträgt: {super().get_gehalt + self._bonus} Euro.")
    
    def set_bonus(self, bonus):
        if self._bonus < 0:
            print("Nur positive Boni möglich")
        else:
            self._bonus = bonus
            print(f"Der Bonus beträgt {self._bonus} Euro.")
            


mitarbeiter1 = Mitarbeiter("Daniel", 2300)
mitarbeiter2 = Mitarbeiter("Gregor", 3500)

print(mitarbeiter1.get_gehalt())
print(mitarbeiter2.get_gehalt())  

mitarbeiter1.gehalt_erhoehen(20)

mitarbeiter3 = Manager("Wilhelm", 6450, 0)
print(mitarbeiter3.get_gehalt())

mitarbeiter3.set_bonus(320)
print(mitarbeiter3.get_gehalt())
