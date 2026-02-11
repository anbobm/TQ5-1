# Aufgabe 1

rechnung = float(input("Betrag: "))

# Trinkgeld berechnen und ausgeben:
trinkgeld = rechnung * 0.1

print("Trinkgeld:", trinkgeld)

# Alternative mit String-Konkatenation
print("Trinkgeld: " + str(trinkgeld))

# Alternative mit f-Strings
print(f"Trinkgeld: {trinkgeld}")

# Aufgabe 2

def berechne_trinkgeld(betrag):
    trinkgeld = betrag * 0.1
    return betrag * 0.1

rechnung = float(input("Betrag: "))

trinkgeld = berechne_trinkgeld(rechnung)

print("Trinkgeld:", trinkgeld)

# Aufgabe 3

def berechne_trinkgeld(betrag, prozent):
    return betrag * prozent

rechnung = float(input("Betrag: "))

trinkgeld = berechne_trinkgeld(rechnung, 0.2)

print("Trinkgeld:", trinkgeld)

# Benutzer gibt Prozentsatz vor:

def berechne_trinkgeld(betrag, prozent):
    return betrag * prozent

rechnung = float(input("Betrag: "))
prozent = float(input("Trinkgeld (Prozent): "))
prozent = prozent / 100

trinkgeld = berechne_trinkgeld(rechnung, 0.2)

print("Trinkgeld:", trinkgeld)

# Extra extra: Default-Parameter
def berechne_trinkgeld(betrag, prozent=0.1):
    return betrag * prozent

berechne_trinkgeld(100)
berechne_trinkgeld(100, 0.2)