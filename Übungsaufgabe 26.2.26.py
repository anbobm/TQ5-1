class Produkt():
    def __init__(self, Name, Preis):
        self._Name = Name
        self._Preis = Preis
        self._Lagerbestand = 0
    
    def verkaufen(self, menge):
        if self._Lagerbestand >= menge and menge >= 0:
            self._Lagerbestand = self._Lagerbestand - menge
            return
        else:
            return "Der Lagerbestand ist zu niedrig um diese Menge zu verkaufen oder eine -Zahl kann nicht angegeben werden."

    def nachbestellen(self, menge):
        if menge > 0:
            self._Lagerbestand = self._Lagerbestand + menge
            return
        else:
            return "Nichts passiert."
        
    def set_preis(self, neuer_preis):
        if neuer_preis >= 0:
            self._Preis = neuer_preis
            return
        else:
            return "Das ist nicht möglich, da der Preis nicht negativ sein kann."
    
    def get_info(self):
        return (f"Der Produktname ist: {self._Name}, hat den Preis: {self._Preis} und hat den Lagerbestand: {self._Lagerbestand}.")
            

