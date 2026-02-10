#Würfelspiel
# Mit der random.randint() Methode simulieren wir den Wurf von drei sechsseitigen Würfeln. 
# Wir werten die gewürfelten Werte aus, um die Punktzahl zu berechnen. 
# Die Ausgabe der Summe soll so aussehen: Wurf: 4 + 5 + 2 = 11 
# Wenn die Augenzahl auf zwei Würfeln identisch ist, erhalten wir zwei Bonuspunkte für einen Zweierpasch. 
# Wenn die Augenzahl auf allen drei Würfeln identisch ist, erhalten wir sechs Bonuspunkte für einen Dreierpasch. 
# Wenn wir Bonuspunkte bekommen, dann sollen wir nicht nur unsere Summe um den Wert erhöht, 
# sondern wir sollen auch ausgeben, dass wir den Bonus bekommen. 
# Wenn die Summe der Augenzahlen der drei Würfel und aller Bonuspunkte mindestens 15 ist, 
# gewinnen wir das Spiel. Andernfalls verlieren wir.

from random import randint

import random

w1 = random.randint(1, 6)
w2 = random.randint(1, 6)
w3 = random.randint(1, 6)

summe = w1 + w2 + w3


print(f"Wurf: {w1} + {w2} + {w3} = {summe}")

bonus = 0

if w1 == w2 == w3:
    bonus = 6
    print("Bonus: Dreierpasch! +6 Punkte")
elif w1 == w2 or w1 == w3 or w2 == w3:
    bonus = 2
    print("Bonus: Zweierpasch! +2 Punkte")

gesamt = summe + bonus
print(f"Gesamtpunktzahl: {gesamt}")


if gesamt >= 15:
    print("Du hast gewonnen!")
else:
    print("Du hast leider verloren.")
