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