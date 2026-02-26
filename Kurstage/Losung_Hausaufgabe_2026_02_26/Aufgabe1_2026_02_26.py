# Aufgabe Produkt

class Produkt:
    def __init__(self, name, preis):
        self._name = name
        self._preis = preis
        self._lagerbestand = 0

    def verkaufen(self, menge):
        # nur positive Stückzahlen zulässig
        if menge <= 0:
            return  

        # nur verkaufen, wenn Lagerbestand reicht
        if menge > self._lagerbestand:
            return

        self._lagerbestand = self._lagerbestand - menge

    def nachbestellen(self, menge):
        # nur positive Stückzahlen zulässig
        if menge <= 0:
            return

        self._lagerbestand = self._lagerbestand + menge

    def set_preis(self, neuer_preis):
        # keine negativen Preise zulässig
        if neuer_preis < 0:
            return

        self._preis = neuer_preis

    def get_info(self):
        return (
            f"Name: {self._name}," 
            f"Preis: {self._preis}," 
            f"Lagerbestand: {self._lagerbestand}")

        # --- Test ---
produkt1 = Produkt("Apfel", 1.5)

produkt1.nachbestellen(10)
produkt1.verkaufen(3)
produkt1.set_preis(1.8)

print(produkt1.get_info())


