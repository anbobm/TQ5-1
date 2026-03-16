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


# Aufgabe 3

datei = open("Kurstage/2026-03-16/foobar2.txt")

anzahl = 0
for zeile in datei:
    anzahl += zeile.split().count("foo")
print(f"Das Wort foo kommt {anzahl} mal in der Datei vor.")

# # Alternative 1
# print(f"Es gibt {datei.read().split().count("foo")} Wörter in der Datei")

# # Alternative 2
# anzahl = 0
# for zeile in datei:
#     for wort in zeile.split():
#         if wort == "foo":
#             anzahl += 1
# print(f"Das Wort foo kommt {anzahl} mal in der Datei vor.")



