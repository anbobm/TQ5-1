class Haustier:
    def __init__(self, besitzer, name):
        self.besitzer = besitzer
        self.name = name
    
    def ausgabe(self):
        print(f"Ich bin das Haustier namens {self.name} und gehöre {self.besitzer}")

class Katze(Haustier):
    def __init__(self, besitzer, name, rasse):
        super().__init__(besitzer, name)
        self.rasse = rasse

    def miauen(self):
        print("Miau!")

    def ausgabe(self):
        super().ausgabe()
        print(f"Ich bin eine Katze")
        print(f"Meine Rasse ist {self.rasse}")

class Hund(Haustier):
    def __init__(self, besitzer, name, geimpft):
        super().__init__(besitzer, name)
        self.geimpft = False
    
    def set_impfen(self, geimpft):
        geimpft = True
        self.geimpft = geimpft

    def bellen(self):
        print("Wuff!")

    def ausgabe(self):
        istGeimpft = ""
        if self.geimpft == True:
            istGeimpft = "Geimpft"
        else:
            istGeimpft = "nicht geimpft"
        super().ausgabe()
        print(f"Ich bin ein Hund")
        print(f"Mein Besitzer ist {self.besitzer} und mein Name ist {self.name} und ich bin {istGeimpft}.")
    
hund1 = Hund("Frank", "Ben", False)

print(hund1.ausgabe())