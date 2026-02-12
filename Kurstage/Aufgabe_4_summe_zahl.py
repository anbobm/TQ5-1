# Aufgabe 4
# Summe von Zahlen berechnen, bis 0 eingegeben wird

summe = 0

zahl = int(input("Zahl? "))

while zahl != 0:
    summe = summe + zahl
    zahl = int(input("Zahl? "))

print("Summe =", summe)