# # Aufgabe 1
# # Schreibe ein Python-Skript, das vom Benutzer ein Wort eingeben lässt, und anschließend die Häufigkeit jedes Buchstabens in diesem Wort in einem Dictionary zählt und anschließend ausgibt:

# # Gib ein Wort ein: Tassenhenkel

# # T kommt 1 mal vor
# # a kommt 1 mal vor
# # s kommt 2 mal vor
# # e kommt 3 mal vor
# # n kommt 2 mal vor
# # h kommt 1 mal vor
# # k kommt 1 mal vor
# # l kommt 1 mal vor
# # Erinnerung: In Python kann man Strings wie Listen behandeln, also z.B. elementweise durchlaufen in einer for-Schleife.

# dict = {}
# wort = input("Denke dir ein Wort aus: ")
# for i in wort:
#     if i in dict:
#         dict[i] = dict[i] + 1
#     else:
#         dict[i] = 1
# for letter in dict:
#     print(letter, "kommt", dict[letter], "mal vor")       
    




# Aufgabe 2
# Es gibt ein Dictionary, das den Lagerbestand in einem Geschäft festhält und zu Beginn folgenden Zustand hat:

# lager = {
#     "Apfel": {"preis": 2, "menge": 10},
#     "Banane": {"preis": 1, "menge": 8},
#     "Orange": {"preis": 3, "menge": 5}
# }
# Der Benutzer soll nun ein Menü angezeigt bekommen und auswählen was er tun möchte:

# 1: Kompletten Lagerbestand anzeigen
# 2: Lagerbestand von einem Artikel anzeigen
# 3: Menge von Artikeln entfernen (Verkauf)
# 4: Menge von Artikeln zufügen (Einkauf)
# 5: Artikel löschen
# Nach der Eingabe:

# Wenn der Benutzer 1 eingibt, dann soll die Ausgabe in dieser Art erfolgen:

#     Artikel Apfel: Preis 2, Menge: 10
#     Artikel Banane: Preis 1, Menge: 8
#     ...
# Wenn der Benutzer 2 eingibt, dann soll der Benutzer gefragt werden, welcher Artikel angezeigt werden soll und dieser dann Ausgegeben werden:

# Welcher Artikel? Orange
# Preis: 3
# Menge: 5
# Wenn der Benutzer 3 eingibt, dann soll nach dem Artikel und nach der Stückzahl gefragt werden, die aus dem Lagerbestand des jeweiligen Artikels entfernt werden sollen:

# Welcher Artikel? Banane
# Wie viele entnehmen? 3
# 3 Stück entnommen.
# Es sind noch 5 übrig.
# Wenn der Benutzer mehr entnehmen will als es gibt, soll "Nicht genug vorrätig" ausgegeben werden und nichts entnommen werden.

# Wenn der Benutzer 4 eingibt, dann soll nach dem hinzuzufügenden Artikel und der Menge gefragt werden, und der neue Lagerbestand ausgegeben werden:

# Welcher Artikel? Apfel
# Wie viele hinzufügen? 5
# Es sind jetzt 15 vorrätig.
# Wenn der Artikel im Dictionary nicht vorkommt, dann soll er angelegt werden.

# Wenn der Benutzer eine 5 eingibt, dann wird nach dem Artikel gefragt und anschließend die Menge auf 0 gesetzt:

# Welcher Artikel? Apfel
# Lagerbestand auf 0 gesetzt.
# Immer wenn der Nutzer nach einem Artikel gefragt wird und dann einen eingibt, der nicht im Lager vorhanden ist, soll ausgegeben werden "Artikel nicht vorhanden" und sonst nichts getan werden (außer beim Hinzufügen im Menü 4)

# Nachdem du das erfolgreich umgesetzt hast, füge noch einen 6. Menüpunkt "Ende" hinzu, und lasse in einer Schleife den Benutzer immer wieder fragen, welchen Menüpunkt er ausführen will, bis er eine 6 eingibt und das Programm beendet wird.

lager = {
    "Apfel": {"preis": 2, "menge": 10},
    "Banane": {"preis": 1, "menge": 8},
    "Orange": {"preis": 3, "menge": 5}
}

print("Was möchtest du tun?")
print("")
print("1: Kompletten Lagerbestand anzeigen")
print("2: Lagerbestand von einem Artikel anzeigen")
print("3: Menge von Artikeln entfernen (Verkauf)")
print("4: Menge von Artikeln zufügen (Einkauf)")
print("5: Artikel löschen")
print("6: Ende")

menue = int(input("Gib die Nummer des Menüpunkts ein: "))
if menue == 1:
    for i in lager:
        print("Artikel", i, ": Preis", lager[i]["preis"], ", Menge:", lager[i]["menge"])   
elif menue == 2:
    artikel = input("Welcher Artikel? ")
    if artikel in lager:
        print("Preis:", lager[artikel]["preis"])
        print("Menge:", lager[artikel]["menge"])
    else:
        print("Artikel nicht vorhanden")
elif menue == 3:
    artikel = input("Welcher Artikel? ")
    if artikel in lager:
        menge = int(input("Wie viele entnehmen? "))
        if menge <= lager[artikel]["menge"]:
            lager[artikel]["menge"] = lager[artikel]["menge"] - menge
            print(menge, "Stück entnommen.")
            print("Es sind noch", lager[artikel]["menge"], "übrig.")
        else:
            print("Nicht genug vorrätig")
    else:
        print("Artikel nicht vorhanden")
elif menue == 4:
    artikel = input("Welcher Artikel? ")
    menge = int(input("Wie viele hinzufügen? "))
    if artikel in lager:
        lager[artikel]["menge"] = lager[artikel]["menge"] + menge
        print("Es sind jetzt", lager[artikel]["menge"], "vorrätig.")
    else:
        print("Artikel nicht vorhanden.")
elif menue == 5:
    artikel = input("Welcher Artikel? ")
    if artikel in lager:
        del lager[artikel]
        print("Artikel gelöscht.")
    else:
        print("Artikel nicht vorhanden")
elif menue == 6:
    print("Programm wird beendet.")
else:
    print("Ungültige Eingabe")
