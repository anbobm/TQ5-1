# Aufgabe 1-2_Unternehmen_var.2_2026_03_06

import random


class Unternehmen:

    def __init__(self, name: str):
        self.name = name
        self.abteilungen = []

    def abteilung_hinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    def abteilung_entfernen(self, abteilung):
        if abteilung in self.abteilungen:
            self.abteilungen.remove(abteilung)


# ---------- AUFGABE 2 ----------

    def abteilung_finden(self, bezeichnung):
        for abteilung in self.abteilungen:
            if abteilung.bezeichnung == bezeichnung:
                return abteilung
        return None

    def alle_mitarbeiter_anzeigen(self):
        for abteilung in self.abteilungen:
            print("Abteilung:", abteilung.bezeichnung)
            for mitarbeiter in abteilung.mitarbeiter:
                print("   ", mitarbeiter.personalnummer, mitarbeiter.name)

    def mitarbeiter_suchen(self, personalnummer):
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.personalnummer == personalnummer:
                    return mitarbeiter
        return None


class Abteilung:

    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.mitarbeiter = []

    def mitarbeiter_hinzufügen(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def mitarbeiter_entfernen(self, mitarbeiter):
        if mitarbeiter in self.mitarbeiter:
            self.mitarbeiter.remove(mitarbeiter)


class Mitarbeiter:

    def __init__(self, personalnummer, name):
        self.personalnummer = personalnummer
        self.name = name


unternehmen = Unternehmen("TQ5 GmbH")


abteilungen = [
    Abteilung("Entwicklung"),
    Abteilung("Vertrieb"),
    Abteilung("Produktion"),
    Abteilung("Buchhaltung")
]


mitarbeiter = [
    Mitarbeiter("001", "Tunahan"),
    Mitarbeiter("002", "Anne"),
    Mitarbeiter("003", "Katja"),
    Mitarbeiter("004", "Mohamad"),
    Mitarbeiter("005", "Sebastian"),
    Mitarbeiter("006", "Ihor"),
    Mitarbeiter("007", "Ruwen"),
    Mitarbeiter("008", "Nataliya"),
    Mitarbeiter("009", "Andreas"),
    Mitarbeiter("010", "Efkan")
]


# Abteilungen hinzufügen
for abteilung in abteilungen:
    unternehmen.abteilung_hinzufügen(abteilung)


# Beispiel: zusätzlicher Mitarbeiter
mitarbeiter1 = Mitarbeiter("M023", "Paula Pause")

abteilung1 = Abteilung("Pause")

abteilung1.mitarbeiter_hinzufügen(mitarbeiter1)


# Mitarbeiter zufällig verteilen
for mitarbeiter in mitarbeiter:
    zufällige_abteilung = random.choice(unternehmen.abteilungen)
    zufällige_abteilung.mitarbeiter_hinzufügen(mitarbeiter)

# -----Test----
print("\n--- Alle Mitarbeiter im Unternehmen ---")
unternehmen.alle_mitarbeiter_anzeigen()

print("\n--- Abteilung finden ---")
a = unternehmen.abteilung_finden("Vertrieb")
if a:
    print("Gefunden:", a.bezeichnung)

print("\n--- Mitarbeiter suchen ---")
m = unternehmen.mitarbeiter_suchen("003")
if m:
    print("Gefunden:", m.name)