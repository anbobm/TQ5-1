# Aufgabe 1
# Lege ein *Dictionary* `student` mit folgenden Schlüssel-Wert-Paaren (key-value-pairs) an:
# * Name: Alice
# * Alter: 20
# * Note: befriedigend
# Gib das Dictionary aus: `print(student)`

student = {
    "name": "Alice",
    "alter": 20,
    "note": "befriedigend"
}

print(student)

# Aufgabe 2
# Gib nur den Wert der zum Schlüssel `Note` gehört aus.

print(student["note"])

# Aufgabe 3
# Ändere das Alter zu 21.

student["alter"] = 21
print(student)

# Aufgabe 4
# Füge einen neuen Schlüssel `Studiengang` mit dem Wert `Biologie` hinzu.

student["studiengang"] = "Biologie"
print(student)

# Aufgabe 5
# Gib mit einer `for`-Schleife alle Werte im Dictionary `student` aus.

for schlüssel in student:
    wert = student[schlüssel]
    print(wert)

# Aufgabe 6
# Gegeben ist
# liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]
# Benutze ein Dictionary um zu Zählen, wie oft jede Zahl in dieser Liste vorkommt (Schlüssel ist die Zahl, Wert ist die Anzahl).

liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]

häufigkeiten = {}

for zahl in liste:
    if zahl in häufigkeiten:
        häufigkeiten[zahl] = häufigkeiten[zahl] + 1
    else:
        häufigkeiten[zahl] = 1

print(häufigkeiten)