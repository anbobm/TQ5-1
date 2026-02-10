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