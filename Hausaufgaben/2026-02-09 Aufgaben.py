#Aufgabe 1
#Lege eine Variable zahl fest
#Wenn die Zahl größer oder gleich 10 ist, gib "Die Zahl ist größer oder gleich 10" auf die Kommandozeile aus.
#Ansonsten gib "Die Zahl ist kleiner als 10" aus.
#Teste das Skript für verschiedene Werte von zahl: 9, 10, 11, 1001, -1

zahl = 9
if zahl >=10:
    print("Die Zahl ist größer oder gleich 10")
else:
    print("Die Zahl ist kleiner als 10")


#Aufgabe 2
#Genau wie Aufgabe 1, aber die Variable zahl
#soll von der Kommandozeile eingelesen werden. 

zahl = int(input("Bitte gib eine Zahl ein")) 
if zahl >= 10:
    print("Die Zahl ist größer oder gleich 10")
else:
    print("Die Zahl ist kleiner als 10") 

#Aufgabe 3
#Der Benutzer soll sein Alter eingeben. Anschließend wird, falls das Alter kleiner als 18 ist "minderjährig" 
#ausgegeben, ansonsten "volljährig".

alter = int(input("Bitte dein Alter eingeben"))
if alter < 18:
    print("minderjährig")
else:
    print("volljährig)")


#Aufgabe 4
#Der Benutzer soll ein Passwort eingeben. Wenn der Benutzer
#"password123" eingegeben hat, soll ausgegeben werden 
#"Du hast das Passwort erraten!" (ansonsten passiert nichts).   

passwort = input("Bitte Passwort eingeben: ")

if passwort == "password123":
    print("Du hast das Passwort erraten")  

zahl = int(input("Bitte gib eine Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade")
else:
    print("Die Zahl ist ungerade")

def isEven(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False


zahl = int(input("Bitte gib eine Zahl ein: "))

if isEven(zahl):
    print("Die Zahl ist gerade")
else:
    print("Die Zahl ist ungerade")

 
zahl = int(input("Zahl eingeben: "))

if zahl > 0:
    print("positiv")
elif zahl < 0:
    print("negativ")
else:
    print("weder positiv noch negativ")


temperatur = int(input("Bitte gib eine Temperatur ein: "))

if temperatur < 0:
    print("Es ist eiskalt")
elif temperatur < 20:
    print("Es ist frisch")
elif temperatur < 30:
    print("Es ist warm") 
else:
    print("Es ist zu heiß")

import random

# 1. Drei Würfel werfen
w1 = random.randint(1, 6)
w2 = random.randint(1, 6)
w3 = random.randint(1, 6)

# 2. Summe berechnen
summe = w1 + w2 + w3

# 3. Ausgabe des Wurfs
print(f"Wurf: {w1} + {w2} + {w3} = {summe}")

# 4. Bonuspunkte prüfen
bonus = 0

# Dreierpasch zuerst prüfen (sonst würde Zweierpasch vorher greifen)
if w1 == w2 == w3:
    bonus = 6
    print("Dreierpasch! +6 Bonuspunkte")
# Zweierpasch prüfen
elif w1 == w2 or w1 == w3 or w2 == w3:
    bonus = 2
    print("Zweierpasch! +2 Bonuspunkte")

# 5. Bonus zur Summe addieren
gesamt = summe + bonus

print(f"Gesamtpunkte: {gesamt}")

# 6. Gewinnbedingung
if gesamt >= 15:
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")

 



