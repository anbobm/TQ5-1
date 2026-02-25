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
        self.geimpft = geimpft

    def ausgabe(self):
        print(f"Besitzer: {self.besitzer}, Name: {self.name}")
        if self.geimpft:
            print("Geimpft")
        else:
            print("Nicht geimpft")

    def bellen(self):
        print("Wuff!")

hund = Hund("Max", "Bob", True)
hund.ausgabe()