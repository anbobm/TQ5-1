
import random

zufallszahl = random.randint(1, 6)
zufallszahl2 = random.randint(1, 6)
zufallszahl3 = random.randint(1, 6)
PashBonus = 2
dreiherpashBonus = 6
Summe = zufallszahl + zufallszahl2 + zufallszahl3
Punkte = Summe
if zufallszahl == zufallszahl2:
    print("Du hast ein Pash geworfen!")
    print(zufallszahl,"+",zufallszahl2,"+",zufallszahl3,"+",PashBonus,"=",Summe + PashBonus)
    print("Deine Punkte:",Punkte + PashBonus)
    Summe = Summe + PashBonus
elif zufallszahl == zufallszahl3:
    print("Du hast ein Pash geworfen!")
    print(zufallszahl,"+",zufallszahl2,"+",zufallszahl3,"+",PashBonus,"=",Summe + PashBonus)
    print("Deine Punkte:",Punkte + PashBonus)
    Summe = Summe + PashBonus
elif zufallszahl2 == zufallszahl3 and zufallszahl2 == zufallszahl:
    print("Du hast ein dreiherpash geworfen!")
    print(zufallszahl,"+",zufallszahl2,"+",zufallszahl3,"+",dreiherpashBonus,"=",Summe + dreiherpashBonus)
    print("Deine Punkte:",Punkte + dreiherpashBonus)
    Summe = Summe + dreiherpashBonus
else:
    print(zufallszahl,"+",zufallszahl2,"+",zufallszahl3,"=",Summe)
    print("Deine Punkte:",Punkte)

if Summe >= 15:
    print("Glückwunsch, du hast gewonnen!")
else:
    print("Leider verloren, versuch es nochmal!")

