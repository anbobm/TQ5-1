# Aufgabe 1
# Nutze eine `while`-Schleife, um die Zahlen von 10 bis 1 auszugeben.

zahl = 10

while zahl >= 1:
    print(zahl)
    zahl = zahl - 1


# Aufgabe 2
# Berechne die Fakultät einer Zahl, die der Benutzer eingegeben hat.
# 5! = fakultät(5) = 1 * 2 * 3 * 4 * 5
# 7! = fakultät(7) = 1 * 2 * 3 * 4 * 5 * 6 * 7

# Randbemerkung:
# 1! = fakultät(1) = 1
# 0! = fakultät(0) = 1

# mit for

zahl = int(input("Zahl! "))

faktoren = range(1, zahl + 1)

produkt = 1

for faktor in faktoren:
    produkt = produkt * faktor

print(f"{zahl}! = fakultät({zahl}) = {produkt}")

# mit while

zahl = int(input("Zahl! "))
faktor = 1
produkt = 1

while faktor <= zahl:
    produkt = produkt * faktor
    faktor = faktor + 1

print(f"{zahl}! = fakultät({zahl}) = {produkt}")