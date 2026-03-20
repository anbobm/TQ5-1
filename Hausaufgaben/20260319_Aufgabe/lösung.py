from dataclasses import dataclass

@dataclass
class TemperaturMessung:
    temperatur: float
    datum: str
    zeit: str

def lade_messungen(dateipfad):
    daten = []

    try:
        with open(dateipfad, "r") as f:
            for zeile in f:
                try:
                    temp, raw_datum, raw_zeit = zeile.split()

                    j, m, t = raw_datum.split("-")
                    datum = f"{t}.{m}.{j}"
                    zeit = raw_zeit.removesuffix("Uhr")

                    daten.append(TemperaturMessung(float(temp), datum, zeit))
                except ValueError:
                    print(f"Übersprungen: {zeile.strip()}")

    except FileNotFoundError:
        print("Keine Datei gefunden, starte leer.")

    return daten

def speichere_messungen(dateipfad, daten):
    with open(dateipfad, "w") as f:
        for eintrag in daten:
            t, m, j = eintrag.datum.split(".")
            datum = f"{j}-{m}-{t}"
            f.write(f"{eintrag.temperatur} {datum} {eintrag.zeit} Uhr\n")

def zeige_alle(daten):
    print("\Temperatur Messungen:")
    for idx, e in enumerate(daten):
        print(f"{idx}: {e.temperatur:.1f} °C {e.datum} {e.zeit} Uhr")

def neue_messung(daten):
    try:
        temp = float(input("Temperatur: ").replace(",", "."))
        datum = input("Datum: ").strip()
        zeit = input("Zeit: ").strip()

        if "." not in datum or ":" not in zeit:
            print("Format falsch!")
            return

        daten.append(TemperaturMessung(temp, datum, zeit))
        print("Gespeichert.")

    except ValueError:
        print("Ungültige Eingabe!")

def entferne_messung(daten):
    try:
        idx = int(input("Index: "))
        geloescht = daten.pop(idx)
        print(f"Entfernt: {geloescht.temperatur} °C")
    except (ValueError, IndexError):
        print("Fehler beim Löschen!")

def menue_anzeigen():
    print("Auswahl:")
    print("[1] Messungen anzeigen")
    print("[2] Messung hinzufügen")
    print("[3] Messung löschen")
    print("[E] Speichern und beenden")

def run():
    pfad = "TQ5-1/Kurstage/2026-03-17/temps.txt"
    daten = lade_messungen(pfad)

    while True:
        menue_anzeigen()
        auswahl = input("Wählen Sie ein Punktmenu aus: ").strip().upper()

        match auswahl:
            case "1":
                zeige_alle(daten)
            case "2":
                neue_messung(daten)
            case "3":
                entferne_messung(daten)
            case "E":
                speichere_messungen(pfad, daten)
                print("Daten gespeichert")
                break
            case _:
                print("Ungültige Auswahl!")

run()