# Aufgabe 1
# Der Benutzer soll eine Zahl eingeben. Anschließend werden die Vielfachen dieser Zahl ausgegeben. 
# Z.B.: Wenn der Nutzer 5 eingegeben hat, soll die Ausgabe so aussehen:

# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 9 x 5 = 45
# 10 x 5 = 50

def multipliziere(zahl):
    for i in range(1, 11):
        print(f"{i} x {zahl} = {i * zahl}")
        
zahl = int(input("Geben Sie eine Zahl ein: "))
multipliziere(zahl)




# Aufgabe 2
# Schreibe ein Python-Skript, welches eine Zahl zwischen 1 und 10 würfelt. 
# Anschließend soll der Benutzer diese Zahl raten. Das Skript wird erst beendet, wenn der Benutzer richtig geraten hat.
from random import randint

gewuerfelte_zahl = randint(1, 10)

while gewuerfelte_zahl != int(input("Gib deinen Tip ab: ")):
    print("Falsch geraten, versuche es erneut!")
print("Gut geraten!")
    


# Aufgabe 3
# Wie Aufgabe 2, allerdings soll dem Nutzer nach dem Raten mitgeteilt werden, ob er zu hoch oder zu niedrig geraten hat.
# from random import randint
# def wuerfeln():
#     return randint(1,10)
from random import randint

gewuerfelte_zahl = randint(1, 10)
rate_zahl = int(input("Gib deinen Tip ab: "))

while gewuerfelte_zahl != rate_zahl:
    print("Falsch geraten, versuche es erneut!")
    if rate_zahl < gewuerfelte_zahl:
        print("deine Zahl ist zu niedrig")
    elif rate_zahl > gewuerfelte_zahl:
        print("deine Zahl ist zu hoch")
    rate_zahl = int(input("Gib deinen Tip ab: "))
print("Gut geraten!")
    
     


# # Zusatz:
# # Nachdem der Benutzer richtig geraten hat wird er gefragt, ob er noch einmal spielen möchte. 
# # Falls ja wird das ganze wiederholt, ansonsten das Skript beendet.
from random import randint


gewuerfelte_zahl = randint(1, 10)
rate_zahl = int(input("Gib deinen Tip ab: "))

while gewuerfelte_zahl != rate_zahl:
    print("Falsch geraten, versuche es erneut!")
    if rate_zahl < gewuerfelte_zahl:
        print("deine Zahl ist zu niedrig")
    elif rate_zahl > gewuerfelte_zahl:
        print("deine Zahl ist zu hoch")
    rate_zahl = int(input("Gib deinen Tip ab: "))
print("Gut geraten!")
else:
    print("Schade, vielleicht beim nächsten Mal!")  
print("")
print("möchtest du noch eine Runde raten?")
spiel = input("J/N: ")

    
