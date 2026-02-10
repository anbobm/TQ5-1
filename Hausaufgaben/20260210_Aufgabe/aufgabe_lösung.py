import random

sum = 0
bonus_punkte = 0

wurf1 = wurf2 = wurf3 = 0

for i in range(3):
    würfel = random.randint(1, 6)

    if i == 0:
        wurf1 = würfel
    elif i == 1:
        wurf2 = würfel
    else:
        wurf3 = würfel

    print(f"Wurf {i + 1}: {würfel}")
    sum += würfel

if wurf1 == wurf2 == wurf3:
    bonus_punkte += 6
if wurf1 == wurf2 or wurf1 == wurf3 or wurf2 == wurf3:
    bonus_punkte += 2

print(f"Summe der Würfe: {sum} und bonus Punkte: {bonus_punkte}")
print(f"Endergebnis: {sum + bonus_punkte}")

if(sum + bonus_punkte >= 15):
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")