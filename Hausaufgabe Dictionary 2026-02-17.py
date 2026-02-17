# Aufgabe 1
# Lege ein Dictionary student mit folgenden Schlüssel-Wert-Paaren (key-value-pairs) an:

# Name: Alice
# Alter: 20
# Note: befriedigend
# Gib das Dictionary aus: print(student)

# Lösung Aufgabe 1
student = {
    "Name": "Alice",
    "Alter": 20,
    "Note": "befriedigend"
}
print(student)


# Aufgabe 2
# Gib nur den Wert der zum Schlüssel Note gehört aus.

# Lösung Aufgabe 2

print(student["Note"])


# Aufgabe 3
# Ändere das Alter zu 21.

# Lösung Aufgabe 3

student["Alter"] = 21
print(student)


# Aufgabe 4
# Füge einen neuen Schlüssel Studiengang mit dem Wert Biologie hinzu.

# Lösung Aufgabe 4
student["Studiengang"] = "Biologie"
print(student)


# Aufgabe 5
# Gib mit einer for-Schleife alle Werte im Dictionary student aus.

# Lösung Aufgabe 5
for wert in student.values():
    print(wert) 

     
# Aufgabe 6
# Gegeben ist

# liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]
# Benutze ein Dictionary um zu Zählen, wie oft jede Zahl in dieser Liste vorkommt 
# (Schlüssel ist die Zahl, Wert ist die Anzahl).

# Lösung Aufgabe 6
liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]
zaehler = {}

for zahl in liste:
    if zahl in zaehler:
        zaehler[zahl] += 1
    else:
        zaehler[zahl] = 1

print(zaehler)
