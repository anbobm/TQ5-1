#Aufgabe 1

#liste = [3, 26, -3, 0.5, "apfel"]

#print(liste[0]) #erste element
#print(liste[-1]) #letzte element #1
#print(liste[len(liste)-1]) #letzte element #2
############### HAHAHA-Lösung
#liste.reverse()
#print(liste[0])

#Aufgabe 2

#print(liste[-3]) # -3

#Aufgabe 3

#liste = [3, 26, -3, 0.5, "apfel"]

#for index, item in enumerate(liste):
#   print(f"Index {index}, item {item}")

# for index, item in enumerate(liste):
#     if item == 26:
#         liste[index] = 27

# print(liste)

#Aufgabe 4

# liste = [3, 27, -3, 0.5, "apfel"]

# for index, item in enumerate(liste):
#     if item == 0.5:
#         liste.insert(index, "birne")
#         break

# print(liste)

#Aufgabe 5

liste = [3, 27, -3, "birne", 0.5, "apfel"]

for index, item in enumerate(liste):
    if index % 2 == 1:
        print(f"Index: {index}, item: {item}")
    
