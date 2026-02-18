# Aufgabe 1
# Schreibe ein Python-Skript, das vom Benutzer ein Wort eingeben lässt, 
# und anschließend die Häufigkeit jedes Buchstabens 
# in diesem Wort in einem Dictionary zählt und anschließend ausgibt:

# Gib ein Wort ein: Tassenhenkel

# T kommt 1 mal vor
# a kommt 1 mal vor
# s kommt 2 mal vor
# e kommt 3 mal vor
# n kommt 2 mal vor
# h kommt 1 mal vor
# k kommt 1 mal vor
# l kommt 1 mal vor
# Erinnerung: In Python kann man Strings wie Listen behandeln, also z.B. elementweise
# durchlaufen in einer for-Schleife.

# Lösung Aufgabe 1

wort = "kaffeevollautomat"

haeufigkeit = {}

for buchstabe in wort:
    if buchstabe in haeufigkeit:
        haeufigkeit[buchstabe] += 1
    else:
        haeufigkeit[buchstabe] = 1

for buchstabe, anzahl in haeufigkeit.items():
    print(f"{buchstabe} kommt {anzahl} mal vor")


# Aufgabe 2
# Es gibt ein Dictionary, das den Lagerbestand in einem Geschäft festhält 
# und zu Beginn folgenden Zustand hat:

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
# Wenn der Benutzer 3 eingibt, dann soll nach dem 
# Artikel und nach der Stückzahl gefragt werden, die aus dem Lagerbestand
# des jeweiligen Artikels entfernt werden sollen:

# Welcher Artikel? Banane
# Wie viele entnehmen? 3
# 3 Stück entnommen.
# Es sind noch 5 übrig.
# Wenn der Benutzer mehr entnehmen will als es gibt, soll "Nicht genug vorrätig"
# ausgegeben werden und nichts entnommen werden.

# Wenn der Benutzer 4 eingibt, dann soll nach dem hinzuzufügenden Artikel und der 
# Menge gefragt werden, und der neue Lagerbestand ausgegeben werden:

# Welcher Artikel? Apfel
# Wie viele hinzufügen? 5
# Es sind jetzt 15 vorrätig.
# Wenn der Artikel im Dictionary nicht vorkommt, dann soll er angelegt werden.

# Wenn der Benutzer eine 5 eingibt, dann wird nach dem Artikel gefragt und 
# anschließend die Menge auf 0 gesetzt:

# Welcher Artikel? Apfel
# Lagerbestand auf 0 gesetzt.
# Immer wenn der Nutzer nach einem Artikel gefragt wird und dann einen eingibt,
# der nicht im Lager vorhanden ist, soll ausgegeben werden "Artikel nicht vorhanden" 
# und sonst nichts getan werden (außer beim Hinzufügen im Menü 4)

# Nachdem du das erfolgreich umgesetzt hast, füge noch einen 6. Menüpunkt "Ende"
# hinzu, und lasse in einer Schleife den Benutzer immer wieder fragen, welchen Menüpunkt
# er ausführen will, bis er eine 6 eingibt und das Programm beendet wird.

# Lösung Aufgabe 2

lager = {
    "Apfel": {"preis": 2, "menge": 10},
    "Banane": {"preis": 1, "menge": 8},
    "Orange": {"preis": 3, "menge": 5}
}

while True:
    print("\n--- Lager-Menü ---")
    print("1: Lagerbestand anzeigen")
    print("2: Lagerbestand der Artikel anzeigen")
    print("3: Menge von Artikeln wird entfernt")
    print("4: Menge von Artikeln wird zugefügt")
    print("5: Artikel wird gelöscht")
    print("6: Auf Wiedersehen")
    
    auswahl = input("Wie kann ich helfen? ")

    if auswahl == "1":
        for artikel, daten in lager.items():
            print(f"Artikel {artikel}: Preis {daten['preis']}, Menge: {daten['menge']}")

    elif auswahl == "2":
        artikel = input("Welches Obst darf es sein? ")
        if artikel in lager:
            print(f"Preis: {lager[artikel]['preis']}")
            print(f"Menge: {lager[artikel]['menge']}")
        else:
            print("Artikel ist leider nicht vorhanden")

    elif auswahl == "3":
        artikel = input("Wie kann ich helfen? ")
        if artikel in lager:
            menge_weg = int(input("Wie viele entnehmen? "))
            if menge_weg <= lager[artikel]["menge"]:
                lager[artikel]["menge"] -= menge_weg
                print(f"{menge_weg} Stück entnommen.")
                print(f"Es sind noch {lager[artikel]['menge']} übrig.")
            else:
                print("Nicht genug vorrätig")
        else:
            print("Artikel nicht vorhanden")

    elif auswahl == "4":
        artikel = input("Welcher Artikel? ")
        menge_dazu = int(input("Wie viele hinzufügen? "))
        
        if artikel in lager:
            lager[artikel]["menge"] += menge_dazu
            print(f"Es sind jetzt {lager[artikel]['menge']} vorrätig.")
        else:
            # Falls der Artikel neu ist, legen wir einen Standardpreis fest
            preis = int(input(f"{artikel} ist neu. Bitte Preis festlegen: "))
            lager[artikel] = {"preis": preis, "menge": menge_dazu}
            print(f"Artikel {artikel} wurde neu angelegt.")

    elif auswahl == "5":
        artikel = input("Welcher Artikel? ")
        if artikel in lager:
            lager[artikel]["menge"] = 0
            print("Lagerbestand auf 0 gesetzt.")
        else:
            print("Artikel nicht vorhanden")

    elif auswahl == "6":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Eingabe, bitte versuchen Sie es erneut.")