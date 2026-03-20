# Aufgabe 6
# Erstelle eine Klasse TemperaturMessung mit den Attributen wert (float in Celsius), datum (String in der Form 22.12.2026) und uhrzeit (String in der Form 3:14).

# Überschreibe in der Klasse die Methode __repr__(self). Diese soll einen String zurückgeben der Form: TemperaturMessung(24.5, "2026-12-24", "18:00").

# Lies die Datei temps.txt ein, und erstelle eine Liste temperaturen von TemperaturMessung-Objekten, je eins pro Datensatz.

# Gib dann die Liste aus mit print(temperaturen).
from datetime import datetime
class TempMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = float(wert)
        self.datum = datum
        self.uhrzeit = uhrzeit
        
    def __repr__(self):
        return f'TempMessung({self.wert}, "{self.datum}", "{self.uhrzeit}")'
    
temperaturen = []

datei = open("20260318_temperaturen.txt", encoding="utf-8")
for zeile in datei:
    zeile = zeile.removesuffix("Uhr\n")
    if not zeile:
        continue
    
    wert, datum, uhrzeit = zeile.split()
    jahr, monat, tag = datum.split("-")
    
    datum = f"{tag}.{monat}.{jahr}"
    temperaturen.append(TempMessung(wert, datum, uhrzeit))
    

# Aufgabe 7
# Die Datei temps.txt soll in eine Liste von TemperaturMessung-Objekten eingelesen werden, wie in Aufgabe 6.

# Anschließend soll dem Benutzer folgendes angezeigt werden:

# Was möchtest du tun?
# [1] Messungen anzeigen
# [2] Messung hinzufügen
# [3] Messung löschen
# [E] Speichern und beenden


# Wenn der Benutzer 1 eingibt, sollen alle Messungen in der Liste ausgeben werden, zusammen mit einer Nummer:
# # Messungen
# [0] 13.4 °C, 19.10.2026, 19:58 Uhr
# [1] 19.9 °C, 4.1.2026, 9:36 Uhr
# [2] 24.4 °C, 10.1.2026, 16:42 Uhr
while True:
    eingabe = input("Was möchtest du tun?\n--------------------\n[1] Messungen anzeigen\n[2] Messung hinzufügen\n[3] Messungen löschen\n[E] Speichern & Beenden\n")


    if eingabe == "1":
        index = 0
        for messung in temperaturen:
            print(f"[{index}] {messung.wert} °C, {messung.datum}, {messung.uhrzeit} Uhr")
            index = index + 1
            
    elif eingabe == "2":
        temperatur = input(f"Gib die Temperatur in °C ein (Format xy.z): ")
        datum = input("Gib das Datum ein (Format TT.MM.JJJJ): ")
        uhrzeit = datetime.now().strftime("%H:%M")
        temperaturen.append(TempMessung(temperatur, datum, uhrzeit))

    elif eingabe == "3":
        index = int(input("Gib die Nummer des Datensatzes ein, den du löschen möchtest: "))
        #if index >= 0 and index < len(temperaturen):
        if index in range(len(temperaturen)):
            temperaturen.pop(index)
            print(f"Messung mit Index [{index}] gelöscht.")
        else:
            print("Diese Nummer gibt es nicht.")

    elif eingabe.upper() == "E":
        datei = open("20260318_temperaturen.txt", "w", encoding="utf-8")
        for m in temperaturen:
           tag, monat, jahr = m.datum.split(".")
           datum_format = f"{jahr}-{monat}-{tag}"
           datei.write(f"{m.wert} {datum_format} {m.uhrzeit}Uhr\n")
        
        print("Daten gespeichert und Programm verlassen.")
        break
    
    else:
        print("Eingabe ungültig:",eingabe)
    
    datei.close()
       
        

# ...
# Wenn der Benutzer 2 eingibt, dann soll er zur Eingabe der Temperatur in °C und zur Eingabe von Datum und Uhrzeit (in einem explizit angegebenen Format) aufgefordert werden. Daraus wird ein TemperaturMessung-Objekt erzeugt und der Liste angehängt.

# Wenn der Benutzer 3 eingibt, kann der Benutzer die Nummer des Datensatzes angeben, den er löschen möchte. Dieser wird dann aus der temperaturen-Liste entfernt. (pop(index))

# Wenn der Benutzer E eingibt, soll die Liste der Messungen wieder in temps.txt gespeichert, und das Programm beendet werden.