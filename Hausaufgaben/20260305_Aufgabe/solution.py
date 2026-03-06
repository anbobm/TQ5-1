class Medium:
    def __init__(self, titel, ist_ausgeliehen=False):
        self.titel = titel
        self.ist_ausgeliehen = ist_ausgeliehen
        self.ausgeliehen_von = None

    def ausleihen(self, benutzer):
        if not self.ist_ausgeliehen:
            self.ausgeliehen_von = benutzer
            self.ist_ausgeliehen = True
            print(f"{self.titel} wurde von {benutzer.name} ausgeliehen.")
            

    def zurueckgeben(self):
        if self.ist_ausgeliehen:
            print(f"{self.titel} wurde von {self.ausgeliehen_von.name} zurückgegeben.")
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

    def hinzufuegen(self, medium):
        self.medien.append(medium)

    def ausgeliehene_medien(self):
        ausgeliehene = []
        for medium in self.medien:
            if medium.ist_ausgeliehen:
                ausgeliehene.append(medium)
        return ausgeliehene
    
    def anzahl_medien(self):
        count = 0
        for media in self.medien:
            count = count + 1
        print(f"Anzahl Medien: {count}")

    def anzahl_buecher(self):
        count = 0
        for buch in self.medien:
            if isinstance(buch, Buch):
                count = count + 1
        print(f"Anzahl Buecher: {count}")

    def anzahl_dvds(self):
        count = 0
        for dvd in self.medien:
            if isinstance(dvd, Dvd):
                count = count + 1
        print(f"Anzahl Dvds: {count}")

    def anzahl_ausgeliehen(self):
        count = 0
        for medium in self.medien:
            if medium.ist_ausgeliehen:
                count = count + 1
        print(f"Anzahl ausgeliehen: {count}")

    def anzahl_verfuegbar(self):
        count = 0
        for medium in self.medien:
            if not medium.ist_ausgeliehen:
                count = count + 1
        print(f"Anzahl vefuegbar: {count}")


class Benutzer:
    def __init__(self, name):
        self.name = name

print()

benutzer_igor = Benutzer("Igor")
benutzer_anna = Benutzer("Anna")

buch_avengers_origins = Buch("Avengers Origins", 420, "Stan Lee")
buch_spider_man_story = Buch("Spider-Man: Great Responsibility", 350, "Steve Ditko")

dvd_iron_man_film = Dvd("Iron Man", 126, "Jon Favreau")
dvd_avengers_endgame_film = Dvd("Avengers: Endgame", 181, "Anthony und Joe Russo")

bibliothek_stadt = Bibliothek()

bibliothek_stadt.hinzufuegen(buch_avengers_origins)
bibliothek_stadt.hinzufuegen(buch_spider_man_story)
bibliothek_stadt.hinzufuegen(dvd_iron_man_film)
bibliothek_stadt.hinzufuegen(dvd_avengers_endgame_film)

buch_avengers_origins.ausleihen(benutzer_igor)
dvd_avengers_endgame_film.ausleihen(benutzer_anna)

print()

bibliothek_stadt.anzahl_medien()
bibliothek_stadt.anzahl_buecher()
bibliothek_stadt.anzahl_dvds()
bibliothek_stadt.anzahl_ausgeliehen()
bibliothek_stadt.anzahl_verfuegbar()

print()

print("Ausgeliehene Medien:")
for medium in bibliothek_stadt.ausgeliehene_medien():
    print(medium.titel, "-", medium.ausgeliehen_von.name)

print()

buch_avengers_origins.zurueckgeben()
dvd_avengers_endgame_film.zurueckgeben()

print()

bibliothek_stadt.anzahl_ausgeliehen()
bibliothek_stadt.anzahl_verfuegbar()