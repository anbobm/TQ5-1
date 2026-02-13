import random

sum = 0
bonus_punkte = 0

wurf_1 = wurf_2 = wurf_3 = 0

for i in range(3):
    würfel = random.randint(1, 6)

    if i == 0:
        wurf_1 = würfel
    elif i == 1:
        wurf_2 = würfel
    else:
        wurf_3 = würfel

    print(f"Wurf {i + 1}: {würfel}")
    sum += würfel

if wurf_1 == wurf_2 == wurf_3:
    bonus_punkte += 6
if wurf_1 == wurf_2 or wurf_1 == wurf_3 or wurf_2 == wurf_3:
    bonus_punkte += 2

print(f"Summe der Würfe: {sum} und bonus Punkte: {bonus_punkte}")
print(f"Endergebnis: {sum + bonus_punkte}")

if(sum + bonus_punkte >= 15):
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")