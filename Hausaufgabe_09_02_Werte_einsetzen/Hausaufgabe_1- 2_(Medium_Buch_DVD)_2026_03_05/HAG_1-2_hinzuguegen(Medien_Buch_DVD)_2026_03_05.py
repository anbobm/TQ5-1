# Hausaufgabe 1-2_Medien_BUCH_DVD)hinzufuegen

# --- KLASS MEDIUM ---

class Medium:

    def __init__(self, titel):
        self.titel = titel
        self.ausgeliehen = False

    def ausleihen(self):
        self.ausgeliehen = True

    def zurueckgeben(self):
        self.ausgeliehen = False


# ---КLASS BUCH ---

class Buch(Medium):

    def __init__(self, titel, seitenzahl, autor):
        super().__init__(titel)
        self.seitenzahl = seitenzahl
        self.autor = autor



# --- KLASS DVD ---

class Dvd(Medium):

    def __init__(self, titel, laufzeit, regisseur):
        super().__init__(titel)
        self.laufzeit = laufzeit
        self.regisseur = regisseur


# ---KLASS BIBLIOTHEK ---
class Bibliothek:

    def __init__(self):
        self.medien = []

    #  (Aufgabe 2)
    
    def medium_hinzufuegen(self, medium):
        self.medien.append(medium)

    def ausgeliehene_medien(self):

        ausgeliehene = []

        for medium in self.medien:
            if medium.ausgeliehen:
                ausgeliehene.append(medium)

        return ausgeliehene
    


# ---------- TEST ----------

if __name__ == "__main__":

    buch1 = Buch("Der Hobbit", 300, "Tolkien")
    buch2 = Buch("Harry Potter", 500, "Rowling")

    dvd1 = Dvd("Matrix", 120, "Wachowski")
    dvd2 = Dvd("Avatar", 160, "Cameron")

    bibliothek = Bibliothek()

    # hinzufügen Media
    bibliothek.medium_hinzufuegen(buch1)
    bibliothek.medium_hinzufuegen(buch2)
    bibliothek.medium_hinzufuegen(dvd1)
    bibliothek.medium_hinzufuegen(dvd2)

    # geben Buch
    buch1.ausleihen()

    print("Ausgeliehene Medien:")

    for medium in bibliothek.ausgeliehene_medien():
        print(medium.titel)
    
    buch1 = Buch("Der Hobbit", 300, "Tolkien")
    buch2 = Buch("Harry Potter", 500, "Rowling")

    dvd1 = Dvd("Matrix", 120, "Wachowski")
    dvd2 = Dvd("Avatar", 160, "Cameron")

    bibliothek = Bibliothek()

    # hinzufügen Media
    bibliothek.medium_hinzufuegen(buch1)
    bibliothek.medium_hinzufuegen(buch2)
    bibliothek.medium_hinzufuegen(dvd1)
    bibliothek.medium_hinzufuegen(dvd2)

    # geben Buch
    buch1.ausleihen()

    print("Ausgeliehene Medien:")

    for medium in bibliothek.ausgeliehene_medien():
        print(medium.titel)
