zahl = int(input("Gib eine Zahl ein: "))
# if zahl % 2 == 0:
#     print("Die Zahl ist gerade.")
# else:    
#     print("Die Zahl ist ungerade.")

def isEven(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

Ausgabe = isEven(zahl)
if Ausgabe == True:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")