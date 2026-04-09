# Aufgabe_person.csv

import csv

personen = [
    ["Max", "Mustermann", 30, "Dorfstraße 1, 01234 Dorf"],
    ["Maxine", "Musterfrau", 25, "Dorfstraße 2, 01234 Dorf"],
    ["Paul", "Pausenfreu", 17, "Alte Dorfstraße 23, 28471 Ypsilon"],
    ["Ingrid", "Individuell", 23, "Unter den Linden 1, 10115 Berlin"],
]

datei = open("Kurstage/Aufgabe_person.csv_2026_03_20/person.csv", "w", newline='', encoding="utf-8")

for person in personen:
    vorname, nachname, alter, adresse = person
    datei.write(f'{vorname},{nachname},{alter},"{adresse}"\n')

datei.close()

datei = open("Kurstage/Aufgabe_person.csv_2026_03_20/person.csv", newline='', encoding="utf-8")

for datensatz in csv.reader(datei):
    vorname, nachname, alter, adresse = datensatz
    print(f"Nachname: {vorname} {nachname}\nAlter: {alter}\nAdresse: {adresse}\n\n")

datei.close()