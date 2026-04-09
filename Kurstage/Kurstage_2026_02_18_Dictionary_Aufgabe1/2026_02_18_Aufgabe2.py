# Aufgabe 2
# Die Werte von Dictionaries können auch Listen oder Dictionaries sein.

students = {
    "Max": {
        "alter": 22,
        "note": "gut",
        "studiengang": "Informatik"
    },
    "Petra": {
        "alter": 21,
        "note": "sehr gut",
        "studiengang": "Biologie"
    }
}

# Ausgabe der Note von Petra
print(students["Petra"]["note"])