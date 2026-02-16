# Aufgabe 1

# Schreibe eine Funktion, die eine Liste erhält und darin das größte Element findet.
# python
# def größtes_element(liste):
#     ...
#     ...
#     ...
#     return größtes
liste = [3, 7, 181, 8, 47, 9, 5, 32]

def größtes_element(liste):
    größtes = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > größtes:
            größtes = liste[i]
    return größtes
print("Das größte Element ist:", größtes_element(liste))


# Aufgabe 2

# Schreibe eine Funktion die eine Liste von Zahlen erhält, und zurückgibt, wie viele positive Zahlen in dieser Liste stehen.
# ```python
# def zähle_positive(liste):
#     ...
#     ...
#     ...
#     return anzahl
# ```
liste = [3, 7, -181, -8, 47, -9, 5, 32]

def pos_zahlen(liste):
    anzahl = 0
    for i in range(len(liste)):
        if liste[i] > 0:
            anzahl = anzahl + 1
    return anzahl
print("Die Anzahl positiver Zahlen ist:", pos_zahlen(liste))


# # Aufgabe 3
# Schreibe eine Funktion die eine Liste von Zahlen erhält, und die Summe aller ungeraden Zahlen dieser Liste zurückgibt.

# ```python
# def summe_ungerade(liste):
#     ...
#     ...
#     ...
#     return summe
# `
liste = [3, 7, -181, -8, 47, -9, 5, 32]

def summe_ungerade(liste):
    summe = 0
    for i in range(len(liste)):
        if liste[i] % 2 != 0:
            summe = summe + liste[i]
    return summe
print("Die Summe aller ungeraden Zahlen ist:", summe_ungerade(liste))