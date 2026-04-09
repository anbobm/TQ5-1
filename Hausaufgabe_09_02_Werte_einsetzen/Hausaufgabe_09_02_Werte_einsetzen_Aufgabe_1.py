# Aufgabe 1
# Aufgabe 1
# Lege eine Variable zahl fest.
# Wenn die Zahl größer oder gleich 10 ist,
# gib „Die Zahl ist …“ aus.
# Ansonsten gib den anderen Text aus.
# Teste die Werte: 9, 10, 11, 1001, -1

def pruefe_zahl(zahl):
    if zahl >= 10:
        print(f"{zahl}: Die Zahl ist größer oder gleich 10")
    else:
        print(f"{zahl}: Die Zahl ist kleiner als 10")

#testwerte = [9, 10, 11, 1001, -1]

#for zahl in testwerte:
    #pruefe_zahl(zahl)


    # Aufgabe 2
# Genau wie Aufgabe 1, aber die Variable „zahl“ soll von der Kommandozeile eingelesen werden.

def pruefe_zahl(zahl):
    if zahl >= 10:
        print(f"{zahl}: Die Zahl ist größer oder gleich 10")
    else:
        print(f"{zahl}: Die Zahl ist kleiner als 10")

# Eingabe von der Kommandozeile
zahl = int(input("Gib eine Zahl ein: "))

# Aufruf der Funktion mit der eingegebenen Zahl
pruefe_zahl(zahl)


