# Aufgabe 1-2-3-4_(Medien_Buch_DVD)

# -------- MEDIUM --------

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


# -------- BUCH --------

class Buch(Medium):

    def __init__(self, titel, seitenzahl, autor):
        super().__init__(titel)
        self.seitenzahl = seitenzahl
        self.autor = autor


# -------- DVD --------

class Dvd(Medium):

    def __init__(self, titel, laufzeit, regisseur):
        super().__init__(titel)
        self.laufzeit = laufzeit
        self.regisseur = regisseur


# -------- BIBLIOTHEK --------

class Bibliothek:

    def __init__(self):
        self.medien = []


    def hinzufuegen(self, medium):
        self.medien.append(medium)


    def anzahl_medien(self):
        return len(self.medien)


    def anzahl_buecher(self):

        count = 0

        for medium in self.medien:
            if type(medium) == Buch:
                count += 1

        return count


    def anzahl_dvd(self):

        count = 0

        for medium in self.medien:
            if type(medium) == Dvd:
                count += 1

        return count


    def anzahl_ausgeliehen(self):

        count = 0

        for medium in self.medien:
            if medium.ausgeliehen_von is not None:
                count += 1

        return count


    def ausgeliehene_medien(self):

        ausgeliehen = []

        for medium in self.medien:
            if medium.ausgeliehen_von is not None:
                ausgeliehen.append(medium)

        return ausgeliehen


# -------- BENUTZER --------

class Benutzer:

    def __init__(self, name):
        self.name = name


# -------- TEST --------

benutzer1 = Benutzer("Max")

buch1 = Buch("Harry Potter und der Stein der Weisen", 301, "JKR")
buch2 = Buch("Harry Potter und die Kammer des Schreckens", 340, "JKR")
buch3 = Buch("Der Hobbit", 300, "Tolkien")

dvd1 = Dvd("Matrix", 136, "Die Wachowskis")
dvd2 = Dvd("Herr der Ringe - Rückkehr des Königs", 188, "Peter Jackson")


bibo = Bibliothek()

bibo.hinzufuegen(buch1)
bibo.hinzufuegen(buch2)
bibo.hinzufuegen(buch3)
bibo.hinzufuegen(dvd1)
bibo.hinzufuegen(dvd2)


print(f"Es gibt {bibo.anzahl_medien()} Medien")
print(f"Davon sind {bibo.anzahl_buecher()} Medien Bücher und {bibo.anzahl_dvd()} Medien DVDs")


buch1.ausleihen(benutzer1)
dvd2.ausleihen(benutzer1)


print("Ausgeliehene Medien")

for medium in bibo.ausgeliehene_medien():
    print(f'Medium "{medium.titel}" ist ausgeliehen von {medium.ausgeliehen_von.name}')       

