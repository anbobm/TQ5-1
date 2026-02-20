# Aufgabe
 
# Erstelle eine Klasse Bankkonto mit den Attributen inhaber (String, anfangs "")  und kontostand (Ganzzahl, anfangs 0).
 
# Erzeuge anschließend zwei Objekte aus dieser Klasse und gib ihren Attributen konkrete Werte.

class banknote:
    def __init__(self):
        self.inhaber = str("")
        self.kontostand = int(0)
        
konto1 = banknote()
konto2 = banknote()

konto1.inhaber = "Joshua Kadison"
konto2.inhaber = "Robert Redford"
konto1.kontostand = 254,54
konto2.kontostand = 34985123,12

print(konto1.inhaber, konto1.kontostand)
print("")
print(konto2.inhaber, konto2.kontostand)