datei = open("Kurstage/Aufgabe 2_2026_03_16/foobar.txt", "r")

text = datei.read()

woerter = text.split()

anzahl = len(woerter)

print("Anzahl der Wörter:", anzahl)

datei.close()