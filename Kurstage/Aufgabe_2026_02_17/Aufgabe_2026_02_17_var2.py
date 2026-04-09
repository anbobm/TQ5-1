# Alternative 2
liste = [3, 9, 6, 6, 5, 5, 5, 4, 5, 8, 2, 8, 6, 7, 3, 7, 6, 8, 6, 9, 9, 3, 7, 9, 1, 5, 5, 7, 8, 5, 2, 1, 3, 9, 7, 9, 8, 9, 6, 9, 6, 5, 6, 3, 3, 7, 4, 9, 9, 5, 4, 9, 9, 8, 1, 9, 8, 9, 8, 6, 1, 8, 3, 3, 2, 4, 9, 2, 6, 2, 9, 3, 9, 6, 8, 4, 5, 4, 4, 3, 8, 8, 1, 3, 4, 2, 8, 3, 5, 7, 4, 4, 1, 3, 3, 3, 2, 9, 9, 8]

code = 0
for index in range(len(liste)):
    wert = liste[index]

    wert_gerade = wert % 2 == 0
    wert_ungerade = not wert_gerade
    index_gerade = index % 2 == 0
    index_ungerade = not index_gerade

    if wert_gerade and index_gerade:
        code = code + 2 * wert
    elif wert_gerade and index_ungerade:
        code = code + wert
    elif wert_ungerade and index_gerade:
        code = code - 2 * wert
    elif wert_ungerade and index_ungerade:
        code = code - wert
print(code)