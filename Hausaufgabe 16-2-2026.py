# Aufgabe 1
liste = [11, 59, 5, 30, 91, 70, 8, 92, 47, 71, 43, 38, 29, 92, 72, 45, 87, 66, 61, 51, 37, 45, 71, 26, 54, 5, 35, 71, 42, 11, 26, 33, 53, 58, 87, 99, 95, 10, 59, 23, 64, 16, 8, 27, 34, 11, 2, 67, 46, 3, 65, 18, 80, 'melone', 49]
def größtes_element(liste):
    größtes = liste[0]
    for i in liste:
        if type(i) == int and i > größtes:
            größtes = i
    return größtes
print(größtes_element(liste))

# Aufgabe 2
def zähle_positive(liste):
    anzahl = 0
    for i in liste:
        if type(i) == int and i > 0:
            anzahl += 1
    return anzahl
print(zähle_positive(liste))

# Aufgabe 3
def summe_ungrade(liste):
    summe = 0
    for i in liste:
        if type(i) == int and i % 2 == 1:
            summe += i
    return summe
print(summe_ungrade(liste))