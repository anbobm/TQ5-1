# Exercise 1
rechnung = float(input("Betrag: "))
trinkgeld = rechnung * 0.10
print("Trinkgeld: ", round(trinkgeld, 2))

# Exercise 2
def trinkgeld_berechnen(rechnung):
    return rechnung * 0.10

betrag = float(input("Betrag: "))
trinkgeld = trinkgeld_berechnen(betrag)
print("Trinkgeld: ", round(trinkgeld, 2))

# Exercise 3
def trinkgeld_berechnen(rechnung, prozent):
    return rechnung * prozent / 100

betrag = float(input("Betrag: "))
prozent = float(input("Prozent: "))
trinkgeld = trinkgeld_berechnen(betrag, prozent)
print("Trinkgeld: ", round(trinkgeld, 2))