# dictionaries

# definieren
person = {"name" : "Max", "alter": 25}

# leeres dict
foo = {}

# Schlüssel-Wert-Paar hinzufügen
person["adresse"] = "Am Teich 1, 01234 Dorf"
print(person) # {'name': 'Max', 'alter': 25, 'adresse': 'Am Teich 1, 01234 Dorf'}

# Wert zu Schlüssel auslesen
name = person["name"]
alter = person["alter"]
adresse = person["adresse"]

# lesend auf fehlenden Schlüssel zugreifen: KeyError
# email = person["email"]

# Prüfen, ob Schlüssel in Dictionary vorhanden mit in-Keyword:
"name" in person # True
"alter" in person # True
"adresse" in person # True
"email" in person # False
25 in person # False

# mit dict.get() kann man den Wert zu einem Schlüssel auslesen, wenn der Schlüssel nicht
# existiert, dann wird der übergebene Default-Wert zurückgegeben
person.get("email", "")

for key in person:
    print(f"Schlüssel {key} hat Wert {person[key]}")

# mit == kann man gucken ob zwei dictionaries genau gleich sind (Reihenfolge
# der Schlüssel ist egal)
{"a": 1, "b": 2} == {"b": 2, "a": 1} # True