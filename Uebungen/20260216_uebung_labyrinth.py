# Labyrinth

# Gegeben ist folgende Liste.
# Wir starten beim Element liste[0], dort steht der Index, zu dem
# wir als nächstes gehen: 3. Bei liste[3] steht dann
# wieder der Index, der als nächstes besucht werden soll: 1.
# Bei liste[1] steht wieder der nächste Index: 7. Und so weiter.
# Wenn wir dem Pfad durch das Labyrinth auf diese Weise folgen,
# gelangen wir irgendwann zu einem Listenelement, welches
# keine Zahl ist. Wir sind am Ziel.

# liste = [ 3, 7, "apfel", 1, "birne", 8, 4, 9, 5, 2]
# Index   0  1     2     3     4     5  6  7  8  9

# In der oberen Liste lässt sich noch leicht per Hand rausfinden,
# was das Ziel ist: "apfel". Überzeuge dich selbst davon.

# In der nachfolgenden Liste wäre das per Hand schon sehr 
# mühselig und fehleranfällig.
# Schreibe also ein Python-Skript und das Ziel zu finden. Ist es 
# "apfel", "birne" oder "melone"?



liste = [11, 59, 5, 30, 91, 70, 8, 92, 47, 71, 43, 38, 29, 92, 72, 'melone', 45, 87, 66, 61, 51, 37, 45, 71, 26, 54, 5, 35, 71, 'birne', 42, 11, 26, 33, 53, 58, 87, 'apfel', 99, 95, 10, 59, 23, 64, 16, 8, 27, 34, 11, 2, 67, 46, 3, 65, 18, 80, 'melone', 49, 12, 25, 24, 9, 25, 74, 53, 50, 51, 17, 82, 69, 42, 41, 71, 93, 'birne', 6, 36, 73, 76, 38, 17, 34, 81, 89, 14, 72, 20, 61, 11, 22, 46, 75, 40, 22, 25, 80, 59, 62, 19, 93]

# # stimmt nicht 
# for i in range(len(liste)):
#     if type(liste[i]) == str:
#         print("Das Ziel ist:", liste[i])
#         break


# # Alternative Lösung:  
# for i in range(len(liste)):
#     if type(liste[i]) == int:
#         i = liste[i]
#     elif type(liste[i]) == str:
#         print("Das Ziel ist:", liste[i])
#         break
#     else:
#         i = liste[i]
        
# while
wert = 0
while wert < len(liste):
    if type(liste[wert]) == int:
        wert = liste[wert]
    elif type(liste[wert]) == str:
        print("Das Ziel ist:", liste[wert])
        break
    else:
        wert = liste[wert]
        
 