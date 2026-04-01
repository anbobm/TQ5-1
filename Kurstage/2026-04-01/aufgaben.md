# Aufgabe 1

Zeichne ein Klassendiagramm für folgende Klassen (mit Vererbung, Aggregation, Assoziation):

```python
class Fahrzeug:
    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def starten(self):
        print("Fahrzeug startet")


class Auto(Fahrzeug):
    def __init__(self, marke, baujahr, anzahl_tueren):
        super().__init__(marke, baujahr)
        self.anzahl_tueren = anzahl_tueren

    def hupen(self):
        print("Hup Hup!")


class Fahrrad(Fahrzeug):
    def __init__(self, marke, baujahr, typ):
        super().__init__(marke, baujahr)
        self.typ = typ

    def klingeln(self):
        print("Ring Ring!")


class Garage:
    def __init__(self, name):
        self.name = name
        self.fahrzeuge = []

    def add_fahrzeug(self, fahrzeug):
        self.fahrzeuge.append(fahrzeug)

    def liste_fahrzeuge(self):
        for f in self.fahrzeuge:
            print(f.marke)


class Besitzer:
    def __init__(self, name):
        self.name = name
        self.garage = None

    def set_garage(self, garage):
        self.garage = garage
```