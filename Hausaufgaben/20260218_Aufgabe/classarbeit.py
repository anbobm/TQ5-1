handy = {
    "marke": "Samsung",
    "modell": "A50",
    "speicher": "1 tb",
    "farbe": "Dark",
    "betriebssystem": "Android",
    "preis": 120 
}

key = ""
while key != "exit":

    key = input("Geben Sie ein Schluessel ein: ").lower()

    if key in handy:
        print(handy[key])
    else:
        print("Der Schlüssel existiert nicht")

#Aufgabe 2 

students = {
    "Max": {
        "Alter": 22, 
        "Note":"good", 
        "Studiengang": "Biologie"
        },
    "Petra": {
        "Alter": 27, 
        "Note":"befriedigend", 
        "Studiengang": "Mathe"
    }
}

print("Die Note von Petra ist: " + students["Petra"]["Note"])
