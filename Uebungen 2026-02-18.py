# Aufgabe 1
 
# Gegeben ist folgendes Dictionary. Ergänze die Werte mit denen deines Handys.
 
# ```python
# handy = {
#     "marke": "Samsung",
#     "modell": "Galaxy S24",
#     "speicher": "256 GB",
#     "farbe": "Schwarz",
#     "betriebssystem": "Android 14",
#     "preis": 899.99
# }
# ```
 
# Schreibe ein Skript, das den Nutzer einen Schlüssel eingeben lässt.
# Existiert der Schlüssel, gib den Wert dazu aus, ansonsten gib "Der Schlüssel existiert nicht" aus.

# Lösung Aufgabe 1

handy = {
    "marke": "Samsung",
    "modell": "Galaxy S25 FE",
    "speicher": "256 GB",
    "farbe": "blau",
    "betriebssystem": "Android",
    "preis": 699
}

schluessel = input("Welchen Schlüssel möchtest du abfragen? ")

if schluessel in handy:
    print(handy[schluessel])
else:
    print("Der Schlüssel existiert nicht")

# Aufgabe 2
# Die Werte von Dictionaries können beliebig sein, nicht nur string, int, float, etc., 
# sondern auch Listen oder Dictionaries.

# dictionary = {
#     1: "foo",
#     "bar": [11, 5, "apfel"]
# }

# Erstelle ein Dictionary `students` welches für zwei Studenten `Max` und `Petra` 
# jeweils den Schlüssel ihres Namens besitzt, und der zugehörige Value ist ein Dictionary 
# mit den Schlüsseln `alter`, `note` und `studiengang`:

# ```python
# students = {
#     "Max": ...,
#     "Petra": ...
# }

# Gib anschließend die Note von "Petra" aus.

# Lösung Aufgabe 2

students = {
    "Max": {
        "alter": 22,        
        "note": "gut",
        "studiengang": "Informatik"
    },
    "Petra": {
        "alter": 21,
        "note": "sehr gut",
        "studiengang": "Mathematik"
    }
}       
print(students["Petra"]["note"])
