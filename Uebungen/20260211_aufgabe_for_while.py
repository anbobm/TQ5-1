# Aufgabe 1
# Gib die Zahlen von 0 bis 20 aus: 0, 1, ..., 20
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

# while
print("Aufgabe 1 mit while: Gib die Zahen von 0 bis 20 aus. ")
n = 0
while n <= 20:
    print(n)
    n = n + 1
    
# for
print("")
print("Aufgabe 1 mit for: Gib die Zahen von 0 bis 20 aus. ")
for zahl in range(21):
    print(zahl)



# Aufgabe 2
# Gib die Zahlen von 13 bis 25 aus: 13, 14, ... , 25
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

# while
print("")
print("Aufgabe 2 mit while: Gib die Zahen von 13 bis 25 aus.")
n = 13
while n <= 25:
    print(n)
    n = n + 1
    
    
# for
print("")
print("Aufgabe 2 mit for: Gib die Zahen von 13 bis 25 aus. ")
for zahl in range(13, 26):
    print(zahl)
print("Wie du siehst, siehst du nüscht!")



# Aufgabe 3
# Summiere alle Zahlen von 0 bis 100 auf.

# while
print("")
print("Aufgabe 3 mit while: Summe aller Zahlen von 0 bis 100.")
n=0
summe = 0
while n <= 100:
    summe = summe + n
    n = n + 1
print("Summe aller Zahlen von 0 bis 100:", summe)


# for
print("")
print("Aufgabe 3 mit for: Summe aller Zahlen von 0 bis 100.")
summe = 0
for n in range(101):
    summe = summe + n
print("Summe aller Zahlen von 0 bis 100:", summe)



# Aufgabe 4
# Summiere alle geraden Zahlen von 0 bis 100 auf.

# while
print("")
print("Aufgabe 4 mit while: Summe aller geraden Zahlen von 0 bis 100.")
n = 0
summe = 0
while n <= 100:
    if n % 2 == 0:
        summe = summe + n
    n = n + 1
print("Summe aller geraden Zahlen von 0 bis 100:", summe)

# for
print("")
print("Aufgabe 4 mit for: Summe aller geraden Zahlen von 0 bis 100.")
summe = 0
for n in range(101):
    if n % 2 == 0:
        summe = summe + n
print("Summe aller geraden Zahlen von 0 bis 100:", summe)