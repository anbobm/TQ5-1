# Aufgabe 1
import os

pfad = r"C:\Users\Sebas\Desktop\TQ5\Repo\TQ5-1\photos"
Dateien = os.listdir(pfad)

for datei in Dateien:
    aufgeteilt = datei.split("-")
    beschreibung = aufgeteilt[2]
    datum_und_uhrzeit = aufgeteilt[3]
    datum, zeit = datum_und_uhrzeit.split("_")
    tag, monat, jahr = datum.split(".")
    zeit = zeit.replace("h", "").replace("jpg", "")
    neuer_name = f"{jahr} {monat} {tag} {zeit} {beschreibung}.jpg"
    alt = os.path.join(pfad, datei)
    neu = os.path.join(pfad, neuer_name)
    os.rename(alt, neu)

    #Aufgabe 2

taschrechner = input("Geben Sie eine Rechnung ein und gebe davor plus, minus, mal oder durch ein: ")
operationen = taschrechner.split()
operator = operationen[0]
zahl1 = float(operationen[1])
zahl2 = float(operationen[2])
if operator == "plus":
    ergebnis = zahl1 + zahl2
elif operator == "minus":
    ergebnis = zahl1 - zahl2
elif operator == "mal":
    ergebnis = zahl1 * zahl2
elif operator == "durch":
    ergebnis = zahl1 / zahl2
print("Das Ergebnis ist:", ergebnis)


