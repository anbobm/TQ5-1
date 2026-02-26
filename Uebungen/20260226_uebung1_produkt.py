# Aufgabe 1
# Schreibe eine Klasse Produkt mit privaten Attributen für Name, Preis und Lagerbestand.

# Sie soll außerdem folgende Methoden haben:

# verkaufen(menge): Eine Stückzahl menge des Produkts wird verkauft (nur positive Stückzahlen zulässig), allerdings nur wenn es der Lagerbestand zulässt.
# nachbestellen(menge): Eine Stückzahl menge des Produkts wird nachbestellt. Nur positive Stückzahlen zulässig.
# set_preis(neuer_preis): Keine negativen Preise zulässig
# get_info(): gibt String mit allen Infos zum Produkt zurück

class Produkt:
    def __init__(self, name, preis, lagerbestand):
        self._name = name
        self._preis = preis
        self._lagerbestand = lagerbestand
        
    def verkaufen(self, menge):
        if menge > self._lagerbestand:
            print("Bestand nicht vorrätig")
        else:
            self._lagerbestand = self._lagerbestand - menge
            print(f"{menge} verkauft. Es sind noch {self._lagerbestand} auf Lager.")
    
    def nachbestellen(self, menge):
        if menge <= 0:
            print("Bitte nur positive Bestellmengen angeben")
        else:
            self._lagerbestand = self._lagerbestand + menge
            print(f"{menge} nachbestellt. Neuer Lagerbestand: {self._lagerbestand}")
            
    def set_preis(self, neuer_preis):
        if neuer_preis < 0:
            print("Der Preis darf nicht unter 0 liegen.")
        else:
            self._preis = neuer_preis
            print(f"Preis auf {neuer_preis} gesetzt.")
            
    def get_info(self):
        print(f"Produktname: {self._name}, Preis: {self._preis}, Lagerbestand: {self._lagerbestand} Stück")
        
produkt1 = Produkt("Kaugummi", 2, 85)
produkt2 = Produkt("China-Vasen", 395, 3)
produkt3 = Produkt("Sitzerhöhung", 15, 30)

produkt1.get_info()
produkt2.get_info()
produkt3.get_info()

produkt1.verkaufen(6)
produkt2.verkaufen(6)
produkt2.nachbestellen(17)

produkt1.get_info()
produkt2.get_info()
produkt3.get_info()