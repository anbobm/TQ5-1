# Aufgabe 1
# Gib die Zahlen von 0 bis 20 aus: 0, 1, ..., 20
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

# mit for
zahlen = range(21)

for zahl in zahlen:
    print(zahl)

# # mit while
zahl = 0

while zahl <= 20:
    print(zahl)
    zahl = zahl + 1

# Aufgabe 2
# Gib die Zahlen von 13 bis 25 aus: 13, 14, ... , 25
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

# for

for zahl in range(13, 26):
    print(zahl)

# while

zahl = 13

while zahl <= 25:
    print(zahl)
    zahl = zahl + 1