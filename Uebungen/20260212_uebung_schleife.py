# Aufgabe 1
# Nutze eine `while`-Schleife, um die Zahlen von 10 bis 1 auszugeben.
n = 11
while n > 1:
    n = n - 1
    print(n)
    

# Aufgabe 2
# Berechne die Fakultät einer Zahl, die der Benutzer eingegeben hat.
# 5! = fakultät(5) = 1 * 2 * 3 * 4 * 5
# 7! = fakultät(7) = 1 * 2 * 3 * 4 * 5 * 6 * 7
import math
zahl = int(input("Gib eine Zahl ein: "))
fakultaet = math.factorial(zahl)

print(f"Die Fakultät von {zahl} ist {fakultaet}.")


# Alternativ mit Schleife
zahl = int(input("Geben Sie eine Zahl ein: "))
fakultaet = 1
for i in range(1, zahl + 1):
    fakultaet = fakultaet * i
    
print(f"Die Fakultät von {zahl} ist {fakultaet}")



# Aufgabe 3
#Der Benutzer soll einen Satz eingeben. Anschließend zählen wir, wie viele Vokale (a, e, i, o, u) in diesem Satz vorhanden sind.
satz = input("Geben Sie einen Satz ein: ")
vokale = "aeiouAEIOU"
anzahl = 0
for buchstabe in satz:
    if buchstabe in vokale:
        anzahl += 1
print(f"Der Satz enthält {anzahl} Vokale.")


# Aufgabe 4
#Frage den Benutzer so lange nach einer Zahl, bis er eine 0 eingibt. Anschließend gib die Summe aller Zahlen die er eingegeben hat aus. Z.B:
# Zahl? 34
# Zahl? 35
# Zahl? 0
# Summe = 69
zahl = int(input("Gib eine Zahl ein: "))
summe = 0
while zahl != 0:
    summe += zahl
    zahl = int(input("Gib eine Zahl ein: "))
print(f"Summe = {summe}")