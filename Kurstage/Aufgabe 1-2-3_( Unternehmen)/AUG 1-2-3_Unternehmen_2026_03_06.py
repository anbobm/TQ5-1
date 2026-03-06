# Augabe 1-2-3_UNTERNEHMEN_2026_03_06
# Aufgabe 1
# Klassen definieren


import random

class Unternehmen:

    def __init__(self, name):
        self.name = name
        self.abteilungen = []   # Liste von Abteilungen

    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    def abteilung_entfernen(self, abteilung):
        self.abteilungen.remove(abteilung)


class Abteilung:

    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = []   # Liste von Mitarbeitern

    def mitarbeiter_hinzufügen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def mitarbeiter_entfernen(self, mitarbeiter):
        self.mitarbeiter.remove(mitarbeiter)


class Mitarbeiter:

    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name


# Aufgabe 2
# Methoden erweitern


class Unternehmen:

    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    def abteilung_entfernen(self, abteilung):
        self.abteilungen.remove(abteilung)

    def abteilung_finden(self, bezeichnung):

        for abteilung in self.abteilungen:

            if abteilung.bezeichnung == bezeichnung:
                return abteilung

        return None

    def alle_mitarbeiter_anzeigen(self):

        for abteilung in self.abteilungen:

            for mitarbeiter in abteilung.mitarbeiter:

                print(f"{mitarbeiter.personalnummer}: {mitarbeiter.name}")

    def mitarbeiter_suchen(self, personalnummer):

        for abteilung in self.abteilungen:

            for mitarbeiter in abteilung.mitarbeiter:

                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter

        return None
    

# Aufgabe 3
# Methode info hinzufügen


    def info(self):

        print(self.name)

        for abteilung in self.abteilungen:

            print(f"  {abteilung.bezeichnung}")

            for mitarbeiter in abteilung.mitarbeiter:

                print(f"    {mitarbeiter.name}")


# Testdaten


unternehmen = Unternehmen("Unternehmen X")


abteilungen = [

    Abteilung("Abteilung A"),
    Abteilung("Abteilung B"),
    Abteilung("Abteilung C")

]


mitarbeiter = [

    Mitarbeiter("001", "Mitarbeiter 1"),
    Mitarbeiter("002", "Mitarbeiter 2"),
    Mitarbeiter("003", "Mitarbeiter 3"),
    Mitarbeiter("004", "Mitarbeiter 4"),
    Mitarbeiter("005", "Mitarbeiter 5"),
    Mitarbeiter("006", "Mitarbeiter 6")
]

# Abteilungen hinzufügen


for abteilung in abteilungen:

    unternehmen.abteilung_hinzufügen(abteilung)


# Mitarbeiter zufällig verteilen


for mitarbeiter in mitarbeiter:

    zufällige_abteilung = random.choice(unternehmen.abteilungen)

    zufällige_abteilung.mitarbeiter_hinzufügen(mitarbeiter)


# Aufgabe 2 testen


print("\n--- Abteilung suchen ---")

gesuchte_abteilung = "Abteilung B"

if unternehmen.abteilung_finden(gesuchte_abteilung):

    print(f"Abteilung {gesuchte_abteilung} gefunden")

else:

    print(f"Abteilung {gesuchte_abteilung} nicht gefunden")


print("\n--- Alle Mitarbeiter anzeigen ---")

unternehmen.alle_mitarbeiter_anzeigen()


print("\n--- Mitarbeiter suchen ---")

personalnummer = "003"


mitarbeiter = unternehmen.mitarbeiter_suchen(personalnummer)

if mitarbeiter:

    print("Mitarbeiter gefunden")

    print(f"Personalnummer: {mitarbeiter.personalnummer}")

    print(f"Name: {mitarbeiter.name}")

else:

    print("Mitarbeiter nicht gefunden")


# Aufgabe 3 testen


print("\n--- Unternehmensstruktur ---")

unternehmen.info()
