# Aufgabe 5

from datetime import datetime

datei = open("Kurstage/Aufgabe 5_2026_03_18/ted_temps.txt", "r") as datei:
neue_datei = open("Kurstage/Aufgabe 5_2026_03_18/formatted_temps.txt", "w", encoding="utf-8")

for zeile in datei:
    zeile = zeile.strip().removesuffix("Uhr")

    temperatur, datum_string, uhrzeit = zeile.split()

    datum = datetime.strptime(datum_string, "%Y-%m-%d")
    neues_datum = datum.strftime("%d.%m.%Y")

    neue_datei.write(
        f"Temperatur: {temperatur} \u00B0C\n"
        f"Datum: {neues_datum}\n"
        f"Uhrzeit: {uhrzeit}\n\n"
    )

datei.close()
neue_datei.close()