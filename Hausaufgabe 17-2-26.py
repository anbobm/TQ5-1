# Aufgabe 1
student = {}
student["Name:"] = "Alice"
student["Alter:"] = 20
student["Note:"] = "befriedigend"
print(student)

# Aufgabe 2
print(student["Note:"])

# Aufgabe 3
student["Alter:"] = "21"
print(student)

# Aufgabe 4
student["Studiengang:"] = "Biologie"
print(student)

# Aufgabe 5
for key in student:
    print(key, student[key])

# Aufgabe 6
liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]
anzahl = {}
for i in liste:
    for key in anzahl:
        if i == key:
            anzahl[key] += 1
            break
    else:        anzahl[i] = 1
print(anzahl)