# Aufgabe 2 - Sequenzdiagramm mit Alternative
# Gegeben sind folgende Klassen und ihre Verwendung im Hauptprogramm.

# Zeichne ein Sequenzdiagramm für den Aufruf anne.freitag_starten(). Benutze das alt-Fragment, um alternative Abläufe darzustellen.

class CocktailEnthusiast:
    def __init__(self, bar):
        self.bar = bar

    def freitag_starten(self):
        # ...
        self.cocktails_trinken()
        # ...
    
    def cocktails_trinken(self):
        # ...
        promille = self.bar.mojito()

        if promille > 1.0:
            self.verabschieden()
        else:
            self.bar.long_island_ice_tea()
        # ...
    
    def verabschieden(self):
        # ...
        return

class Cocktailbar:
    def mojito(self):
        return ...
    
    def long_island_ice_tea(self):
        # ...
        return
    
    def eierlikör(self):
        # ...
        return

bar1 = Cocktailbar()
anne = CocktailEnthusiast(bar1)

anne.freitag_starten()
