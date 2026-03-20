import csv

datei = open("20260320_personen.csv", newline='', encoding="utf-8")

for datensatz in csv.reader(datei, delimiter=";"):
    vorname, nachname, alter, adresse = datensatz
    print(f"Name: {vorname} {nachname}\nALter: {alter}\nAdresse: {adresse}\n\n")