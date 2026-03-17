# Aufgabe 4

# Datei muss mit mode = "w" geöffnet werden, sonst kommt bei write() ein Fehler,
# da sie defaultmäßig nur mit "r", also zum Lesen, geöffnet wird

datei = open("Kurstage/Aufgabe 4_2026_03_16/person.txt", "w")
weiter = "j"

while weiter == "j":
    vorname = input("Vorname? ")
    nachname = input("Nachname? ")
    alter = input("Alter? ")

    datei.write(f"{vorname},{nachname},{alter}")

    weiter = input("Weiter? (j/n)")

datei.close()