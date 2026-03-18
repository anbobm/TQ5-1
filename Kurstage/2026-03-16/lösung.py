# # Hausaufgabe

# datei = open("Kurstage/2026-03-16/foo.txt")

# count = 1

# while True:
#     zeile = datei.readline()
#     if zeile == "":
#         break
#     if zeile == "bar\n":
#         print(f"bar gefunden in Zeile {count}")
#         break
#     count += 1

# datei.close()

# # Aufgabe 1

# eingabe = input("Gib einen Satz ein: ")
# wortliste = eingabe.split()
# wörter = len(wortliste)

# print(f"Der Satz hat {wörter} Wörter.")


# # Aufgabe 2

# datei = open("Kurstage/2026-03-16/foobar.txt")

# anzahl = 0
# for zeile in datei:
#     anzahl += len(zeile.split())
# print(f"Es gibt {anzahl} Wörter in der Datei")

# # Alternative 1
# # print(f"Es gibt {len(datei.read().split())} Wörter in der Datei")

# # Alternative 2
# # anzahl = 0
# # while True:
# #     zeile = datei.readline()
# #     if zeile == "":
# #         break
# #     anzahl += len(zeile.split())
# # print(f"Es gibt {anzahl} Wörter in der Datei")


# # Aufgabe 3

# datei = open("Kurstage/2026-03-16/foobar2.txt")

# anzahl = 0
# for zeile in datei:
#     anzahl += zeile.split().count("foo")
# print(f"Das Wort foo kommt {anzahl} mal in der Datei vor.")

# # # Alternative 1
# # print(f"Es gibt {datei.read().split().count("foo")} Wörter in der Datei")

# # # Alternative 2
# # anzahl = 0
# # for zeile in datei:
# #     for wort in zeile.split():
# #         if wort == "foo":
# #             anzahl += 1
# # print(f"Das Wort foo kommt {anzahl} mal in der Datei vor.")

# # Aufgabe 4

# # Datei muss mit mode = "w" geöffnet werden, sonst kommt bei write() ein Fehler,
# # da sie defaultmäßig nur mit "r", also zum lesen, geöffnet wird
# datei = open("Kurstage/2026-03-16/person.txt", "w")

# weiter = "j"
# while weiter == "j":
#     vorname = input("Vorname? ")
#     nachname = input("Nachname? ")
#     alter = input("Alter? ")
#     datei.write(f"{vorname},{nachname},{alter}\n")

#     weiter = input("Weiter? (j/n)")

# datei.close()


# Aufgabe 5

datei = open("Kurstage/2026-03-16/person.txt")

personen = []

for zeile in datei:
    vorname, nachname, alter = zeile.rstrip("\n").split(",")
    person = {
        "vorname": vorname,
        "nachname": nachname,
        "alter": alter
    }
    personen.append(person)

print(personen)

datei.close()

# personen = [
#     {"vorname": "Max", "nachname": "Mustermann", "alter": "30"},
#     {"vorname": "Maxine", "nachname": "Musterfrau", "alter": "25"},
#     ...
# ]


# datei = open("Kurstage/2026-03-16/person.txt")

# zeilen = datei.read().splitlines()

# personen = []

# for zeile in zeilen:
#     werte = zeile.split(",")
#     person = {
#         "vorname": werte[0],
#         "nachname": werte[1],
#         "alter": werte[2]
#     }
#     personen.append(person)

# print(personen)

# datei.close()