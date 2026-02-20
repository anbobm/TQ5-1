#Erstelle eine Klasse Bankkonto mit den Attributen inhaber (String, anfangs "")  und kontostand (Ganzzahl, anfangs 0).
#Erzeuge anschließend zwei Objekte aus dieser Klasse und gib ihren Attributen konkrete Werte.
class Bankkonto:
    def __init__(self, inhaber, kontostand):
        self._inhaber = ""
        self._kontostand = kontostand

    def get_inhaber(self):
        return self._inhaber
    
    def set_inhaber(self, inhaber):
        self._inhaber = inhaber

    def ausgeben(self):
        print(f"Inhaber: {self._inhaber}, Kontostand: {self._kontostand} Euro")
        return f"Inhaber: {self._inhaber}, Kontostand: {self._kontostand} Euro"  

    def einzahlen(self, betrag):
        if betrag > 0:
            self._kontostand += betrag
        else:
            print("Der Einzahlungsbetrag muss positiv sein.")
    
    def auszahlen(self, betrag):
        if betrag <= self._kontostand:
            self._kontostand -= betrag
        else:
            print("Nicht genügend Guthaben vorhanden.")

# Erzeuge zwei Objekte der Klasse Bankkonto
konto1 = Bankkonto("", 100)
konto1.set_inhaber("Max")  # Setze den Inhaber für konto1
konto2 = Bankkonto("", 250)
konto2.set_inhaber("Lisa")  # Setze den Inhaber für konto2
print(konto1.ausgeben())  # Ausgabe: Max


# Gib die Attribute der Objekte aus
# konto1.ausgeben()
# konto1.einzahlen(50)  
# konto1.auszahlen(70)
# konto1.ausgeben()
# konto2.ausgeben()