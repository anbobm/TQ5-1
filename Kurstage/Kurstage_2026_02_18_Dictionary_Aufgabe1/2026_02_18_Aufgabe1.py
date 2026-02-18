# Aufgabe 1
# Gegeben ist folgendes Dictionary.
# Ergänze die Werte mit denen deines Handys.
# Schreibe ein Skript, das den Nutzer einen Schlüssel eingeben lässt.
# Existiert der Schlüssel, gib den Wert dazu aus,
# ansonsten gib "Der Schlüssel existiert nicht" aus.

handy = {
    "marke": "Xiaomi",
    "modell": "Redmi Note 13 Pro+ 5G",
    "speicher": "512 GB",
    "ram": "12 GB",
    "farbe": "schwarz",
    "betriebssystem": "Android 15",
    "preis": 250
}


schluessel = input("Gib einen Schlüssel ein: ")

if schluessel in handy:
    print(handy[schluessel])
else:
    print("Der Schlüssel existiert nicht")


   