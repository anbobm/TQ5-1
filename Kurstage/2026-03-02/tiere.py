class Tier:
    def gib_laut(self):
        print("Tiergeräusch!")

class Hund(Tier):
    def gib_laut(self):
        print("Wuff!")

class Katze(Tier):
    pass

class Füsch(Tier):
    def gib_laut(self):
        print("Blüb!")

tiere = [Hund(), Hund(), Katze(), Füsch(), Hund()]

for tier in tiere:
    tier.gib_laut()