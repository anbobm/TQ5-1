# Aufgabe 6

class TemperaturMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = wert
        self.datum = datum
        self.uhrzeit = uhrzeit

    def __repr__(self):
        return f'TemperaturMessung({self.wert}, "{self.datum}", "{self.uhrzeit}")'


temperaturen = []

datei = open("Kurstage/Aufgabe 5_2026_03_18/temps.txt", encoding="utf-8")
zeilen = datei.read().splitlines()
datei.close()

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    wert, datum, uhrzeit = zeile.split()

    messung = TemperaturMessung(float(wert), datum, uhrzeit)
    temperaturen.append(messung)

print(temperaturen)