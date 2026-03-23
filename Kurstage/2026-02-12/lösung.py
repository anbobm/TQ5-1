# # Aufgabe 1
# # Nutze eine `while`-Schleife, um die Zahlen von 10 bis 1 auszugeben.

# zahl = 10

# while zahl >= 1:
#     print(zahl)
#     zahl = zahl - 1


# # Aufgabe 2
# # Berechne die Fakultät einer Zahl, die der Benutzer eingegeben hat.
# # 5! = fakultät(5) = 1 * 2 * 3 * 4 * 5
# # 7! = fakultät(7) = 1 * 2 * 3 * 4 * 5 * 6 * 7

# # Randbemerkung:
# # 1! = fakultät(1) = 1
# # 0! = fakultät(0) = 1

# # mit for

# zahl = int(input("Zahl! "))

# faktoren = range(1, zahl + 1)

# produkt = 1

# for faktor in faktoren:
#     produkt = produkt * faktor

# print(f"{zahl}! = fakultät({zahl}) = {produkt}")

# # mit while

# zahl = int(input("Zahl! "))
# faktor = 1
# produkt = 1

# while faktor <= zahl:
#     produkt = produkt * faktor
#     faktor = faktor + 1

# print(f"{zahl}! = fakultät({zahl}) = {produkt}")

# # Aufgabe 3

# # Der Benutzer soll einen Satz eingeben. Anschließend zählen wir, wie viele Vokale (a, e, i, o, u) in diesem Satz vorhanden sind.

# satz = input()

# anzahl = 0

# vokale = "aeiou"

# for zeichen in satz:
#     zeichen = zeichen.lower()
#     if zeichen in vokale:
#         anzahl = anzahl + 1

# print(anzahl)

# # Aufgabe 4

# # Frage den Benutzer so lange nach einer Zahl, bis er eine 0 eingibt. Anschließend gib die Summe aller Zahlen die er eingegeben hat aus. Z.B:
# # Zahl? 34
# # Zahl? 35
# # Zahl? 0
# # Summe = 69

# summe = 0

# while True:
#     zahl = int(input("Zahl? "))
#     if zahl == 0:
#         break
#     summe = summe + zahl

# print(summe)

# Aufgabe 5
# Gegeben ist folgende Liste:
# liste = [2, 2, 3, 3, 1, 2, 1, 1, 3, 2, 2, 3, 1, 3, 1, 2, 3, 2, 2, 1, 2, 2, 1, 3, 1, 1, 2, 1, 1, 3, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 1, 2, 1, 3, 1, 2, 2, 1, 2, 3, 3, 2, 3, 2, 3, 3, 3, 3, 1, 2, 3, 2, 3, 1, 3, 1, 3, 3, 3, 1, 2, 1, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 3, 3, 1, 1, 1, 2, 2, 1, 1, 2, 3, 3]
# Zähle mit einer Schleife, wie oft die Zahl 3 in dieser Liste vorkommt. (36 mal)

liste = [2, 2, 3, 3, 1, 2, 1, 1, 3, 2, 2, 3, 1, 3, 1, 2, 3, 2, 2, 1, 2, 2, 1, 3, 1, 1, 2, 1, 1, 3, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 1, 2, 1, 3, 1, 2, 2, 1, 2, 3, 3, 2, 3, 2, 3, 3, 3, 3, 1, 2, 3, 2, 3, 1, 3, 1, 3, 3, 3, 1, 2, 1, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 3, 3, 1, 1, 1, 2, 2, 1, 1, 2, 3, 3]

count = 0

for element in liste:
    if element == 3:
        count = count + 1

print(count)