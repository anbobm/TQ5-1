# Aufgabe 1
# Die Liste soll durchlaufen werden.
# Regeln:
# Wenn der Wert gerade ist → zum Code addieren
# Wenn der Wert ungerade ist → vom Code subtrahieren
# Aber zusätzlich:
# Wenn der Index gerade ist → Wert vorher verdoppeln
# Wenn der Index ungerade ist → Wert nicht verdoppeln
# Gesucht ist der Code (Endwert) für die gegebene Liste.


def berechne_code(liste):
    code = 0

    for index, wert in enumerate(liste):

        if index % 2 == 0:
            wert = wert * 2

        if wert % 2 == 0:
            code += wert
        else:
            code -= wert

    return code

# # Test
liste = [3, 9, 6, 6, 5, 5, 5, 4, 5, 8, 2, 8, 6, 7, 3, 7, 
6, 8, 6, 9, 9, 3, 7, 9, 1, 5, 5, 7, 8, 5,
2, 1, 3, 9, 7, 9, 8, 9, 6, 9]

print(berechne_code(liste))