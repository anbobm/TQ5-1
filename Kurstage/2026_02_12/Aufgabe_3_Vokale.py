# Aufgabe 3
# Der Benutzer soll einen Satz eingeben.
# Anschließend zählen wir, wie viele Vokale (a, e, i, o, u) vorhanden sind.

satz = input("Gib ein Wort oder einen Satz ein: ")
vokale = "aeiou"
anzahl = 0

for zeichen in satz:
    if zeichen.lower() in vokale:
        anzahl = anzahl + 1

print("Anzahl der Vokale:", anzahl)