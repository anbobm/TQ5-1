# Aufgabe 5

personen = []

with open("Kurstage/Aufgabe 5_2026_03_17/person.txt", "r") as datei:
    for zeile in datei:
        daten = zeile.strip().split(",")

        person = {
            "vorname": daten[0],
            "nachname": daten[1],
            "alter": daten[2]
        }

        personen.append(person)

print(personen)