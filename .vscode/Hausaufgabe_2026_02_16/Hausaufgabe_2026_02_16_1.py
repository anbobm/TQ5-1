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