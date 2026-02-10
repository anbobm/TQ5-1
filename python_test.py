# Aufgabe

#Der Benutzer gibt eine Temperatur ein.
#Wenn die Temperatur kleiner als 0 ist, dann gib "Es ist eiskalt" aus.
#Wenn die Temperatur kleiner als 20 ist, dann gib "Es ist frisch" aus.
#Wenn die Temperatur kleiner als 30 ist, dann gib "Es ist warm" aus.
#Ansonsten gib "Es ist zu heiß" aus.

temperatur = input("Geben Sie die Temperatur ein: ")

if temperatur < 0:
    print("Es ist eiskalt")
elif temperatur < 20:
    print("Es ist frisch")
elif temperatur < 30:
    print("Es ist warm")
else:
    print("Es ist zu heiß")

