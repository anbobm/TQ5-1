# # # Aufgabe 1
# eingabe = open('C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\input.txt', 'r')
# inhalt = eingabe.read()
# eingabe.close()

# ausgabe = open('C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\lange_wörter.txt', 'w')
# wörter = inhalt.split()

# for wort in wörter:
#     if len(wort) > 5:
#         ausgabe.write(wort + '\n')
# ausgabe.close()

# #Aufgabe 2
# Eingabe = input('Geben Sie einen Satz ein: ')
# Ausgabe = print(Eingabe.rstrip("bar"))


# # Aufgabe 3
# with open('dates.txt', 'r') as eingabe:
#     inhalt = eingabe.read()

# zeilen = inhalt.split()

# with open('dates_output.txt', 'w') as ausgabe:
#     for zeile in range(0, len(zeilen), 2):
#         ausgabe.write(f"Datum: {zeilen[zeile]}, \nUhrzeit: {zeilen[zeile + 1].rstrip('Uhr')}\n\n")

# #Aufgabe 4
# with open('dates.txt', 'r') as eingabe:
#     inhalt = eingabe.read()

# zeilen = inhalt.split()
# date = []
# for i in range(0, len(zeilen), 2):
#     date.append(zeilen[i])

# with open('dates_output2.txt', 'w') as ausgabe:
#     for zeile in range(0, len(zeilen), 2):
#         d = zeilen[zeile].replace('-', '.')
#         d = d.split(".")
#         date = ".".join(reversed(d))
#         ausgabe.write(f"Datum: {date}, \nUhrzeit: {zeilen[zeile + 1].rstrip('Uhr')}\n\n")
        
#Aufgabe 5
# datei = open("temps.txt", "r")
# zeilen = datei.read().splitlines()
# datei.close()

# neue_datei = open("formatted_dates.txt", "w")
# for zeile in zeilen:
#     zeile = zeile.removesuffix("Uhr")
#     temperatur, datum, uhrzeit = zeile.split()
#     jahr, monat, tag = datum.split("-")
#     neue_datei.write(f"Temperatur: {temperatur} Grad Celsius\nDatum: {tag}.{monat}.{jahr}\nUhrzeit: {uhrzeit}\n\n")
# neue_datei.close()

#Aufgabe 6
class TemperaturMessung:
    def __init__(self, wert, datum, uhrzeit):
        self.wert = wert
        self.datum = datum
        self.uhrzeit = uhrzeit
    def __repr__(self):
        return f"TemperaturMessung({self.wert}, '{self.datum}', '{self.uhrzeit}')"
    
    def Messung_anzeigen(self):
        Anzahl_Messungen = 0
        for zeile in zeilen:
            temperatur, datum, uhrzeit = zeile.split()
            jahr, monat, tag = datum.split("-")
            datum = f"{tag}.{monat}.{jahr}"
            print(f" [{Anzahl_Messungen}] {temperatur} °C, {datum}, {uhrzeit}\n")
            Anzahl_Messungen += 1
    
    def Messung_hinzufügen(self, wert, datum, uhrzeit):
        neue_messung = TemperaturMessung(wert, datum, uhrzeit)
        temperaturen.append(neue_messung)
        print("Messung hinzugefügt.")
    

datei = open("temps.txt", encoding="utf-8")
zeilen = datei.read().splitlines()
datei.close()

temperaturen = []

for zeile in zeilen:
    zeile = zeile.removesuffix("Uhr")
    temperatur, datum, uhrzeit = zeile.split()
    jahr, monat, tag = datum.split("-")

    temperatur = float(temperatur)
    datum = f"{tag}.{monat}.{jahr}"

    messung = TemperaturMessung(temperatur, datum, uhrzeit)
    temperaturen.append(messung)
    
print(temperaturen)

#Aufgabe 7
print("Was möchten Sie tun?" \
"\n1. Alle Messungen anzeigen" \
"\n2. Messung hinzufügen" \
"\n3. Messung löschen" \
"\nE. Speichern und Beenden")

while True:
    auswahl = input("Ihre Auswahl: ")
    if auswahl == "1":
        messung.Messung_anzeigen()
    elif auswahl == "2":
        wert = float(input("Geben Sie den Temperaturwert ein in Grad Celsius: "))
        datum = input("Geben Sie das Datum im Format TT.MM.JJJJ ein: ")
        uhrzeit = input("Geben Sie die Uhrzeit im Format HH:MM ein: ")
        messung.Messung_hinzufügen(wert, datum, uhrzeit)
        print("Messung hinzugefügt.")
    elif auswahl == "3":
        index = int(input("Geben Sie die Nummer der Messung ein, die Sie löschen möchten (beginnend bei 1): ")) - 1
        if 0 <= index < len(temperaturen):
            del temperaturen[index]
            print("Messung gelöscht.")
        else:
            print("Ungültige Nummer.")
    elif auswahl.upper() == "E":
        with open("temps.txt", "w", encoding="utf-8") as datei:
            for messung in temperaturen:
                datei.write(f"{messung.wert} {messung.datum.replace('.', '-')} {messung.uhrzeit}Uhr\n")
        print("Daten gespeichert. Programm wird beendet.")
        break
    else:
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

