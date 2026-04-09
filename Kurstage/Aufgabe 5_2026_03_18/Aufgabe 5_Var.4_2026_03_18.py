# Aufgabe 5_Var.4_2026_03_18

datei = open("Kurstage/Aufgabe 5_2026_03_18/temps.txt", "r", encoding="utf-8")
zeilen = datei.read().splitlines()
datei.close()

neue_datei = open("Kurstage/Aufgabe 5_2026_03_18/formatted_temps.txt", "w", encoding="utf-8")

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    
    temperatur, datum, uhrzeit = zeile.split()
    
    # Smiley je nach Temperatur
    if float(temperatur) < 10:
        temperatur = temperatur + "🥶"
    elif float(temperatur) <= 18:
        temperatur = temperatur + "🙂"
    else:
        temperatur = temperatur + "😎"
    
    jahr, monat, tag = datum.split("-")
    
    neue_datei.write(f"Temperatur: {temperatur} °C\n")
    neue_datei.write(f"Datum: {tag}.{monat}.{jahr}\n")
    neue_datei.write(f"Uhrzeit: {uhrzeit}\n\n")

neue_datei.close()
