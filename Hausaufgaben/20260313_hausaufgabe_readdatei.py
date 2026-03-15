datei = open("test.txt")

# inhalt = datei.read()

# print(inhalt)

zeilennummer = 1
zeile = datei.readline()

while zeile != "":
    if "bar" in zeile:
        print("\"bar\" gefunden in Zeile:", zeilennummer)

    zeile = datei.readline()
    zeilennummer = zeilennummer + 1

    

datei.close()

