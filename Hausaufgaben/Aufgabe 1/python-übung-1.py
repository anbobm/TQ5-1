lager = {}

def hinzufuegen(artikel, menge):
    if artikel not in lager:
        lager[artikel] = menge
    else:
        lager[artikel] += menge

    print(f"{menge} von {artikel} hinzugefügt. Neuer Bestand: {lager[artikel]}")

def entfernen(artikel, menge):
    if artikel in lager and lager[artikel] >= menge:
        lager[artikel] -= menge
        print(f"{menge} von {artikel} entfernt. Neuer Bestand: {lager[artikel]}")

        if lager[artikel] == 0:
            del lager[artikel]
    else:
        print(f"Nicht genügend Bestand von {artikel} oder Artikel nicht vorhanden.")

# Beispiel
hinzufuegen("Rot", 5)
hinzufuegen("Rot", 5)
hinzufuegen("Rot", 5)
hinzufuegen("Rot", 5)

entfernen("Rot", 5)
entfernen("Rot", 5)
entfernen("Rot", 5)
entfernen("Rot", 5)

