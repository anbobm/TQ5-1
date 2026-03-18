# Aufgabe 2: rstrip()
# Der Benutzer soll irgendetwas eingeben und von diesem Eingabe-String soll dann die Endung bar, sofern vorhanden, entfernt und der Rest ausgegeben werden. z.B.:

# Eingabe? foobar
# Ausgabe: foo

# Eingabe? foobarbar
# Ausgabe: foobar

# Eingabe? Ich zahle bar
# Ausgabe: Ich zahle 

# Eingabe? Ich zahle bar.
# Ausgabe: Ich zahle bar.

# eingabe = input("Gib etwas ein: ")
# ausgabe = eingabe.rstrip("bar") # removesuffix("bar") nimmt nur 1x bar weg, während strip alle Zeichen in irgendeiner Kombi wegschneidet

# print(ausgabe)




# Aufgabe 3: split(), rstrip()
# Es ist eine Datei dates.txt gegeben. In dieser stehen Zeitpunkte, pro Zeile einer, mit Datum und Uhrzeit, z.B.:

# 2026-3-22 10:24Uhr
# 2026-3-4 22:42Uhr
# ...
# Diese Datei soll eingelesen werden und aus den Zeitpunkten eine Datei formatted_dates.txt generiert werden, die folgendes Format haben soll:

# Datum: 2026-3-22
# Uhrzeit: 10:24

# Datum: 2026-3-4
# Uhrzeit: 22:42


# datumsliste = []
# datei = open("20260317_dates.txt")
# datei2 = open("20260317_formatted_dates.txt", "w")

# for zeile in datei:
#         datum, uhrzeit = zeile.strip().split(" ")
#         date = {
#             "Datum": datum,
#             "Uhrzeit": uhrzeit.rstrip("Uhr")
#         }
#         datumsliste.append(date)
        
#         datei2.write(f"Datum: {datum}\nUhrzeit: {uhrzeit.rstrip("Uhr")}\n\n")

# print(datumsliste)
# datei.close()




# Aufgabe 4
# Wie Aufgabe 3. Die gleiche Datei dates.txt soll genutzt werden, aber das Format von formatted_dates.txt soll so aussehen (Datumsformat jetzt Tag.Monat.Jahr anstelle von Jahr-Monat-Tag):

# Datum: 22.3.2026
# Uhrzeit: 10:24

# Datum: 4.3.2026
# Uhrzeit: 22:42
# from datetime import datetime
# datumsliste = []
# datei = open("20260317_dates.txt")
# datei2 = open("20260317_formatted_dates.txt", "w")

# for zeile in datei:
#         datum, uhrzeit = zeile.strip().split(" ")
#         jahr, monat, tag = datum.split("-")
#         date = {
#             "Datum": datum,
#             "Uhrzeit": uhrzeit.rstrip("Uhr")
#         }
#         datumsliste.append(date)
        
#         datei2.write(f"Datum: {tag}.{monat}.{jahr}\nUhrzeit: {uhrzeit.rstrip("Uhr")}\n\n")

# print(datumsliste)
# datei.close()

# Aufgabe 5
# formatted_temps.txt:

# Temperatur: 23.2 °C
# Datum: 22.3.2026
# Uhrzeit: 10:24

# Temperatur: 6.0 °C
# Datum: 4.3.2026
# Uhrzeit: 22:42
from datetime import datetime
datumsliste = []
datei = open("20260318_temperaturen.txt")
datei2 = open("20260318_formatted_temperaturen.txt", "w", encoding="utf-8")

for zeile in datei:
        temp, datum, uhrzeit = zeile.strip().split(" ")
        jahr, monat, tag = datum.split("-")
        date = {
            "Datum": datum,
            "Uhrzeit": uhrzeit.rstrip("Uhr")
        }
        datumsliste.append(date)
        
        datei2.write(f"Temperatur: {temp}°C\nDatum: {tag}.{monat}.{jahr}\nUhrzeit: {uhrzeit.rstrip("Uhr")}\n\n")

print(datumsliste)
datei.close()