# Aufgabe(Medium_Buch_DVD)

class Medium:

    def __init__(self, titel):
        self.titel = titel
        self.ausgeliehen = False

    def ausleihen(self):
        self.ausgeliehen = True

    def zurueckgeben(self):
        self.ausgeliehen = False


class Buch(Medium):

    def __init__(self, titel, seitenzahl, autor):
        super().__init__(titel)
        self.seitenzahl = seitenzahl
        self.autor = autor


class Dvd(Medium):

    def __init__(self, titel, laufzeit, regisseur):
        super().__init__(titel)
        self.laufzeit = laufzeit
        self.regisseur = regisseur


class Bibliothek:

    def __init__(self):
        self.medien = []

    def ausgeliehene_medien(self):
        ausgeliehene = []

        for medium in self.medien:
            if medium.ausgeliehen:
                ausgeliehene.append(medium)

        return ausgeliehene


# ----- TEST ----
if __name__ == "__main__":

    buch1 = Buch("Der Hobbit", 300, "Tolkien")
    dvd1 = Dvd("Matrix", 120, "Wachowski")

    bibliothek = Bibliothek()
bibliothek.medien.append(buch1)
bibliothek.medien.append(dvd1)

buch1.ausleihen()

for medium in bibliothek.ausgeliehene_medien():
    print(medium.titel)


