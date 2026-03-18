# Aufgabe 3.1

datei = open("Kurstage/Aufgabe 3.1_2026_03_17/dates.txt", "r")
neue_datei = open("Kurstage/Aufgabe 3.1_2026_03_17/formatted_dates.txt", "w")
for zeile in datei:
    zeile = zeile.strip().removesuffix("Uhr")

    datum, uhrzeit = zeile.split()

    neue_datei.write(f"Datum: {datum}\nUhrzeit: {uhrzeit}\n\n")

datei.close()
neue_datei.close()