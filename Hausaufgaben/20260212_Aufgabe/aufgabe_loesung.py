#Aufgabe 1
print("Aufgabe 1")

zahl = 10
iter = 1
step = 1

while zahl >= iter:
    print(zahl)
    zahl = zahl - step

#Aufgabe 2
print("Aufgabe 2")
zahl = int(input("Geben Sie ein Zahl ein: "))

def fakultät(zahl):
    if zahl == 1:
        return 1
    return zahl * fakultät(zahl - 1)

print(fakultät(5))

#Aufgabe 3
print("Aufgabe 3")

vokale = ["a","e","i","o","u"]

string = input("Geben Sie ein Satz ein: ")

count = 0

for char in string:
    if char in vokale:
        count = count + 1
    print(char)

print("Anzahl der Vokale:", count)

#Aufgabe 4
print("Aufgabe 4")

summe = 0

while True:
    zahl = int(input("Zahl? "))   
    if zahl == 0:
        break  
    summe += zahl

print("Summe =", summe)

#Aufgabe 5
print("Aufgabe 5")

liste = [2, 2, 3, 3, 1, 2, 1, 1, 3, 2, 2, 3, 1, 3, 1, 2, 3, 2, 2, 1, 2, 2, 1, 3, 1, 1, 2, 1, 1, 3, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 1, 2, 1, 3, 1, 2, 2, 1, 2, 3, 3, 2, 3, 2, 3, 3, 3, 3, 1, 2, 3, 2, 3, 1, 3, 1, 3, 3, 3, 1, 2, 1, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 3, 3, 1, 1, 1, 2, 2, 1, 1, 2, 3, 3]

count = 0

for n in liste:
    if n == 3:
        count = count + 1
print(count)