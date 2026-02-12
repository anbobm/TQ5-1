# Aufgabe 1
# Der Benutzer soll eine Zahl eingeben.
# Anschließend werden die Vielfachen dieser Zahl ausgegeben.
# Ausgabe von 1 bis 10

zahl = int(input("Bitte gib eine Zahl ein: "))

for i in range(1, 11):
    print(f"{i} x {zahl} = {i * zahl}")


    # Aufgabe 4
# Summe von Zahlen berechnen, bis 0 eingegeben wird

summe = 0

zahl = int(input("Zahl? "))

while zahl != 0:
    summe = summe + zahl
    zahl = int(input("Zahl? "))

print("Summe =", summe)


    # Aufgabe 2
# Das Programm würfelt eine Zahl zwischen 1 und 10.
# Der Benutzer muss die Zahl erraten.
# Das Programm endet bei richtiger Eingabe.

import random

zahl = random.randint(1, 10)
tipp = 0

while tipp != zahl:
    tipp = int(input("Rate die Zahl zwischen 1 und 10: "))

print("Richtig geraten!")   



# Aufgabe 3
# Der Benutzer soll erraten, ob die Zahl zu hoch oder zu niedrig ist.

import random

zahl = random.randint(1, 10)
tipp = 0

while tipp != zahl:
    tipp = int(input("Rate die Zahl zwischen 1 und 10: "))

    if tipp < zahl:
        print("Zu niedrig")
    elif tipp > zahl:
        print("Zu hoch")

print("Richtig geraten!")