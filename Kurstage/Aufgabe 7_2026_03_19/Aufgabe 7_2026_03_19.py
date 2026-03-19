# Aufgabe 7

class TemperaturMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = wert
        self.datum = datum
        self.uhrzeit = uhrzeit

    def __repr__(self):
        return f"TemperaturMessung({self.wert}, '{self.datum}', '{self.uhrzeit}')"


def lade_datei():
    temperaturen = []

    with open("Kurstage/Aufgabe 5_2026_03_18/temps.txt", "r", encoding="utf-8") as f:
        for zeile in f:
            zeile = zeile.strip().removesuffix("Uhr")

            if zeile == "":
                continue

            wert, datum, uhrzeit = zeile.split()
            wert = float(wert)

            jahr, monat, tag = datum.split("-")
            datum = f"{tag}.{monat}.{jahr}"

            messung = TemperaturMessung(wert, datum, uhrzeit)
            temperaturen.append(messung)

    return temperaturen


def anzeigen(temperaturen):
    print("Messungen")
    for i, t in enumerate(temperaturen):
        print(f"[{i}] {t.wert} °C, {t.datum}, {t.uhrzeit} Uhr")


def hinzufügen(temperaturen):
    wert = float(input("Temperatur in °C: "))
    datum = input("Datum (TT.MM.JJJJ): ")
    uhrzeit = input("Uhrzeit (HH:MM): ")

    messung = TemperaturMessung(wert, datum, uhrzeit)
    temperaturen.append(messung)


def löschen(temperaturen):
    index = int(input("Nummer des Datensatzes: "))
    if 0 <= index < len(temperaturen):
        temperaturen.pop(index)


def speichern(temperaturen):
    with open("temps.txt", "w", encoding="utf-8") as f:
        for t in temperaturen:
            tag, monat, jahr = t.datum.split(".")
            datum = f"{jahr}-{monat}-{tag}"
            f.write(f"{t.wert} {datum} {t.uhrzeit}Uhr\n")


def main():
    temperaturen = lade_datei()

    while True:
        print()
        print("Was möchtest du tun?")
        print("[1] Messungen anzeigen")
        print("[2] Messung hinzufügen")
        print("[3] Messung löschen")
        print("[E] Speichern und beenden")

        wahl = input("Auswahl: ")

        if wahl == "1":
            anzeigen(temperaturen)

        elif wahl == "2":
            hinzufügen(temperaturen)

        elif wahl == "3":
            löschen(temperaturen)

        elif wahl.upper() == "E":
            speichern(temperaturen)
            break


main()