# Aufgabe-1_Alice
# Gib das Dictionary
student = {
    "Name": "Alice",
    "Alter": 20,
    "Note": "befriedigend"
}

print(student)


# Aufgabe 2
# Gib nur wert

student = {
    "Name": "Alice",
    "Alter": 20,
    "Note": "befriedigend"
}

print(student["Note"])

# Test
# print(student)
print(student["Note"])


# Aufgabe 3 
# Aufgabe 3 (DE — условие задания)

student = {
    "Name": "Alice",
    "Alter": 20,
    "Note": "befriedigend"
}

student["Alter"] = 21

print(student)


# Aufgabe 4
# Neuen Schlüssel hinzufügen

student = {
    "Name": "Alice",
    "Alter": 20,
    "Note": "befriedigend"
}

student["Studiengang"] = "Biologie"

print(student)


# Aufgabe 5
# Alle Werte mit einer for-Schleife ausgeben

student = {
    "Name": "Alice",
    "Alter": 21,
    "Note": "befriedigend",
    "Studiengang": "Biologie"
}

for value in student.values():
    print(value)