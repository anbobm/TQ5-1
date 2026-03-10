from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def gib_laut(self):
        pass

class Hund(Tier):
    def gib_laut(self):
        print("Wuff!")

class Katze(Tier):
    def gib_laut(self):
        print("Miau!")

class Füsch(Tier):
    def gib_laut(self):
        print("Blüb!")

tiere = [Hund(), Hund(), Katze(), Füsch(), Hund()]

for tier in tiere:
    tier.gib_laut()

# Wirft Fehler, weil abstrakte Basisklasse
# tier = Tier()