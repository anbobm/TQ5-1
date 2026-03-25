eingabe = input("Bitte eingeben:")

teile = eingabe.split()

operator = teile[0]
zahl1 = int(teile[1])
zahl2 = int(teile[2])

if operator == "plus":
    ergebnis = zahl1 + zahl2
elif operator == "minus":
    ergebnis = zahl1 - zahl2
elif operator == "mal":
    ergebnis = zahl1 * zahl2
elif operator == "durch":
    ergebnis = zahl1 / zahl2

print(int(ergebnis))