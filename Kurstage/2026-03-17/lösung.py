# # Aufgabe 1

# eingabe = open("Kurstage/2026-03-17/input.txt")
# inhalt = eingabe.read()
# eingabe.close()

# ausgabe = open("Kurstage/2026-03-17/lange_wörter.txt", "w")

# wörter = inhalt.split()

# for wort in wörter:
#     if len(wort) > 5:
#         ausgabe.write(f"{wort}\n")

# ausgabe.close()

# # Alternative: zeilenweise

# eingabe = open("Kurstage/2026-03-17/input.txt")
# ausgabe = open("Kurstage/2026-03-17/lange_wörter.txt", "w")

# for zeile in eingabe:
#     wörter = zeile.split()
#     for wort in wörter:
#         if len(wort) > 5:
#             ausgabe.write(f"{wort}\n")

# eingabe.close()
# ausgabe.close()


# # Aufgabe 2 (removesuffix, doch nicht rstrip)

# eingabe = input("Gib irgendwas ein: ")

# print(eingabe.removesuffix("bar"))


# # Aufgabe 3

# datei = open("Kurstage/2026-03-17/dates.txt")
# zeilen = datei.read().splitlines()
# datei.close()

# neue_datei = open("Kurstage/2026-03-17/formatted_dates.txt", "w")

# for zeile in zeilen:
#     zeile = zeile.removesuffix("Uhr")

#     datum, uhrzeit = zeile.split()
#     neue_datei.write(f"Datum: {datum}\nUhrzeit: {uhrzeit}\n\n")

# neue_datei.close()


# # Aufgabe 4

# datei = open("Kurstage/2026-03-17/dates.txt")
# zeilen = datei.read().splitlines()
# datei.close()

# neue_datei = open("Kurstage/2026-03-17/formatted_dates.txt", "w")

# for zeile in zeilen:
#     zeile = zeile.removesuffix("Uhr")
#     datum, uhrzeit = zeile.split()
#     jahr, monat, tag = datum.split("-")
#     neue_datei.write(f"Datum: {tag}.{monat}.{jahr}\nUhrzeit: {uhrzeit}\n\n")

# neue_datei.close()

# # Aufgabe 5

# datei = open("Kurstage/2026-03-17/temps.txt", encoding="utf-8")
# zeilen = datei.read().splitlines()
# datei.close()

# neue_datei = open("Kurstage/2026-03-17/formatted_temps.txt", "w", encoding="utf-8")

# for zeile in zeilen:
#     zeile = zeile.removesuffix("Uhr")
#     temperatur, datum, uhrzeit = zeile.split()
#     jahr, monat, tag = datum.split("-")
#     neue_datei.write(f"Temperatur: {temperatur} °C\n")
#     neue_datei.write(f"Datum: {tag}.{monat}.{jahr}\n")
#     neue_datei.write(f"Uhrzeit: {uhrzeit}\n\n")

# neue_datei.close()


# # Aufgabe 6

# class TemperaturMessung:
#     def __init__(self, wert, datum, uhrzeit):
#         self.wert = wert
#         self.datum = datum
#         self.uhrzeit = uhrzeit

#     def __repr__(self):
#         return f"TemperaturMessung({self.wert}, '{self.datum}', '{self.uhrzeit}')"
    

# datei = open("Kurstage/2026-03-17/temps.txt", encoding="utf-8")
# zeilen = datei.read().splitlines()
# datei.close()

# temperaturen = []

# for zeile in zeilen:
#     zeile = zeile.removesuffix("Uhr")
#     temperatur, datum, uhrzeit = zeile.split()
#     jahr, monat, tag = datum.split("-")

#     temperatur = float(temperatur)
#     datum = f"{tag}.{monat}.{jahr}"

#     messung = TemperaturMessung(temperatur, datum, uhrzeit)
#     temperaturen.append(messung)
    
# print(temperaturen)


# Aufgabe 7

class TemperaturMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = wert
        self.datum : str = datum # Type hint str bedeutet datum soll String sein
        self.uhrzeit = uhrzeit

    def __repr__(self):
        return f"TemperaturMessung({self.wert}, '{self.datum}', '{self.uhrzeit}')"
    

datei = open("Kurstage/2026-03-17/temps.txt", encoding="utf-8")
zeilen = datei.read().splitlines()
datei.close()

temperaturen : list[TemperaturMessung] = [] # Type hint list[TemperaturMessung] bedeutet Liste von TemperaturMessungs-Objekten

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    temperatur, datum, uhrzeit = zeile.split()
    jahr, monat, tag = datum.split("-")

    temperatur = float(temperatur)
    datum = f"{tag}.{monat}.{jahr}"

    messung = TemperaturMessung(temperatur, datum, uhrzeit)
    temperaturen.append(messung)

while True:
    print("Was möchtest du tun?")
    print("[1] Messungen anzeigen")
    print("[2] Messung hinzufügen")
    print("[3] Messung löschen")
    print("[E] Speichern und beenden")

    eingabe = input()

    if eingabe == "1":
        index = 0
        for messung in temperaturen:
            print(f"[{index}] {messung.wert} °C, {messung.datum}, {messung.uhrzeit} Uhr")
            index += 1

        # Alternative:
        # for index, messung in enumerate(temperaturen):
        #     print(f"[{index}] {messung.wert} °C, {messung.datum}, {messung.uhrzeit} Uhr")
            
    elif eingabe == "2":
        temperatur = float(input("Temperaturwert in °C? "))
        datum = input("Datum (DD.MM.YYYY)? ")
        uhrzeit = input("Uhrzeit (HH:MM)? ")

        messung = TemperaturMessung(temperatur, datum, uhrzeit)
        temperaturen.append(messung)

    elif eingabe == "3":
        index = int(input("Welche Messung löschen (Nr.)? "))
   
        # Alternative: if index in range(len(temperaturen)):
        if index >= 0 and index < len(temperaturen):
            temperaturen.pop(index)
            print(f"Messung Nr. {index} gelöscht")
        else:
            print("Diese Nummer gibt es nicht")

    elif eingabe == "E":
        break
    else:
        print("Menüoption nicht verfügbar")


datei = open("Kurstage/2026-03-17/temps.txt", "w", encoding="utf-8")
for messung in temperaturen:
    tag, monat, jahr = messung.datum.split(".")
    datei.write(f"{messung.wert} {jahr}-{monat}-{tag} {messung.uhrzeit}Uhr\n")
datei.close()