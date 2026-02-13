# #Aufgabe 1 

zahl_a = int(input("Zahl a? "))
zahl_b = int(input("Zahl b? "))
operator = input("Operator?(*,+,-,/): ")

match operator:
    case "+":
        print(f"{zahl_a} + {zahl_b} = {zahl_a + zahl_b}")
    case "-":
        print(f"{zahl_a} - {zahl_b} = {zahl_a - zahl_b}")
    case "*":
        print(f"{zahl_a} * {zahl_b} = {zahl_a * zahl_b}")
    case "/":
        print(f"{zahl_a} / {zahl_b} = {zahl_a / zahl_b}")

# #Aufgabe 2 

max_zahl = int(input("Zahl 1? "))

for iter in range(2):
    zahl = int(input(f"Zahl {iter + 2}? "))
    if zahl > max_zahl:
        max_zahl = zahl

print(max_zahl)

#Aufgabe 3

#mit for

zahl = int(input("Geben Sie ein Zahl ein: "))
summe = 0

for iter in range(1, zahl + 1):
    if iter % 3 == 0:
        summe = summe + iter

print(summe)

#mit while

i = 1

while iter <= zahl:
    if iter % 3 == 0:
        summe += iter
    iter = iter + 1

print(summe)

