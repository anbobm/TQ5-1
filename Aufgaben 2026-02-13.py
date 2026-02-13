# Aufgabe 1
# Der Benutzer soll nacheinander zwei Zahlen eingeben 
# und danach einen Operator (+, -, * oder /). 
# Danach gibt das Programm das Ergebnis aus. Z.B.:

# Zahl a? 3
# Zahl b? 5
# Operator? *
# Ergebnis: 3 * 5 = 15

# Lösung 1 

a = int(input("zahl a? "))
b = int(input("zahl b? "))
op = input("Operator? ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)   
else:
    print("Ungültiger Operator")

# # Aufgabe 2
# # Der Benutzer gibt nacheinander 3 Zahlen ein,
# #  und bekommt dann die größte von ihnen angezeigt. Z.B.:

# # Zahl a? 5
# # Zahl b? 11
# # Zahl c? 11
# # Die größte Zahl ist: 11

# # Lösung 2 

a = int(input("Zahl a? "))
b = int(input("Zahl b? "))
c = int(input("Zahl c? "))

groesste = a
if b > groesste:
    groesste = b
if c > groesste:
    groesste = c
print("Die größte Zahl ist:", groesste)


# # Aufgabe 3
# # Der Benutzer gibt eine Zahl ein. Anschließend 
# # werden alle Vielfachen von 3 (3, 6, 9, 12, 15, ...) 
# # bis einschließlich dieser Zahl aufsummiert. 
# # Wenn der Benutzer 6 eingibt, dann soll 9 ausgegeben werden,
# # denn 3 + 6 = 9. Wenn der Benutzer 13 eingibt, 
# # soll 30 ausgegeben werden, denn 3 + 6 + 9 + 12 = 30. 
# # Wenn der Benutzer 53 eingibt muss der Ergebnis 459 sein 
# # weil 3 + 6 + ... + 51 = 459.

# # Löse die Aufgabe einmal mit while und einmal mit for.

# # Lösung 3 WHILE

zahl = int(input("Zahl? "))
summe = 0
i = 3
while i <= zahl:
    summe += i
    i += 3
print(summe)


# #  Lösung mit FOR

zahl = int(input("Zahl? "))
summe = 0
for i in range(3, zahl + 1, 3):
    summe += i
print(summe)

