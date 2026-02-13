# Aufgabe 1
# Der Benutzer soll eine Zahl eingeben. Anschließend werden die Vielfachen dieser Zahl ausgegeben. Z.B.: Wenn der Nutzer `5` eingegeben hat, soll die Ausgabe so aussehen:
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 9 x 5 = 45
# 10 x 5 = 50

gewuerfelt = int(input("Gib Zahl! "))

for i in range(1, 11):
    print(f"{i} x {gewuerfelt} = {i * gewuerfelt}")
    # Alternative:
    # print(i, "x", zahl, "=", i * zahl)
    # Alternative:
    # print(str(i) + " x " + str(zahl) + " = " + str(i * zahl))


# Aufgabe 2

# Schreibe ein Python-Skript, welches eine Zahl zwischen 1 und 10 würfelt. Anschließend soll der Benutzer diese Zahl raten. Das Skript wird erst beendet, wenn der Benutzer richtig geraten hat.

from random import randint

gewuerfelt = randint(1, 10)

geraten = int(input("Welche Zahl hab ich gewürfelt? "))

while gewuerfelt != geraten:
    print("Falsch geraten!")
    geraten = int(input("Welche Zahl hab ich gewürfelt? "))

print("Du hast richtig geraten")

# Aufgabe 3

# Wie Aufgabe 2, allerdings soll dem Nutzer nach dem Raten mitgeteilt werden, ob er zu hoch oder zu niedrig geraten hat.

from random import randint

gewuerfelt = randint(1, 10)

geraten = 0

while gewuerfelt != geraten:
    geraten = int(input("Welche Zahl hab ich gewürfelt? "))
    if geraten < gewuerfelt:
        print("Du hast zu tief geraten")
    if geraten > gewuerfelt:
        print("Du hast zu hoch geraten")

print("Du hast richtig geraten")

# Zusatz:
# Nachdem der Benutzer richtig geraten hat wird er gefragt, ob er noch einmal spielen möchte. Falls ja wird das ganze wiederholt, ansonsten das Skript beendet.

from random import randint

eingabe = ''

while eingabe != 'j':
    gewuerfelt = randint(1, 10)

    geraten = 0

    while gewuerfelt != geraten:
        geraten = int(input("Welche Zahl hab ich gewürfelt? "))
        if geraten < gewuerfelt:
            print("Du hast zu tief geraten")
        if geraten > gewuerfelt:
            print("Du hast zu hoch geraten")

    print("Du hast richtig geraten")

    eingabe = input("Beenden? (j/n) ")