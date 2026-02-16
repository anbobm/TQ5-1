# Aufgabe 1 (DE)
# Schreibe eine Funktion, die eine Liste erhält und
#  darin das größte Element findet.

def größtes_element(liste):
    größtes = liste[0]
    for zahl in liste:
        if zahl > größtes:
            größtes = zahl
    return größtes

# Test / Kontrolle
print(größtes_element([3, 7, 2, 9, 5]))


# # Aufgabe 2
# Funktion zählt, wie viele positive Zahlen in 
# der Liste stehen

def zähle_positive(liste):
    anzahl = 0
    for zahl in liste:
        if zahl > 0:
            anzahl += 1
    return anzahl

# Test / Kontrolle
print(zähle_positive([1, -2, 3, 0, 5, -7]))


# Aufgabe 3
# Funktion berechnet die Summe 
# aller ungeraden Zahlen in der Liste.

def summe_ungerade(liste):
    summe = 0
    for zahl in liste:
        if zahl % 2 != 0:
            summe += zahl
    return summe

# Test / Kontrolle
print(summe_ungerade([1, 2, 3, 4, 5, 6, 7]))



