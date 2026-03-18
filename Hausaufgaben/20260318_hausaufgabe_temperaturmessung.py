# Aufgabe 6
# Erstelle eine Klasse TemperaturMessung mit den Attributen wert (float in Celsius), datum (String in der Form 22.12.2026) und uhrzeit (String in der Form 3:14).

# Überschreibe in der Klasse die Methode __repr__(self). Diese soll einen String zurückgeben der Form: TemperaturMessung(24.5, "2026-12-24", "18:00").

# Lies die Datei temps.txt ein, und erstelle eine Liste temperaturen von TemperaturMessung-Objekten, je eins pro Datensatz.

# Gib dann die Liste aus mit print(temperaturen).

class TempMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = float(wert)
        self.datum = datum
        self.uhrzeit = uhrzeit
        
    def __repr__(self):
        return f'TempMessung({self.wert}, "{self.datum}", "{self.uhrzeit}")'
    
temperaturen = []

datei = open("20260318_temperaturen.txt", "r", encoding="utf-8")
for zeile in datei:
    zeile = zeile.strip()
    if not zeile:
        continue
    
    wert, datum, uhrzeit = [mess.strip() for mess in zeile.split(" ")]
    temperaturen.append(TempMessung(wert, datum, uhrzeit))
    
    print(temperaturen)
    
datei.close()