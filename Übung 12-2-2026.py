# Aufgabe 1
zahl = 10
while zahl >= 1:
    print(zahl)
    zahl = zahl - 1

# Aufgabe 2
faktorial = int(input("Gib eine Zahl ein: "))
multipliziert = 1

for i in range(1, faktorial + 1):
    multipliziert = multipliziert * i
    print(multipliziert)

print(multipliziert)

# Aufgabe 4
satz = input("Gib einen Satz ein: ")
Vokale = 0
for buchstabe in satz:
    if buchstabe == "a" or buchstabe == "e" or buchstabe == "i" or buchstabe == "o" or buchstabe == "u":
        Vokale = Vokale + 1
    else:
        continue

print("Der Satz enthält", Vokale, "Vokale.")

# Aufgabe 5

frage = True
Zusatz = 0
while frage == True:
    eingabe = int(input("Gib eine Zahl ein: "))
    if eingabe == 0:
        frage = False
    else:
        Zusatz = Zusatz + eingabe
        

print("Die Summe der eingegebenen Zahlen ist:", Zusatz)
