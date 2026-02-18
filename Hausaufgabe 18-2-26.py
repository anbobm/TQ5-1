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
    print(lager)
elif Auswahl == "2":
    Artikel = input("Gib den Namen des Artikels ein: ")
    if Artikel in lager:
        print(lager[Artikel])
    else:
        print("Der Artikel existiert nicht")
elif Auswahl == "3":
    Artikel = input("Gib den Namen des Artikels ein: ")
    Menge = int(input("Gib die Menge ein, die entfernt werden soll: "))
    if Artikel in lager:
        if Menge <= lager[Artikel]["menge"]:
            lager[Artikel]["menge"] = lager[Artikel]["menge"] - Menge
            print(lager[Artikel])
        else:
            print("Nicht genügend Menge vorhanden")
    else:
        print("Der Artikel existiert nicht")
elif Auswahl == "4":
    Artikel = input("Gib den Namen des Artikels ein: ")
    Menge = int(input("Gib die Menge ein, die hinzugefügt werden soll: "))
    if Artikel in lager:
        lager[Artikel]["menge"] = lager[Artikel]["menge"] + Menge
        print(lager[Artikel])
    else:
        print("Der Artikel existiert nicht")
elif Auswahl == "5":
    Artikel = input("Gib den Namen des Artikels ein: ")
    if Artikel in lager:
        del lager[Artikel]
        print(lager)
    else:
        print("Der Artikel existiert nicht")