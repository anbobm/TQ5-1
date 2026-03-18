# Aufgabe 6_Varianten

# Datei einlesen

variante = 1   # или 2 или 3

class TemperaturMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = wert
        self.datum = datum
        self.uhrzeit = uhrzeit

    def __repr__(self):
        return f"TemperaturMessung({self.wert}, {self.datum}, {self.uhrzeit})"
temperaturen = []

with open("Kurstage/Aufgabe 5_2026_03_18/temps.txt", "r", encoding="utf-8") as datei:
    zeilen = datei.read().splitlines()

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    wert, datum, uhrzeit = zeile.split()
    messung = TemperaturMessung(float(wert), datum, uhrzeit)
    temperaturen.append(messung)

if variante == 1:
    print(temperaturen)

elif variante == 2:
    for t in temperaturen:
        print(t)

elif variante == 3:
    print("Wert | Datum       | Uhrzeit")
    print("-----------------------------")
    for t in temperaturen:
        print(f"{t.wert:5.1f} | {t.datum:11} | {t.uhrzeit}")

else:
    print("Falsche Variante")