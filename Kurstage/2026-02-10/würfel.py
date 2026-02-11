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

def wuerfeln():
    return randint(1, 6) 

versuch1 = wuerfeln()
print(f"Wurf: {versuch1}")
versuch2 = wuerfeln() 
print(f"Wurf: {versuch2}")
versuch3 = wuerfeln()
print(f"Wurf: {versuch3}")
summe = versuch1 + versuch2 + versuch3
if versuch1 == versuch2 == versuch3:
    summe += 6
    print(f"Wurf: {versuch1} + {versuch2} + {versuch3} = {summe} (Dreierpasch Bonus: 6 Punkte)")
elif versuch1 == versuch2 or versuch2 == versuch3 or versuch1 == versuch3:
    summe += 2
    print(f"Wurf: {versuch1} + {versuch2} + {versuch3} = {summe} (Zweierpasch Bonus: 2 Punkte)")
if summe >= 15:
    print(f"{summe} Glückwunsch, du hast gewonnen!")
else:
    print(f"{summe} Leider hast du verloren.")