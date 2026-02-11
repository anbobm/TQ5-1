#Temperatureingabe mit Vergleich

temp = int(input("Geben Sie die aktuelle Temperatur ein: "))

if temp < 0:
    print("Es ist sehr eiskalt.")
elif temp < 20:
    print("Es ist frisch.")
elif temp < 30:
    print("Es ist warm.")  
else:
    print("Es ist zu heiß.")

# Alternative, umständlicher und es ist nicht klar, dass auf jeden Fall
# einer der Blöcke ausgeführt wird
if temp < 0:
    print("Es ist sehr eiskalt.")
if temp >= 0 and temp < 20:
    print("Es ist frisch.")
if temp >= 20 and temp < 30:
    print("Es ist warm.")
if temp >= 30:
    print("Es ist zu heiß.")