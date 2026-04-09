# Aufgabe

datei = open("Kurstage/Aufgabe 1_2026_03_17/input.txt", "r")
neu = open("output.txt", "w")

for zeile in datei:
    for wort in zeile.split():
        if len(wort) > 5:
            neu.write(wort + "\n")

datei.close()
neu.close()



