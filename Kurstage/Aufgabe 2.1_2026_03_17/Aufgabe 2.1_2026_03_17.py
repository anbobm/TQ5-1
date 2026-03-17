# Aufgabe 2.1

text = input("Eingabe? ")

if text.endswith("bar"):
    text = text[:-3]

print("Ausgabe:", text)