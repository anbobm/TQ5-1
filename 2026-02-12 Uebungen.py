# Aufgabe 1

# Nutze eine `while`-Schleife, um die Zahlen von 10 bis 1 auszugeben.=1:


#Lösung 1


zahl = 10

while zahl >=1:
    print(zahl)
    zahl -= 1

# # Aufgabe 2

# Berechne die Fakultät einer Zahl, die der Benutzer eingegeben hat.
# 5! = fakultät(5) = 1 * 2 * 3 * 4 * 5
# # 7! = fakultät(7) = 1 * 2 * 3 * 4 * 5 * 6 * 7

# Lösung 2
# mit WHILE
zahl = int(input("Gib eine Zahl ein: "))
fakultät = 1

i = 1
while i <= zahl:
    fakultät *= i   
    i += 1

print("Die Fakultät von", zahl, "ist:", fakultät)

# Aufgabe 3
 
#Der Benutzer soll einen Satz eingeben. Anschließend zählen wir, 
#wie viele Vokale (a, e, i, o, u) in diesem Satz vorhanden sind.

# Lösung 3

satz = input("Gib einen Satz ein: ")

vokale = "aeiouAEIOU"
anzahl = 0

for buchstabe in satz:
    if buchstabe in vokale:
        anzahl += 1

print(f"Der satz enthält {anzahl} Vokale")  

# Aufgabe 4
 
#Frage den Benutzer so lange nach einer Zahl, bis er eine 0 eingibt. 
#Anschließend gib die Summe aller Zahlen die er eingegeben hat aus. Z.B:
 
#Zahl? 34
#Zahl? 35
#Zahl? 0
#Summe = 69

# Lösung 4

summe = 0

while True:
    zahl = int(input("zahl? "))

    if zahl == 0:
        break

    summe += zahl
print(f"summe = {summe}")   


# Aufgabe 5
# Gegeben ist folgende Liste:

# liste = [2, 2, 3, 3, 1, 2, 1, 1, 3, 2, 2, 3, 1, 3, 1, 2, 3, 2, 2, 1, 2, 2, 1,
#  3, 1, 1, 2, 1, 1, 3, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 1, 2, 1, 3, 1, 2, 2, 1, 2, 3,
#  3, 2, 3, 2, 3, 3, 3, 3, 1, 2, 3, 2, 3, 1, 3, 1, 3, 3, 3, 1, 2, 1, 1, 3, 2, 1, 2, 
# 3, 2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 3, 3, 1, 1, 1, 2, 2, 1, 1, 2, 3, 3]
#Zähle mit einer Schleife, wie oft die Zahl 3 in dieser Liste vorkommt. (36 mal)

liste = [2, 2, 3, 3, 1, 2, 1, 1, 3, 2, 2, 3, 1, 3, 1, 2, 3, 2, 2, 1, 2, 
         2, 1, 3, 1, 1, 2, 1, 1, 3, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 1, 2, 
         1, 3, 1, 2, 2, 1, 2, 3, 3, 2, 3, 2, 3, 3, 3, 3, 1, 2, 3, 2, 3, 
         1, 3, 1, 3, 3, 3, 1, 2, 1, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 1, 
         2, 3, 1, 3, 3, 3, 1, 1, 1, 2, 2, 1, 1, 2, 3, 3]

anzahl = 0

for zahl in liste:
    if zahl == 3:
        anzahl += 1

print("Die Zahl 3 kommt", anzahl, "Mal vor.")
