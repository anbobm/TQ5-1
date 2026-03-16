datei = open("test.txt")

# inhalt = datei.read()

# print(inhalt)

count = 1
zeile = datei.readline()

while zeile != "":
    if "bar" in zeile:
        print("\"bar\" gefunden in Zeile:", count)

    zeile = datei.readline()
    count = count + 1

    

datei.close()

