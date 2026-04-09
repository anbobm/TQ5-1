# Aufgabe 1-2-3_(Medien_Buch_DVD)

class Medium:

    def __init__(self, titel):
        self.titel = titel
        self.ausgeliehen_von = None

    def ausleihen(self, benutzer):

        if self.ausgeliehen_von is None:
            self.ausgeliehen_von = benutzer
            print(f'Medium "{self.titel}" ist ausgeliehen von {benutzer.name}')
        else:
            print(f'Medium "{self.titel}" ist bereits ausgeliehen')

    def zurueckgeben(self):

        if self.ausgeliehen_von is not None:
            print(f'Medium "{self.titel}" wurde zurückgegeben')
            self.ausgeliehen_von = None
        else:
            print(f'Medium "{self.titel}" war nicht ausgeliehen')


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


class Benutzer:

    def __init__(self, name):
        self.name = name


# -------- TEST --------

benutzer1 = Benutzer("Max")
benutzer2 = Benutzer("Anna")

buch1 = Buch("Der Hobbit", 300, "Tolkien")
buch2 = Buch("Harry Potter", 500, "Rowling")

dvd1 = Dvd("Matrix", 120, "Wachowski")

buch1.ausleihen(benutzer1)
dvd1.ausleihen(benutzer2)

buch1.zurueckgeben()

buch2.ausleihen(benutzer2)




