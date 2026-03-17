#Schreibe ein Python-Skript, welches einen Satz vom Benutzer einliest (z.B. "The quick brown fox jumps over the lazy dog") und dann zählt, wie viele Wörter in diesem String sind.

# satz = input("Bitte geben Sie einen Satz ein: ")

# woerter = satz.split()
# anzahl_woerter = len(woerter)
# print("Die Anzahl der Wörter in Ihrem Satz ist:", anzahl_woerter)

# #Es gibt eine Datei foobar.txt mit folgendem Inhalt. Zähle die Wörter in dieser Datei mit einem Python-Skript.

# # dateiname = 'foobar.txt'
# # with open(dateiname, 'r') as datei:
# #     inhalt = datei.read()
# #     woerter_in_datei = inhalt.split()
# #     anzahl_woerter_in_datei = len(woerter_in_datei)
# #     print("Die Anzahl der Wörter in der Datei ist:", anzahl_woerter_in_datei)

# datei = open(r'C:\Users\Sebas\Desktop\TQ5\Repo\TQ5-1\foobar2.txt', 'r')
# inhalt = datei.read()
# woerter_in_datei = inhalt.split()
# anzahl_woerter_in_datei = len(woerter_in_datei)
# print("Die Anzahl der Wörter in der Datei ist:", anzahl_woerter_in_datei)
# datei.close()

# with open(r'C:\Users\Sebas\Desktop\TQ5\Repo\TQ5-1\foobar2.txt', 'r') as datei:
#     inhalt = datei.read()
#     woerter_in_datei = inhalt.split()
#     anzahl_woerter_in_datei = len(woerter_in_datei)
#     anzahl_woerter_in_datei = anzahl_woerter_in_datei // 2
#     print("Die Anzahl der Wörter in der Datei ist:", anzahl_woerter_in_datei)


# Aufgabe 4
datei = open("C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\person.txt", "w")

weiter = "j"
while weiter == "j":
    vorname = input("Vorname? ")
    nachname = input("Nachname? ")
    alter = input("Alter? ")
    datei.write(f"{vorname},{nachname},{alter}\n")

    weiter = input("Weiter? (j/n)")

datei.close()

# Aufgabe 5
datei = open("C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\person.txt", "r")
personen = [{}]
for zeile in datei:
    vorname, nachname, alter = zeile.strip().split(",")
    personen.append({"Vorname": vorname, "Nachname": nachname, "Alter": alter})
datei.close()
print(personen)