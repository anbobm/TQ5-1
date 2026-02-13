# Aufgabe 1
# Der Benutzer soll eine Zahl eingeben. 
# Anschließend werden die Vielfachen dieser Zahl ausgegeben. 
# Z.B.: Wenn der Nutzer 5 eingegeben hat, soll die Ausgabe so aussehen:

# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 9 x 5 = 45
# 10 x 5 = 50

# Lösung Aufgabe 1
zahl = int(input("Zahl eingeben: "))

for i in range(1, 11):
    print(i, "x", zahl, "=", i * zahl)


# Aufgabe 2
# Schreibe ein Python-Skript, welches eine Zahl zwischen 1 und 10 würfelt. 
# Anschließend soll der Benutzer diese Zahl raten. Das Skript wird erst beendet, 
# wenn der Benutzer richtig geraten hat.

# Lösung Aufgabe 2 
import random

geheim = random.randint(1, 10)

tipp = 0
while tipp != geheim:
    tipp = int(input("Rate die Zahl (1-10): "))

print("Richtig!")



# Aufgabe 3
# Wie Aufgabe 2, allerdings soll dem Nutzer nach dem Raten mitgeteilt werden, 
# ob er zu hoch oder zu niedrig geraten hat.

# Lösung Aufgabe 3

import random

geheim = random.randint(1, 10)

tipp = 0
while tipp != geheim:
    tipp = int(input("Rate die Zahl (1-10): "))

    if tipp < geheim:
        print("Zu niedrig")
    elif tipp > geheim:
        print("Zu hoch")

print("Richtig!")


# Zusatz:
# Nachdem der Benutzer richtig geraten hat wird er gefragt, ob er noch einmal spielen möchte. 
# Falls ja wird das ganze wiederholt, ansonsten das Skript beendet.

#Lösung

import random

weiterspielen = "ja"

while weiterspielen == "ja":
    geheim = random.randint(1, 10)
    tipp = 0

    while tipp != geheim:
        tipp = int(input("Rate die Zahl (1-10): "))

        if tipp < geheim:
            print("Zu niedrig")
        elif tipp > geheim:
            print("Zu hoch")

    print("Richtig!")

    weiterspielen = input("Nochmal? (ja/nein): ").lower()

print("Ende.")



