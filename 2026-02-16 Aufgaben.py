# # Aufgabe 1

# Schreibe eine Funktion, die eine Liste erhält und 
# darin das größte Element findet.

# ```python
# def größtes_element(liste):
#     ...
#     ...
#     ...
#     return größtes
# ```

# Lösung Aufgabe 1
def groesstes_element(liste):
    groesstes = liste[0]
    for element in liste:
        if element > groesstes:
            groesstes = element
    return groesstes

zahlen = [3, 17, 9, 42, 5, 150]
ergebnis = groesstes_element(zahlen)
print("Das größte Element ist:", ergebnis)

# # Aufgabe 2

# Schreibe eine Funktion die eine Liste von Zahlen erhält, und zurückgibt, wie viele positive Zahlen in dieser Liste stehen.

# ```python
# def zähle_positive(liste):
#     ...
#     ...
#     ...
#     return anzahl
# ```

# Lösung Aufgabe 2
def zaehle_positive(liste):
    anzahl = 0
    for zahl in liste:
        if zahl > 0:
            anzahl += 1
    return anzahl

zahlen = [-3, 0, 5, 12, -7, 8, 12, 25, +78, -5]
ergebnis = zaehle_positive(zahlen)
print("Anzahl positiver Zahlen:", ergebnis)


# # Aufgabe 3

# Schreibe eine Funktion die eine Liste von Zahlen erhält, und die Summe aller ungeraden Zahlen dieser Liste zurückgibt.

# ```python
# def summe_ungerade(liste):
#     ...
#     ...
#     ...
#     return summe
# ```

# Lösung Aufgabe 3
def summe_ungerade(liste):
    summe = 0
    for zahl in liste:
        if zahl % 2 != 0:
            summe += zahl
    return summe

zahlen = [3, 8, 11, 4, 7, 10, 12, 15, 42, 112, 1110]
ergebnis = summe_ungerade(zahlen)
print("Summe der ungeraden Zahlen:", ergebnis)

