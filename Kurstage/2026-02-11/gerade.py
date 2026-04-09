# Aufgabe 4
# Summiere alle geraden Zahlen von 0 bis 100
# mit for

summe = 0
for zahl in range(0, 101, 2):
    summe = summe + zahl
print(summe)


# Aufgabe 4
# mit while

summe = 0
zahl = 0
while zahl <= 100:
    summe = summe + zahl
    zahl += 2
print(summe)

