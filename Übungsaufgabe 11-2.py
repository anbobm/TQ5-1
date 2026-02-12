# Aufgabe 1
zahlen = range(21)

for zahl in zahlen:
    print(zahl)


zahl = 0

while zahl <= 20:
    print(zahl)
    zahl = zahl + 1

# Aufgabe 2
zahlen = range(13,26)

for zahl in zahlen:
    print(zahl)

while zahl <= 25:
    print(zahl)
    zahl = zahl + 1

# Aufgabe 3
summe = 0
for zahl in range(101):
    summe = summe + zahl
print(summe)

summe = 0
zahl = 0

while zahl <= 100:
    summe = summe + zahl
    zahl = zahl + 1
print(summe)

# Aufgabe 4
summe = 0
zahlen = range(0,101,2)

for zahl in zahlen:
    summe = summe + zahl
    
print(summe)

summe = 0
zahl = 0

while zahl <= 100:
    if zahl % 2 == 0:
        summe = summe + zahl
    zahl = zahl + 1
print(summe)