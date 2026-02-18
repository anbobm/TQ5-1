# Aufgabe 1
 
#Gegeben ist folgendes Dictionary. Ergänze die Werte mit denen deines Handys.
 

handy = {
    "marke": "Samsung",
    "modell": "Galaxy S21",
    "speicher": "128 GB",
    "farbe": "Schwarz",
    "betriebssystem": "Android",
    "preis": 799.99
}

 
#Schreibe ein Skript, das den Nutzer einen Schlüssel eingeben lässt.
#Existiert der Schlüssel, gib den Wert dazu aus, ansonsten gib "Der Schlüssel existiert nicht" aus.

schluessel = input("Gib einen Schlüssel ein: ")

if schluessel in handy:
    print(handy[schluessel])
else:
    print("Der Schlüssel existiert nicht")


# Aufgabe 2
dictionary = {
    1: "foo",
    "bar": [11, 5, "apfel"]
}

#Erstelle ein Dictionary `students` welches für zwei Studenten `Max` und `Petra` jeweils den Schlüssel ihres Namens besitzt, und der zugehörige Value ist ein Dictionary mit den Schlüsseln `alter`, `note` und `studiengang`:


students = {
    "Max": {
        "alter": 20,
        "note": 1.5,
        "studiengang": "Informatik"
    },
    "Petra": {
        "alter": 22,
        "note": 2.0,
        "studiengang": "Mathematik"
    }
}

#Gib anschließend die Note von "Petra" aus
print(students["Petra"]["note"])

dict = {
   "a": 1,
   "b": 23
}

for key in dict:
   if key == "b":
      print(dict[key])