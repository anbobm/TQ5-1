# Aufgabe 1

Zahl_a = int(input("Gib eine Zahl ein: "))
Zahl_b = int(input("Gib eine weitere Zahl ein: ")) 
Operator = input("Gib einen Operator ein (+, -, *, /): ")

if Operator == "+":
    Ergebnis = Zahl_a + Zahl_b
    print("Das Ergebnis ist:", Ergebnis)
elif Operator == "-":
    Ergebnis = Zahl_a - Zahl_b
    print("Das Ergebnis ist:", Ergebnis)
elif Operator == "*":
    Ergebnis = Zahl_a * Zahl_b
    print("Das Ergebnis ist:", Ergebnis)
elif Operator == "/":
    if Zahl_b != 0:
        Ergebnis = Zahl_a / Zahl_b
        print("Das Ergebnis ist:", Ergebnis)
    else:
        print("Fehler: Division durch Null ist nicht erlaubt.")
else:
        print("Fehler: Ungültiger Operator.")

    
# Aufgabe 2

Zahl_a = int(input("Gib eine Zahl ein: "))
Zahl_b = int(input("Gib eine weitere Zahl ein: "))
Zahl_c = int(input("Gib eine dritte Zahl ein: "))

if Zahl_a >= Zahl_b and Zahl_a >= Zahl_c:
    Groesste_Zahl = Zahl_a
elif Zahl_b >= Zahl_a and Zahl_b >= Zahl_c:
    Groesste_Zahl = Zahl_b
else:
    Groesste_Zahl = Zahl_c

print("Die größte Zahl ist:", Groesste_Zahl)

# Aufgabe 3

Zahl = int(input("Gib eine Zahl ein: "))
Ausgabbe = 0
for i in range(3, Zahl + 1, 3):
    Ausgabbe = Ausgabbe + i
print("Die Summe der Vielfachen von 3 ist:", Ausgabbe)
