class Haustier:
    def init(self, besitzer, name):
        self.besitzer = besitzer
        self.name = name

    def ausgabe(self):
        print(f"Ich bin das Haustier namens {self.name} und gehöre {self.besitzer}")


class Katze(Haustier):
    def __init__(self, besitzer, name, rasse):
        super().init(besitzer, name)
        self.rasse = rasse

    def miauen(self):
        print("Miau!")

    def ausgabe(self):
        super().ausgabe()
        print("Ich bin eine Katze")
        print(f"Meine Rasse ist {self.rasse}")


class Hund(Haustier):
    def __init__(self, besitzer, name, geimpft):
        super().init(besitzer, name)
        self.geimpft = geimpft

    def bellen(self):
        print("Wuff!")

    def ausgabe(self):
        super().ausgabe()
        print("Ich bin ein Hund")
        if self.geimpft:
            print("Der Hund ist geimpft")
        else:
            print("Der Hund ist nicht geimpft")


# Objekte erstellen
katze = Katze("Max", "Mauzi", "Perser")
hund = Hund("Anna", "Bello", True)

# Methoden aufrufen
katze.ausgabe()
katze.miauen()

print()

hund.ausgabe()
hund.bellen()