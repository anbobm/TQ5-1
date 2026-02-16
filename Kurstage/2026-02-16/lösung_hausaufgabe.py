# Aufgabe 1
# Gegeben ist folgende Liste:
# liste = [3, 26, -3, 0.5, "apfel"]
# Man kann sich mit `print(liste)` eine komplette Liste auf der Kommandozeile ausgeben lassen.
# Gib das allererste und das letzte Element der Liste auf die Kommandozeile aus. Beim Zugriff auf das letzte Element der Liste gibt es zwei verschiedene Möglichkeiten, zeige beide.

liste = [3, 26, -3, 0.5, "apfel"]
#        0   1   2   3      4
#       -5  -4  -3  -2     -1

# länge einer liste
print(len(liste))

# erstes element
print(liste[0])

# letztes element
print(liste[4])

# letztes element
länge = len(liste)
print(liste[länge-1])

# letztes element
print(liste[-1])

# Aufgabe 2
# Was ist die Ausgabe von print(liste[-3])? Überlege es dir vorher und probiere es dann aus.

liste = [3, 26, -3, 0.5, "apfel"]
#        0   1   2   3      4
#       -5  -4  -3  -2     -1

print(liste[-3]) # gibt -3

# Aufgabe 3
# Modifiziere die Liste so dass aus der 26 eine 27 wird.
# Die Liste sollte dann so aussehen: [3, 27, -3, 0.5, "apfel"]

liste[1] = 27
print(liste)

# Aufgabe 4
# Füge zwischen der -3 und der 0.5 den String "birne" ein.  Nutze dafür eine der Funktionen, die Listen bereits mitbringen (liste.append() etc.)
# Die Liste sollte dann so aussehen: [3, 27, -3, "birne", 0.5, "apfel"]

liste.insert(3, "birne")
print(liste)

# Aufgabe 5
# Gib alle Elemente mit ungeradem Index (1, 3, ...) auf die Kommandozeile aus.
# Die Ausgabe sollte dann so aussehen:
# 27
# birne
# apfel

# [3, 27, -3, "birne", 0.5, "apfel"]

# mit for
for i in range(1, len(liste), 2):
    print(liste[i])

# mit for, nicht ganz so effizient
for i in range (len(liste)):
    if i % 2 == 1:
        print(liste[i])

# mit while
i = 1
while i < len(liste):
    print(liste[i])
    i = i + 2