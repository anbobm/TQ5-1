# # Aufgabe 1
# # Der Benutzer soll nacheinander zwei Zahlen eingeben und danach einen Operator (+, -, * oder /).
# # Danach gibt das Programm das Ergebnis aus. Z.B.:
# # Zahl a? 3
# # Zahl b? 5
# # Operator? *
# # Ergebnis: 3 * 5 = 15

# zahl1 = int(input("Zahl a? "))
# zahl2 = int(input("Zahl b? "))
# operator = input("Operator? ")

# if operator == "+":
#     print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
# elif operator == "-":
#     print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
# elif operator == "*":
#     print(f"{zahl1} * {zahl2} = {zahl1 * zahl2}")
# elif operator == "/":
#     if zahl2 == 0:
#         print("Division durch Null")
#     else:
#         print(f"{zahl1} / {zahl2} = {zahl1 / zahl2}")

# # Aufgabe 2
# # Der Benutzer gibt nacheinander 3 Zahlen ein, und bekommt dann die größte von ihnen angezeigt. Z.B.:
# # Zahl a? 5
# # Zahl b? 11
# # Zahl c? 11
# # Die größte Zahl ist: 11

# a = int(input("Zahl a? "))
# b = int(input("Zahl b? "))
# c = int(input("Zahl c? "))

# if a >= b:
#     if a >= c:
#         print(f"Die größte Zahl ist {a}")
#     else:
#         print(f"Die größte Zahl ist {c}")
# else:
#     if b >= c:
#         print(f"Die größte Zahl ist {b}")
#     else:
#         print(f"Die größte Zahl ist {c}")

# Aufgabe 3
# Der Benutzer gibt eine Zahl ein. Anschließend werden alle Vielfachen von 3 (3, 6, 9, 12, 15, ...) bis einschließlich dieser Zahl aufsummiert. Wenn der Benutzer `6` eingibt, dann soll `9` ausgegeben werden, denn `3 + 6 = 9`. Wenn der Benutzer `13` eingibt, soll `30` ausgegeben werden, denn `3 + 6 + 9 + 12 = 30`. Wenn der Benutzer `53` eingibt muss das Ergebnis `459` sein weil `3 + 6 + ... + 51 = 459`.
# Löse die Aufgabe einmal mit `while` und einmal mit `for`.

#for
 
zahl = int(input("Geben Sie ein Zahl ein: "))
summe = 0
 
for iter in range(3, zahl + 1, 3):
    summe = summe + iter

print(summe)
 
#while

zahl = int(input("Geben Sie ein Zahl ein: "))
summe = 0
iter = 3

while iter <= zahl:
    summe = summe + iter
    iter = iter + 3
print(summe)