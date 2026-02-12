# # Aufgabe 3
 
# Der Benutzer soll einen Satz eingeben. Anschließend zählen wir, wie viele Vokale (a, e, i, o, u) in diesem Satz vorhanden sind.
 
vokale = ["a","e","i","o","u"]

string = input("Geben Sie ein Satz ein: ")

count = 0

for char in string:
    if char in vokale:
        count = count + 1
    print(char)

print("Anzahl der Vokale:", count)

# # Aufgabe 4
 
# Frage den Benutzer so lange nach einer Zahl, bis er eine 0 eingibt. Anschließend gib die Summe aller Zahlen die er eingegeben hat aus. Z.B:
 
# Zahl? 34
# Zahl? 35
# Zahl? 0
# Summe = 69

summe = 0

while True:
    zahl = int(input("Zahl? "))   
    if zahl == 0:
        break  
    summe += zahl

print("Summe =", summe)
