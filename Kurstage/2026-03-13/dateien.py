# Datei zum Lesen öffnen
datei = open("foo.txt")

# inhalt = datei.read()

# print(inhalt)

# zeile1 = datei.readline()
# print("zeile 1 gelesen")
# zeile2 = datei.readline()
# print("zeile 2 gelesen")
# zeile3 = datei.readline()
# print("zeile 3 gelesen")

# print("foo\n")
# print(zeile2)
# print(zeile3)

import time

drei_zeichen = None

while drei_zeichen != "":
    drei_zeichen = datei.read(3)
    print(drei_zeichen)
    time.sleep(2)

datei.close()