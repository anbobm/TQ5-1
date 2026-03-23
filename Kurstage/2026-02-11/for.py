# einen Block von Anweisungen 5 mal ausführen:

for _ in range(5):
    print("Hallo")


# eine Reihe von Zahlen von 0 bis 7 (8 Stück):

for zahl in range(8):
    print(zahl)


# eine Liste durchlaufen

früchte = ["apfel", "birne", "banane"]

for frucht in früchte:
    if frucht == "birne":
        break
    print(f"Frucht: {frucht}")