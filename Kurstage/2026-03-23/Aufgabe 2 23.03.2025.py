# Aufgabe 2
eingabe = input()


teile = eingabe.split()

op = teile[0]
a = int(teile[1])
b = int(teile[2])

if op == "plus":
    ergebnis = a + b
elif op == "minus":
    ergebnis = a - b
elif op == "mal":
    ergebnis = a * b
elif op == "durch":
    ergebnis = a / b
else:
    ergebnis = "Unbekannte Operation"

print(ergebnis)
