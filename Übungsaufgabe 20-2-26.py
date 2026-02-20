#Erstelle eine Klasse Bankkonto mit den Attributen inhaber (String, anfangs "")  und kontostand (Ganzzahl, anfangs 0).
#Erzeuge anschließend zwei Objekte aus dieser Klasse und gib ihren Attributen konkrete Werte.
class Bankkonto:
    def __init__(self, inhaber, kontostand):
        self.inhaber = ""
        self.kontostand = kontostand
      

    def ausgeben(self):
        print(f"Inhaber: {self.inhaber}, Kontostand: {self.kontostand} Euro")

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
        else:
            print("Der Einzahlungsbetrag muss positiv sein.")
    
    def auszahlen(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag
        else:
            print("Nicht genügend Guthaben vorhanden.")

# Erzeuge zwei Objekte der Klasse Bankkonto
konto1 = Bankkonto("Max", 100)
konto1.inhaber = "Max"  # Setze den Inhaber für konto1
print(konto1.inhaber)  # Ausgabe: Max
konto2 = Bankkonto("Lisa", 250)

# Gib die Attribute der Objekte aus
konto1.ausgeben()
konto1.einzahlen(50)  
konto1.auszahlen(70)
konto1.ausgeben()
konto2.ausgeben()