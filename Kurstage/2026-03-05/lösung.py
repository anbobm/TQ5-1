class Medium:
    def __init__(self, titel):
        self.titel = titel
        self.ist_ausgeliehen = False

    def ausleihen(self):
        self.ist_ausgeliehen = True

    def zurueckgeben(self):
        self.ist_ausgeliehen = False


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
        ausgeliehen = []

        for medium in self.medien:
            if medium.ist_ausgeliehen:
                ausgeliehen.append(medium)
        
        return ausgeliehen
    
        # for pros
        # return [medium for medium in self.medien if medium.ist_ausgeliehen]
    
buch1 = Buch("Harry Potter und der Stein der Weisen", 301, "JKR")
buch2 = Buch("Harry Potter und die Kammer des Schreckens", 340, "JKR")

dvd1 = Dvd("Matrix", 136, "Die Wachowskis")
dvd2 = Dvd("Herr der Ringe - Rückkehr des König", 180, "Peter Jackson")

dvd2.ausleihen()
dvd2.zurueckgeben()

bibo = Bibliothek()

bibo.medien = [buch1, dvd2, buch2, dvd1]

dvd2.ausleihen()
buch1.ausleihen()

ausgeliehen = bibo.ausgeliehene_medien()

print("Ausgeliehene Medien")
for medium in ausgeliehen:
    print(medium.titel)