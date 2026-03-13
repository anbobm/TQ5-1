# Datei zum Lesen öffnen
datei = open("Kurstage/Aufg_2026_03_13/foo.txt")

# gesamten Inhalt lesen
# inhalt = datei.read()
# print(inhalt)

# erste Zeile lesen
# zeile1 = datei.readline()
# print("zeile 1 gelesen")

# zweite Zeile lesen
# zeile2 = datei.readline()
# print("zeile 2 gelesen")

# dritte Zeile lesen
# zeile3 = datei.readline()
# print("zeile 3 gelesen")

# print("foo\n")
# print(zeile2)
# print(zeile3)

import time

drei_zeichen = None

while drei_zeichen != "":
    drei_zeichen = datei.read(3)
    print(drei_zeichen, end="")
    # time.sleep(2)

datei.close()