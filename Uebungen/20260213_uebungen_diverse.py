# Aufgabe 1
# Der Benutzer soll nacheinander zwei Zahlen eingeben und danach einen Operator (+, -, * oder /). 
# Danach gibt das Programm das Ergebnis aus. Z.B.:
# Zahl a? 3
# Zahl b? 5
# Operator? *
# Ergebnis: 3 * 5 = 15

zahl_a = int(input("Bitte gib die erste Zahl ein "))
zahl_b = int(input("Bitte gib die zweite Zahl ein "))
operator = input("Welche Rechenmethode soll durchgeführt werden? (+, -, *, /) ")

if operator == "+":
    ergebnis = zahl_a + zahl_b
elif operator == "-":
    ergebnis = zahl_a - zahl_b
elif operator == "*":
    ergebnis = zahl_a * zahl_b
elif operator == "/":
    ergebnis = zahl_a / zahl_b

print(f"Dein Ergebnis : {zahl_a} {operator} {zahl_b} = {ergebnis}")

# Aufgabe 2
# Der Benutzer gibt nacheinander 3 Zahlen ein, und bekommt dann die größte von ihnen angezeigt. Z.B.:
# Zahl a? 5
# Zahl b? 11
# Zahl c? 11
# Die größte Zahl ist: 11
zahl_a = int(input("Bitte gib die erste Zahl ein "))
zahl_b = int(input("Bitte gib die zweite Zahl ein "))
zahl_c = int(input("Bitte gib die dritte Zahl ein "))
groesste_zahl = zahl_a
if zahl_a < zahl_b:
    groesste_zahl = zahl_b
    if zahl_b < zahl_c:
        groesste_zahl = zahl_c
elif zahl_a < zahl_c:
    groesste_zahl = zahl_c
print(f"Die größte Zahl ist: {groesste_zahl}")


# Aufgabe 3
# Der Benutzer gibt eine Zahl ein. Anschließend werden alle Vielfachen von 3 (3, 6, 9, 12, 15, ...) 
# bis einschließlich dieser Zahl aufsummiert. Wenn der Benutzer 6 eingibt, dann soll 9 ausgegeben werden, 
# denn 3 + 6 = 9. Wenn der Benutzer 13 eingibt, soll 30 ausgegeben werden, denn 3 + 6 + 9 + 12 = 30. 
# Wenn der Benutzer 53 eingibt muss der Ergebnis 459 sein weil 3 + 6 + ... + 51 = 459.
# Löse die Aufgabe einmal mit while und einmal mit for.

# Mit while
zahl = int(input("Gib eine Zahl ein: "))
summe = 0
vielfaches = 3
while vielfaches <= zahl:
    summe += vielfaches
    vielfaches += 3
print(f"Die Summe der Vielfachen von 3 bis {zahl} ist: {summe}")



# Mit for
zahl = int(input("Gib eine Zahl ein: "))
summe = 0
for vielfaches in range(3, zahl + 1, 3):
    summe += vielfaches
print(f"Die Summe der Vielfachen von 3 bis {zahl} ist: {summe}")