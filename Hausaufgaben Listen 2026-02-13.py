# Aufgabe 1
# Gegeben ist folgende Liste:
# liste = [3, 26, -3, 0.5, "apfel"]
# Man kann sich mit print(liste) eine 
# komplette Liste auf der Kommandozeile ausgeben lassen.
# Gib das allererste und das letzte Element
# der Liste auf die Kommandozeile aus. 
# Beim Zugriff auf das letzte Element der Liste gibt
# es zwei verschiedene Möglichkeiten, zeige beide.

# Lösung 1

liste = [3, 26, -3, 0.5, "apfel"]
# 1. Element ausgeben
print(liste[0])  
# Letztes Element ausgeben
print(liste[-1])  
# Alternative Möglichkeit, das letzte Element auszugeben
print(liste[len(liste)-1])

# Aufgabe 2
# Was ist die Ausgabe von print(liste[-3])? 
# Überlege es dir vorher und probiere es dann aus.

# Lösung 2

print(liste[-3])   

# Aufgabe 3
# Modifiziere die Liste so dass aus der 26 eine 27 wird.

# Die Liste sollte dann so aussehen: [3, 27, -3, 0.5, "apfel"]

# Lösung 3

liste = [3, 26, -3, 0.5, "apfel"]

liste[1] = 27

[3, 27, -3, 0.5, "apfel"]


# Aufgabe 4
# Füge zwischen der -3 und der 0.5 den String "birne" ein.
# Nutze dafür eine der Funktionen, die Listen bereits mitbringen 
# (liste.append() etc.)
# Die Liste sollte dann so aussehen: [3, 27, -3, "birne", 0.5, "apfel"]

# Lösung 4

liste.insert(3, "birne")
print(liste)

# Aufgabe 5
# Gib alle Elemente mit ungeradem Index (1, 3, ...) 
# auf die Kommandozeile aus.
# Die Ausgabe sollte dann so aussehen:

# 27
# birne
# apfel

liste = [3, 27, -3, "birne", 0.5, "apfel"]
for i in range(1, len(liste), 2):
    print(liste[i])

