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
# ausgabe = eingabe.rstrip("bar")

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


datumsliste = []
datei = open("20260317_dates.txt")
datei2 = open("20260317_formatted_dates.txt", "x")

for zeile in datei:
        datum, uhrzeit = zeile.strip().split(" ")
        date = {
            "Datum": datum.strip(),
            "Uhrzeit": uhrzeit.strip("Uhr")
        }
        datumsliste.append(date)
        
        datei2.write(f"Datum: {datum}\nUhrzeit: {uhrzeit}\n")

print(datumsliste)
datei.close()

# ...
# dates.txt:

# 2026-3-22 10:24Uhr
# 2026-3-4 22:42Uhr
# 2026-3-28 23:18Uhr
# 2026-7-21 10:25Uhr
# 2026-8-30 22:25Uhr
# 2026-3-24 20:4Uhr
# 2026-4-17 7:51Uhr
# 2026-6-26 23:39Uhr
# 2026-8-24 7:28Uhr
# 2026-5-4 19:48Uhr
# 2026-11-29 18:38Uhr
# 2026-7-18 16:30Uhr
# 2026-10-7 9:17Uhr
# 2026-6-16 19:7Uhr
# 2026-10-14 23:29Uhr
# 2026-2-8 16:34Uhr
# 2026-7-20 14:49Uhr
# 2026-6-15 17:15Uhr
# 2026-2-21 17:51Uhr
# 2026-7-1 3:41Uhr
# 2026-8-5 21:53Uhr
# 2026-7-1 19:16Uhr
# 2026-4-13 2:45Uhr
# 2026-8-10 6:28Uhr
# 2026-8-24 15:54Uhr
# 2026-6-30 0:37Uhr
# 2026-2-13 15:23Uhr
# 2026-2-22 6:47Uhr
# 2026-6-7 12:58Uhr
# 2026-10-1 21:50Uhr





# Aufgabe 4
# Wie Aufgabe 3. Die gleiche Datei dates.txt soll genutzt werden, aber das Format von formatted_dates.txt soll so aussehen (Datumsformat jetzt Tag.Monat.Jahr anstelle von Jahr-Monat-Tag):

# Datum: 22.3.2026
# Uhrzeit: 10:24

# Datum: 4.3.2026
# Uhrzeit: 22:42

# ...