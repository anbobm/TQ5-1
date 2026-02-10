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

gesamtpunkte_alle_runden = 0
ziel_punkte = 60  # Du kannst diesen Wert anpassen

for runde in range(1, 6):
    print(f"\n--- RUNDE {runde} ---")
    
    # Würfeln
    w1 = random.randint(1, 6)
    w2 = random.randint(1, 6)
    w3 = random.randint(1, 6)
    
    # Berechnung
    summe = w1 + w2 + w3
    bonus = 0
    
    print(f"Wurf: {w1} + {w2} + {w3} = {summe}")
    
    # Pasch-Prüfung
    if w1 == w2 == w3:
        bonus = 6
        print("Dreierpasch! +6 Bonuspunkte")
    elif w1 == w2 or w1 == w3 or w2 == w3:
        bonus = 2
        print("Zweierpasch! +2 Bonuspunkte")
    
    runde_ergebnis = summe + bonus
    print(f"Punkte in dieser Runde: {runde_ergebnis}")
    
    # Punkte zur Gesamtsumme addieren
    gesamtpunkte_alle_runden += runde_ergebnis

# Endergebnis ausgeben
print("-" * 30)
print(f"GESAMTPUNKTE NACH 5 RUNDEN: {gesamtpunkte_alle_runden}")

# Die Gewinn-Entscheidung
if gesamtpunkte_alle_runden >= ziel_punkte:
    print(f"GEWONNEN! Du hast {ziel_punkte} oder mehr Punkte erreicht.")
else:
    print(f"VERLOREN! Dir fehlen {ziel_punkte - gesamtpunkte_alle_runden} Punkte zum Sieg.")