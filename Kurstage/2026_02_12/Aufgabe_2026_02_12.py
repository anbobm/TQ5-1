# Aufgabe 1
# Nutze eine while-Schleife, um die Zahlen von 10 bis 1 auszugeben.

zahl = 10

while zahl >= 1:
    print(zahl)
    zahl = zahl - 1

# Aufgabe 2
# Berechne die Fakultät einer Zahl, die der Benutzer eingegeben hat.
# 5! = 1 * 2 * 3 * 4 * 5
# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7

zahl = int(input("Gib eine Zahl ein: "))

fakultaet = 1
i = 1

while i <= zahl:
    fakultaet = fakultaet * i
    i = i + 1

print(f"{zahl}! = {fakultaet}")


