# Aufgabe 7

class TemperaturMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = wert
        self.datum = datum
        self.uhrzeit = uhrzeit

    def __repr__(self):
        return f"{self.wert} °C, {self.datum}, {self.uhrzeit} Uhr"


# ----------- Datei laden -----------

datei = open("Kurstage/Aufgabe 5_2026_03_18/temps.txt", encoding="utf-8")
zeilen = datei.read().splitlines()
datei.close()

temperaturen = []

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    temperatur, datum, uhrzeit = zeile.split()

    jahr, monat, tag = datum.split("-")
    datum = f"{tag}.{monat}.{jahr}"

    temperatur = float(temperatur)

    messung = TemperaturMessung(temperatur, datum, uhrzeit)
    temperaturen.append(messung)


# ----------- Menü -----------

while True:
    print("Was möchtest du tun?")
    print("[1] Messungen anzeigen")
    print("[2] Messung hinzufügen")
    print("[3] Messung löschen")
    print("[E] Speichern und beenden")

    eingabe = input()

    if eingabe == "1":
        for i, messung in enumerate(temperaturen):
            print(f"[{i}] {messung}")

    elif eingabe == "2":
        temperatur = float(input("Temperatur in °C: "))
        datum = input("Datum (TT.MM.JJJJ): ")
        uhrzeit = input("Uhrzeit (HH:MM): ")

        messung = TemperaturMessung(temperatur, datum, uhrzeit)
        temperaturen.append(messung)

    elif eingabe == "3":
        index = int(input("Welche Messung löschen (Index): "))
        if 0 <= index < len(temperaturen):
            temperaturen.pop(index)
        else:
            print("Ungültiger Index")

    elif eingabe.lower() == "e":
        with open("temps.txt", "w", encoding="utf-8") as datei:
            for m in temperaturen:
                datei.write(f"{temperatur} {datum} {uhrzeit}\n")
        break