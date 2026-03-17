# # Aufgabe 1
eingabe = open('C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\input.txt', 'r')
inhalt = eingabe.read()
eingabe.close()

ausgabe = open('C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\lange_wörter.txt', 'w')
wörter = inhalt.split()

for wort in wörter:
    if len(wort) > 5:
        ausgabe.write(wort + '\n')
ausgabe.close()

#Aufgabe 2
Eingabe = input('Geben Sie einen Satz ein: ')
Ausgabe = print(Eingabe.rstrip("bar"))


# Aufgabe 3
with open('dates.txt', 'r') as eingabe:
    inhalt = eingabe.read()

zeilen = inhalt.split()

with open('dates_output.txt', 'w') as ausgabe:
    for zeile in range(0, len(zeilen), 2):
        ausgabe.write(f"Datum: {zeilen[zeile]}, \nUhrzeit: {zeilen[zeile + 1].rstrip('Uhr')}\n")

#Aufgabe 4
with open('dates.txt', 'r') as eingabe:
    inhalt = eingabe.read()

zeilen = inhalt.split()
date = []
for i in range(0, len(zeilen), 2):
    date.append(zeilen[i])

anzahl = 0
with open('dates_output2.txt', 'w') as ausgabe:
    for zeile in range(0, len(zeilen), 2):
        d = zeilen[zeile].replace('-', '.')
        d = d.split(".")
        date = ".".join(reversed(d))
        ausgabe.write(f"Datum: {date}, \nUhrzeit: {zeilen[zeile + 1].rstrip('Uhr')}\n")
        

