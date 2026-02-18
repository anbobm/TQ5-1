# Beispiel 1:
# ValueError abfangen, der bei der int() funktion auftreten kann, wenn
# der übergebene String keine Zahl enthält, z.b. int("foo")

try:
    zahl = int(input("Gib eine Zahl ein: "))
except ValueError:
    print("Du hast keine Zahl eingegeben, ich mache mit 0 weiter")
    zahl = 0

print(f"Deine Zahl + 1 ist {zahl + 1}")

# Beispiel 2:
# KeyError abfangen, der auftreten kann, wenn ich lesen auf den Schlüssel
# eines Dictionaries zugreife, der nicht existiert

handy = {
    "marke": "Samsung",
    "modell": "A50",
    "speicher": "1 tb",
    "farbe": "Dark",
    "betriebssystem": "Android",
    "preis": 120
}

schlüssel = input("Gesuchter Schlüssel? ")
try:
    print(handy[schlüssel])
except KeyError:
    print("Schlüssel nicht vorhanden")