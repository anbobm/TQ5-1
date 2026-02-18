# Aufgabe 1
# Lege ein Dictionary student mit folgenden Schlüssel-Wert-Paaren (key-value-pairs) an:

# Name: Alice
# Alter: 20
# Note: befriedigend
# Gib das Dictionary aus: print(student)

student = {
    "Name": "Alice",
    "Alter": 20,
    "Note": "befriedigend"
}
print(student)



# Aufgabe 2
# Gib nur den Wert der zum Schlüssel Note gehört aus.
print(student["Note"])



# Aufgabe 3
# Ändere das Alter zu 21.
student["Alter"] = 21



# Aufgabe 4
# Füge einen neuen Schlüssel Studiengang mit dem Wert Biologie hinzu.
student["Studiengang"] = "Biologie"
print(student)



# Aufgabe 5
# Gib mit einer for-Schleife alle Werte im Dictionary student aus.
for i in student:
    print(student[i])


# Aufgabe 6
# Gegeben ist

# liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]
# Benutze ein Dictionary um zu Zählen, wie oft jede Zahl in dieser Liste vorkommt (Schlüssel ist die Zahl, Wert ist die Anzahl).
liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]
zaehler = {}

for i in liste:
    if i in zaehler:
        zaehler[i] = zaehler[i] + 1
    else:
        zaehler[i] = 1
print(zaehler)