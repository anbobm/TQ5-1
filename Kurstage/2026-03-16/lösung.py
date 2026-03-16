datei = open("Kurstage/2026-03-16/foo.txt")

count = 1

while True:
    zeile = datei.readline()
    if zeile == "":
        break
    if zeile == "bar\n":
        print(f"bar gefunden in Zeile {count}")
        break
    count += 1

datei.close()