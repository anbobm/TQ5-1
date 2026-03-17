# Aufgabe 1
eingabe = open('C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\input.txt', 'r')
inhalt = eingabe.read()
eingabe.close()

ausgabe = open('C:\\Users\\Sebas\\Desktop\\TQ5\\Repo\\TQ5-1\\lange_wörter.txt', 'w')
wörter = inhalt.split()

for wort in wörter:
    if len(wort) > 5:
        ausgabe.write(wort + '\n')
ausgabe.close()



