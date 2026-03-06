class Medium:
    def __init__(self, titel):
        self.titel = titel
        self.ist_ausgeliehen = False
        self.ausgeliehen_von = None

    def ausleihen(self, benutzer):
        self.ist_ausgeliehen = True
        self.ausgeliehen_von = benutzer

    def zurueckgeben(self):
        self.ist_ausgeliehen = False
        self.ausgeliehen_von = None


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
        return len(self.ausgeliehene_medien())
        # count = 0
        # for medium in self.medien:
        #     if medium.ist_ausgeliehen:
        #         count += 1
        # return count

    def anzahl_verfügbar(self):
        return self.anzahl_medien() - self.anzahl_ausgeliehen()
        # count = 0
        # for medium in self.medien:
        #     if not medium.ist_ausgeliehen:
        #         count += 1
        # return count

class Benutzer:
    def __init__(self, name):
        self.name = name


# Bibliothek erzeugen
bibo = Bibliothek()

# Nutzer erzeugen
benutzer1 = Benutzer("Max")

# Medien erzeugen
buch1 = Buch("Harry Potter und der Stein der Weisen", 301, "JKR")
buch2 = Buch("Harry Potter und die Kammer des Schreckens", 340, "JKR")
buch3 = Buch("Harry Potter und der Gefangene von Azkaban", 398, "JKR")
dvd1 = Dvd("Matrix", 136, "Die Wachowskis")
dvd2 = Dvd("Herr der Ringe - Rückkehr des König", 180, "Peter Jackson")

# Medien hinzufügen
bibo.hinzufuegen(buch1)
bibo.hinzufuegen(buch2)
bibo.hinzufuegen(buch3)
bibo.hinzufuegen(dvd1)
bibo.hinzufuegen(dvd2)

# Medien ausleihen
dvd2.ausleihen(benutzer1)
buch1.ausleihen(benutzer1)

# Statistikfunktionen von Bibliothek benutzen
print(f"Es gibt {bibo.anzahl_medien()} Medien")
print(f"Davon sind {bibo.anzahl_buecher()} Bücher und {bibo.anzahl_dvd()} DVDs")
print(f"{bibo.anzahl_ausgeliehen()} Medien sind ausgeliehen und {bibo.anzahl_verfügbar()} Medien sind verfügbar")

# Ausgeliehene Medien auflisten
ausgeliehen = bibo.ausgeliehene_medien()
print("Ausgeliehene Medien")
for medium in ausgeliehen:
    print(f"Medium \"{medium.titel}\" ist ausgeliehen von {medium.ausgeliehen_von.name}")