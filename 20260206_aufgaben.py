#Aufgabe 1: Schreibe ein Python Skript,
# welches den Rechnungsbetrag in einem Restaurant einliest,
# und daraus das Trinkgeld (10 Prozent) berechnet.
betrag = float(input("Betrag eingeben: "))
trinkgeld = betrag * 0.1
print("Trinkgeld beträgt: ", trinkgeld, "Euro")

#Aufgabe 2: Schreibe eine Funktion, die das Trinkgeld berechnet.
def berechne_trinkgeld(betrag):
    return betrag * 0.1

betrag = float(input("Betrag eingeben: "))
trinkgeld = berechne_trinkgeld(betrag)
print("Trinkgeld beträgt: ", trinkgeld, "Euro")

#Aufgabe 3: Erweitere die Funktion um den Oarameter prozent.
def berechne_trinkgeld(betrag, prozent):
    return betrag * (prozent / 100)

betrag = float(input("Betrag eingeben: "))
prozent = float(input("Prozent eingeben: "))
trinkgeld = berechne_trinkgeld(betrag, prozent)
print("Trinkgeld beträgt: ", trinkgeld, "Euro")