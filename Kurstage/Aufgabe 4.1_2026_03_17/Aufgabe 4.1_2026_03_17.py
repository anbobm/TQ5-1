# Aufgabe 4.1

with open("Kurstage/Aufgabe 3.1_2026_03_17/dates.txt", "r") as f:
    lines = f.readlines()

with open("Kurstage/Aufgabe 3.1_2026_03_17/formatted_dates.txt", "w") as f:
    for line in lines:
        line = line.rstrip()
        teile = line.split()

        datum = teile[0]
        uhrzeit = teile[1].rstrip("Uhr")

        jahr, monat, tag = datum.split("-")
        neues_datum = tag + "." + monat + "." + jahr

        f.write("Datum: " + neues_datum + "\n")
        f.write("Uhrzeit: " + uhrzeit + "\n\n")