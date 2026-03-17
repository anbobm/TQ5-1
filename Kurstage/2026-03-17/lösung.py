# Aufgabe 1

eingabe = open("Kurstage/2026-03-17/input.txt")
inhalt = eingabe.read()
eingabe.close()

ausgabe = open("Kurstage/2026-03-17/lange_wörter.txt", "w")

wörter = inhalt.split()

for wort in wörter:
    if len(wort) > 5:
        ausgabe.write(f"{wort}\n")

ausgabe.close()

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