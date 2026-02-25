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

    def bellen(self):
        print("Wuff!")

    def ausgabe(self):
        super().ausgabe()
        print("Ich bin ein Hund")
        if self.geimpft:
            print("Ich bin geimpft")
        else:
            print("Ich bin nicht geimpft")


# katze = Katze("Max", "Mauzi", "Perser")

# katze.ausgabe()
# katze.miauen()

hund = Hund("Max", "Bello", False)

hund.ausgabe()
hund.bellen()