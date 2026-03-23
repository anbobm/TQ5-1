import csv

# datei = open("Kurstage/2026-03-17/person.csv", "w")

# personen = [
#     ["Max","Mustermann",30, "Dorfstraße 1, 01234 Dorf"],
#     ["Maxine","Musterfrau",25, "Dorfstraße 2, 01234 Dorf"],
#     ["Paul","Pausenfreu",17, "Alte Dorfstraße 23, 28471 Ypsilon"],
#     ["Ingrid","Individuell",23, "Unter den Linden 1, 10115 Berlin"],
# ]

# for person in personen:
#     vorname, nachname, alter, adresse = person
#     datei.write(f"{vorname};{nachname};{alter};{adresse}\n")

# datei.close()

datei = open("Kurstage/2026-03-17/person.csv", newline='')

for datensatz in csv.reader(datei, delimiter=";"):
    vorname, nachname, alter, adresse = datensatz

    print(f"Nachname: {vorname} {nachname}\nAlter: {alter}\nAdresse: {adresse}\n\n")