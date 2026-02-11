import random

# Drei Würfel werfen
zahlen = []
summe = 0

for i in range(3):
    zahl = random.randint(1, 6)
    zahlen.append(zahl)
    summe += zahl
    print(f"Wurf {i+1}: {zahl}")

print(f"Summe: {summe}")

# Bonus berechnen
max_count = max(zahlen.count(n) for n in zahlen)
bonus = 0

if max_count == 2:
    bonus = 2
    print("Bonus: 2 (Zweierpasch)")
elif max_count == 3:
    bonus = 6
    print("Bonus: 6 (Dreierpasch)")

gesamt = summe + bonus
print(f"Gesamtpunktzahl: {gesamt}")

# Gewinnbedingung
if gesamt >= 15:
    print("Gewonnen!")
else:
    print("Verloren!")