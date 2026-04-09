rechnung = float(input("Betrag: "))
trinkgeld = rechnung * 0.10
print(trinkgeld)


def berechne_trinkgeld(rechnung):
    return rechnung * 0.10

betrag = float(input("Betrag: "))
trinkgeld = berechne_trinkgeld(betrag)
print(trinkgeld)

print("### NEUE VERSION ###")
def berechne_trinkgeld(rechnung, prozent):
    return rechnung * prozent / 100

betrag = float(input("Betrag: "))
prozent = float(input("Trinkgeld in Prozent: "))

trinkgeld = berechne_trinkgeld(betrag, prozent)
print(trinkgeld)