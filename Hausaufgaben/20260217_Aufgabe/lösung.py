#Aufgabe 1 

student = {"name": "Alice", "Alter": 20, "Note": "befriedigend"}

 #1
print(student)

#2
for key, value in student.items():
    print(f"Key: {key}; Value: {value}")

#Aufgabe 2

print(student["Note"]) #befriedigend

#Aufgabe 3 

student["Alter"] = 21

print(student["Alter"])

#Aufgabe 4

student["Studiengang"] = "Biologie"

print(student["Studiengang"])

#Aufgabe 5

for key, value in student.items():
    print(f"Key: {key}; Value: {value}")

#Aufgabe 6

liste = [1, 5, 3, 5, 2, 1, 7, 1, 8, 4]

dictionary = {}

for item in liste:
    if item in dictionary:
        dictionary[item] = dictionary[item] + 1
    else:
        dictionary[item] = 1

print(dictionary)