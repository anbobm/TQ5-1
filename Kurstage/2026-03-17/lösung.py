# # Aufgabe 1

# eingabe = open("Kurstage/2026-03-17/input.txt")
# inhalt = eingabe.read()
# eingabe.close()

# ausgabe = open("Kurstage/2026-03-17/lange_wörter.txt", "w")

# wörter = inhalt.split()

# for wort in wörter:
#     if len(wort) > 5:
#         ausgabe.write(f"{wort}\n")

# ausgabe.close()

# # Alternative: zeilenweise

# eingabe = open("Kurstage/2026-03-17/input.txt")
# ausgabe = open("Kurstage/2026-03-17/lange_wörter.txt", "w")

# for zeile in eingabe:
#     wörter = zeile.split()
#     for wort in wörter:
#         if len(wort) > 5:
#             ausgabe.write(f"{wort}\n")

# eingabe.close()
# ausgabe.close()


# # Aufgabe 2 (removesuffix, doch nicht rstrip)

# eingabe = input("Gib irgendwas ein: ")

# print(eingabe.removesuffix("bar"))


# # Aufgabe 3

# datei = open("Kurstage/2026-03-17/dates.txt")
# zeilen = datei.read().splitlines()
# datei.close()

# neue_datei = open("Kurstage/2026-03-17/formatted_dates.txt", "w")

# for zeile in zeilen:
#     zeile = zeile.removesuffix("Uhr")

#     datum, uhrzeit = zeile.split()
#     neue_datei.write(f"Datum: {datum}\nUhrzeit: {uhrzeit}\n\n")

# neue_datei.close()


# Aufgabe 4

datei = open("Kurstage/2026-03-17/dates.txt")
zeilen = datei.read().splitlines()
datei.close()

neue_datei = open("Kurstage/2026-03-17/formatted_dates.txt", "w")

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    datum, uhrzeit = zeile.split()
    jahr, monat, tag = datum.split("-")
    neue_datei.write(f"Datum: {tag}.{monat}.{jahr}\nUhrzeit: {uhrzeit}\n\n")

neue_datei.close()