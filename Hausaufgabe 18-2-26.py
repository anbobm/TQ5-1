# Aufgabe 1
char = []
häufigkeiten = {}
Wort = input("Gib ein Wort ein: ")

for c in Wort:
    char.append(c)

print(char)

for c in char:
    if c in häufigkeiten:
        häufigkeiten[c] = häufigkeiten[c] + 1
    else:
        häufigkeiten[c] = 1
print(häufigkeiten)

# Aufgabe 2
lager = {
    "Apfel": {"preis": 2, "menge": 10},
    "Banane": {"preis": 1, "menge": 8},
    "Orange": {"preis": 3, "menge": 5}
}

Auswahl = input("1: Kompletten Lagerbestand anzeigen\n2: Lagerbestand von einem Artikel anzeigen\n3: Menge von Artikeln entfernen (Verkauf)\n4: Menge von Artikeln zufügen (Einkauf)\n5: Artikel löschen\n")
if Auswahl == "1":
    for artikel in lager:
        print("Artikel:", artikel, "Preis:", str(lager[artikel]["preis"]) + "€", "Menge:", lager[artikel]["menge"])
elif Auswahl == "2":
    Artikel = input("Welcher Artikel: ")
    if Artikel in lager:
        print("Preis:", str(lager[Artikel]["preis"]) + "€")
        print("Menge:", lager[Artikel]["menge"])
    else:
        print("Der Artikel existiert nicht")
elif Auswahl == "3":
    Artikel = input("Welcher Artikel: ")
    Menge = int(input("Wie viele entnehmen? "))
    if Artikel in lager:
        if Menge <= lager[Artikel]["menge"]:
            lager[Artikel]["menge"] = lager[Artikel]["menge"] - Menge
            print("Es sind noch" , lager[Artikel]["menge"], Artikel , "übrig.")
        else:
            print("Nicht genügend Menge vorhanden")
    else:
        print("Der Artikel existiert nicht")
elif Auswahl == "4":
    Artikel = input("Welcher Artikel: ")
    Menge = int(input("Wie viele hinzufügen? "))
    if Artikel in lager:
        lager[Artikel]["menge"] = lager[Artikel]["menge"] + Menge
        print("Es sind jetzt", lager[Artikel]["menge"], Artikel, "vorrätig.")
    else:
        print("Der Artikel existiert nicht")
elif Auswahl == "5":
    Artikel = input("Welcher Artikel:: ")
    if Artikel in lager:
        lager[Artikel]["menge"] = 0
        print("Lagerbestand von", Artikel, "auf 0 gesetzt.")
    else:
        print("Der Artikel existiert nicht")