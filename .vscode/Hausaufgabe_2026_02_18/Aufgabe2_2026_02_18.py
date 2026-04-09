# Aufgabe 1
# Schreibe ein Python-Skript, das vom Benutzer ein Wort eingeben lässt, und anschließend die Häufigkeit jedes Buchstabens in diesem Wort in einem Dictionary zählt und anschließend ausgibt:
# Gib ein Wort ein: Tassenhenkel
# T kommt 1 mal vor
# a kommt 1 mal vor
# s kommt 2 mal vor
# e kommt 3 mal vor
# n kommt 2 mal vor
# h kommt 1 mal vor
# k kommt 1 mal vor
# l kommt 1 mal vor
# Erinnerung: In Python kann man Strings wie Listen behandeln, also z.B. elementweise durchlaufen in einer for-Schleife.

# wort = input("Gib ein Wort ein: ")

# häufigkeiten = {}

# for buchstabe in wort:
#     if buchstabe in häufigkeiten:
#         häufigkeiten[buchstabe] = häufigkeiten[buchstabe] + 1
#     else:
#         häufigkeiten[buchstabe] = 1

# for buchstabe in häufigkeiten:
#     print(f"{buchstabe} kommt {häufigkeiten[buchstabe]} mal vor")

    
# Aufgabe 2

lager = {
    "Apfel": {"preis": 2, "menge": 10},
    "Banane": {"preis": 1, "menge": 8},
    "Orange": {"preis": 3, "menge": 5}
}

while True:
    print("1: Kompletten Lagerbestand anzeigen")
    print("2: Lagerbestand von einem Artikel anzeigen")
    print("3: Menge von Artikeln entfernen (Verkauf)")
    print("4: Menge von Artikeln zufügen (Einkauf)")
    print("5: Artikel löschen")
    print("6: Ende")

    menu = input()

    if menu == "1":
        for artikel in lager:
            preis = lager[artikel]["preis"]
            menge = lager[artikel]["menge"]

            print(f"Artikel {artikel}: Preis {preis}, Menge: {menge}")
    elif menu == "2":
        artikel = input("Welcher Artikel? ")

        if artikel in lager:
            preis = lager[artikel]["preis"]
            menge = lager[artikel]["menge"]
            print(f"Preis: {preis}")
            print(f"Menge: {menge}")
        else:
            print("Artikel nicht vorhanden")
    elif menu == "3":
        artikel = input("Welcher Artikel? ")
        anzahl = int(input("Wie viele entnehmen? "))

        if artikel in lager:
            menge = lager[artikel]["menge"]
            if menge >= anzahl:
                neue_menge = menge - anzahl
                lager[artikel]["menge"] = neue_menge
                print(f"{anzahl} Stück entnommen")
                print(f"Es sind noch {neue_menge} übrig.")
            else:
                print("Nicht genug vorrätig")
        else:
            print("Artikel nicht vorhanden")
    elif menu == "4":
        artikel = input("Welcher Artikel? ")
        anzahl = int(input("Wie viele hinzufügen? "))

        if artikel in lager:
            menge = lager[artikel]["menge"]
            neue_menge = menge + anzahl
            lager[artikel]["menge"] = neue_menge
            print(f"Es sind jetzt {neue_menge} vorrätig.")
        else:
            print("Artikel nicht vorhanden")
    elif menu == "5":
        artikel = input("Welcher Artikel? ")

        if artikel in lager:
            lager[artikel]["menge"] = 0
            print("Lagerbestand auf 0 gesetzt.")
        else:
            print("Artikel nicht vorhanden")
    elif menu == "6":
        break