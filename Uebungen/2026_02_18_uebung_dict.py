# Gegeben ist folgendes Dictionary. Ergänze die Werte mit denen deines Handys.
 
# ```python
# handy = {
#     "marke": ,
#     "modell": ,
#     "speicher": ,
#     "farbe": ,
#     "betriebssystem": ,
#     "preis":
# }
# ```
 
# Schreibe ein Skript, das den Nutzer einen Schlüssel eingeben lässt.
# Existiert der Schlüssel, gib den Wert dazu aus, ansonsten gib "Der Schlüssel existiert nicht" aus

handy = {}
handy["marke"] = input("Gib die Marke deines Handys ein: ")
handy["modell"] = input("Gib das Modell deines Handys ein: ")
handy["speicher"] = input("Gib den Speicher deines Handys ein: ")
handy["farbe"] = input("Gib die Farbe deines Handys ein: ")
handy["betriebssystem"] = input("Gib das Betriebssystem deines Handys ein: ")
handy["preis"] = input("Gib den Preis deines Handys ein: ")

schluessel = input("Gib einen Schlüssel ein: ")
if schluessel in handy:
    print(handy[schluessel])   
else:
    print("Der Schlüssel existiert nicht")
    




#  Aufgabe 2'

# Die Werte von Dictionaries können beliebig sein, nicht nur string, int, float, etc., sondern auch Listen oder Dictionaries.

# dictionary = {
#     1: "foo",
#     "bar": [11, 5, "apfel"]
# }

# Erstelle ein Dictionary `students` welches für zwei Studenten `Max` und `Petra` jeweils den Schlüssel ihres Namens besitzt, 
# und der zugehörige Value ist ein Dictionary mit den Schlüsseln `alter`, `note` und `studiengang`:

# ```python
# students = {
#     "Max": ...,
#     "Petra": ...
# }

# Gib anschließend die Note von "Petra" aus.
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