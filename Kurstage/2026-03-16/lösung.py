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


# Aufgabe 1

eingabe = input("Gib einen Satz ein: ")
wortliste = eingabe.split()
wörter = len(wortliste)

print(f"Der Satz hat {wörter} Wörter.")
