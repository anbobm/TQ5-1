# Aufgabe 2: textbasierter einfacher Taschenrechner
# Der Benutzer soll z.B. eingeben "plus 3 19", "minus 2 7", "mal 11 5" oder "durch 18 3" und das Programm soll entsprechend ausgeben 22, -5, 55 oder 6.

# Benutze split() und denk dran, dass du Strings erst in eine Zahl umwandeln musst um damit rechnen zu können.

rechnung = input("Gib eine Aufgabe ein: (plus, minus, mal oder durch und dann die Zahlen) " )

formelzeichen, a, b = rechnung.split()
a = float(a)
b = float(b)
if formelzeichen == "plus": 
    summe = a + b
    print(f"{summe}")
elif formelzeichen == "minus":
    summe = a - b
    print(f"{summe}")
elif formelzeichen == "mal":
    summe = a * b
    print(f"{summe}")
elif formelzeichen == "durch":
    summe = a / b
    print(f"{summe}")
else:
    print("Eingabe ungültig")

