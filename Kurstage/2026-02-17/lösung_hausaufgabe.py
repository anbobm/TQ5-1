# Schreibe eine Funktion, die eine Liste erhält und darin das größte Element findet.
# Aufgabe 1
# def größtes_element(liste):
#     ...
#     return größtes

def größtes_element(liste):
    größtes = liste[0]
    for zahl in liste:
        if zahl > größtes:
            größtes = zahl
    return größtes

liste = [4, 2, 7, 1, 18, 3, 6]
print(größtes_element(liste))


# Aufgabe 2
# Schreibe eine Funktion die eine Liste von Zahlen erhält, und zurückgibt, wie viele positive Zahlen in dieser Liste stehen.
# def zähle_positive(liste):
#     ...
#     return anzahl

def zähle_positive(liste):
    anzahl = 0
    for zahl in liste:
        if zahl > 0:
            anzahl = anzahl + 1
    return anzahl

liste = [4, 2, -1001, 7, 1, -3, 0, 18, 3, 6]
print(zähle_positive(liste))

# Aufgabe 3
# Schreibe eine Funktion die eine Liste von Zahlen erhält, und die Summe aller ungeraden Zahlen dieser Liste zurückgibt.
# def summe_ungerade(liste):
#     ...
#     return summe

def summe_ungerade(liste):
    summe = 0
    for zahl in liste:
        if zahl % 2 == 1:
            summe = summe + zahl
    return summe

liste = [4, 2, 7, 1, 18, 3, 6]
print(summe_ungerade(liste))