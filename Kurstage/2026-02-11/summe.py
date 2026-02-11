# Aufgabe 3
 
# Summiere alle Zahlen von 0 bis 100 auf.

# mit for
summe = 0

for zahl in range(101):
    summe = summe + zahl

print(summe)

# mit while
summe = 0
zahl = 0

while zahl <= 100:
    summe = summe + zahl
    zahl += 1

print(summe)