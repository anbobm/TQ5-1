<<<<<<< HEAD
#for i in range(21):
#    print(i)

#i = 0
#while i <= 20:
#    print(i)
#    i = i + 1

#for i in range(13,26):
#    print(i)

i = 13
while i <= 25:
    print(i)
    i = i + 1

# Aufgabe 1
# Gib die Zahlen von 0 bis 20 aus: 0, 1, ..., 20
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

# mit for
zahlen = range(21)

for zahl in zahlen:
    print(zahl)

# # mit while
zahl = 0

while zahl <= 20:
    print(zahl)
    zahl = zahl + 1

# Aufgabe 2
# Gib die Zahlen von 13 bis 25 aus: 13, 14, ... , 25
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

# for

for zahl in range(13, 26):
    print(zahl)

# while

zahl = 13

while zahl <= 25:
    print(zahl)
    zahl = zahl + 1
<<<<<<< HEAD
=======

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
    zahl = zahl + 1

print(summe)

# Gauss:
# 1   +   2 +   3 +  .. +  99 + 100 = 101 * 100 / 2
# 100 +  99 +  98 +  .. +   2 +   1
# 101 + 101 + 101 +  .. + 101 + 101 = 101 * 100


# Aufgabe 4
# Summiere alle geraden Zahlen von 0 bis 100 auf.

# mit for
summe = 0

for zahl in range(101):
    if zahl % 2 == 0:
        summe = summe + zahl

# mit for aber anders

summe = 0

for zahl in range(0, 101, 2):
    summe = summe + zahl

# mit while

summe = 0
zahl = 0

while zahl <= 100:
    if zahl % 2 == 0:
        summe = summe + zahl
    zahl = zahl + 1
>>>>>>> e4e837b7382beaaebc6aa70577c49580bc2c8046
