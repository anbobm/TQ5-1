# # Aufgabe 1

# #Gib die Zahlen von 0 bis 20 aus: 0, 1, ..., 20
# #Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.

#Lösung mit FOR Schleife

for i in range(21):
    print(i)

# Lösung mit WHILE Schleife

i = 0
while i <= 20:
    print(i)
    i = i + 1    


# Aufgabe 2

# Gib die Zahlen von 13 bis 25 aus: 13, 14, ... , 25
# Gib die Zahlen von 13 bis 25 aus: 13, 14, ... , 25
# Einmal mit Hilfe von `for .. in ..:` und einmal mit Hilfe von  `while`.  

# Lösung mit FOR Schleife 

for i in range(13, 26):
    print(i)


# Lösung mit While Schleife

i = 13
while i <= 25:
    print(i)
    i = i + 1

# Aufgabe 3
# Summiere alle Zahlen von 0 bis 100 auf

# Lösung mit FOR Schleife

for i in range(101):
    print(i)   

# Lösung mit WHILE Schleife
n = 0
summe = 0
while n <= 100:
    summe = summe + n
    n = n + 1
print("Summe aller Zahlen von 0 bis 100:", summe)
 

# Aufgabe 4 
# Summiere alle geraden Zahlen von 0 bis 100 auf.

# Lösung mit FOR Schleife

summe = 0
for i in range(0, 101, 2):
    summe += i
    print(summe)
     
#Lösung mit WHILE Schleife

def new_func():
    n = 0
    summe = 0
    while n <= 100:
        summe = summe + n
        n = n + 2
    print("Summe aller geraden Zahlen von 0 bis 100:", summe)

new_func()
