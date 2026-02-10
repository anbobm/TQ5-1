zahl = int(input("Geben Sie eine gerade Zahl ein: "))
if zahl % 2 == 0:
    print("Glückwunsch, die Zahl ist gerade.")
else:    print("Du solltest noch mal zur Schule gehen.")

#Funktion isEven(zahl) schreiben, die true zurückgibt, 
#wenn die übergebene Zahl gerade ist, ansonsten false

def isEven(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False
    
inputZahl = int(input("Geben Sie eine Zahl ein: "))
if isEven(inputZahl):
    print("gerade.")
else:    print("ungerade.")

#Temperatureingabe mit Vergleich
temp = int(input("Geben Sie die aktuelle Temperatur ein: "))
if temp < 0:
    print("Es ist sehr eiskalt.")
elif temp < 20:
    print("Es ist frisch.")
elif temp < 30:
    print("Es ist warm.")  
else:    print("Es ist zu heiß.")

# Notenausgabe nach Punktzahleingabe
punkte = int(input("Geben Sie die erreichten Punkte ein: "))
if punkte >= 92:
    print("Note: Sehr gut")
elif punkte >= 81:
    print("Note: Gut")
elif punkte >= 67:
    print("Note: Befriedigend")
elif punkte >= 50:
    print("Note: Ausreichend") 

elif punkte >= 30:
    print("Note: Mangelhaft")
else:
    print("Note: Ungenügend")