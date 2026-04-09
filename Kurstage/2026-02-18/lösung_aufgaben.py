# Aufgabe 1
# Gegeben ist folgendes Dictionary. Ergänze die Werte mit denen deines Handys.
# handy = {
#     "marke": ,
#     "modell": ,
#     "speicher": ,
#     "farbe": ,
#     "betriebssystem": ,
#     "preis": 
# }
# Schreibe ein Skript, das den Nutzer einen Schlüssel eingeben lässt.
# Existiert der Schlüssel, gib den Wert dazu aus, ansonsten gib "Der Schlüssel existiert nicht" aus.

handy = {
    "marke": "Samsung",
    "modell": "A50",
    "speicher": "1 tb",
    "farbe": "Dark",
    "betriebssystem": "Android",
    "preis": 120
}

schlüssel = input("Gesuchter Schlüssel? ")

if schlüssel in handy:
    print(handy[schlüssel])
else:
    print("Der Schlüssel existiert nicht")

# Aufgabe 2
# Die Werte von Dictionaries können beliebig sein, nicht nur string, int, float, etc., sondern auch Listen oder Dictionaries.
# dictionary = {
#     1: "foo",
#     "bar": [11, 5, "apfel"]
# }
# Erstelle ein Dictionary `students` welches für zwei Studenten `Max` und `Petra` jeweils den Schlüssel ihres Namens besitzt, und der zugehörige Value ist ein Dictionary mit den Schlüsseln `alter`, `note` und `studiengang`:
# students = {
#     "Max": ...,
#     "Petra": ...
# }
# Gib anschließend die Note von "Petra" aus.

students = {
    "Max": {
        "alter": 23,
        "note": "sehr gut",
        "studiengang": "Informatik"
    },
    "Petra": {
        "alter": 22,
        "note": "gut",
        "studiengang": "Medizin"
    }
}

petra = students["Petra"]
note_von_petra = petra["note"]
print(note_von_petra)

# oder ohne Zwischenvariablen:
print(students["Petra"]["note"])