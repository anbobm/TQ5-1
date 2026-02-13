# Aufgabe 1
liste = [3, 26, -3, 0.5, "apfel"]
print(liste[0])

# Aufgabe 1.1
print(liste[4])

for i in range(len(liste)):
    if i == 4:
        print(liste[i])

# Aufgabe 2
print(liste[-3])
## Zählt die Liste rückwärts. -1 (apfel) ist der erste Eintrag und -5 (3) ist der letzte Eintrag.

# Aufgabe 3
liste = [3, 27, -3, 0.5, "apfel"]
liste[1] = 26
print(liste)

# Aufgabe 4
liste = [3, 26, -3, 0.5, "apfel"]
liste.insert(3, "birne")
print(liste)

# oder wenn man wirklich mit append arbeiten möchte:
liste.clear()
print(liste)
liste.append(3)
liste.append(26)
liste.append(-3)
liste.append(0.5)
liste.append("apfel")
print(liste)

# Aufgabe 5
liste = [3, 26, -3, "birne", 0.5, "apfel"]
# for i in range(1, len(liste), 2):
#     print(liste[i])

for i in liste[1::2]:
    print(i)


    


