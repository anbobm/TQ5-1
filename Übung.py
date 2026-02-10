# zahl = int(input("Gib eine Zahl ein: "))
# if zahl % 2 == 0:
#     print("Die Zahl ist gerade.")
# else:    
#     print("Die Zahl ist ungerade.")

# def isEven(zahl):
#     if zahl % 2 == 0:
#         return True
#     else:
#         return False

# Ausgabe = isEven(zahl)
# if Ausgabe == True:
#     print("Die Zahl ist gerade.")
# else:
#     print("Die Zahl ist ungerade.")

# temperatur = int(input("Gib die Temperatur ein: "))
# if temperatur < 0:
#     print("Es ist eiskalt.")
# elif temperatur < 20:
#     print("Es ist frisch.")
# elif temperatur < 30:
#     print("Es ist warm.")
# else:
#     print("Es ist heiß.")


benutzer_note= int(input("Gib deine Note ein: "))
if benutzer_note >= 92:
    print("Sehr gut")
elif benutzer_note >= 81:
    print("Gut")
elif benutzer_note >= 67:
    print("Befriedigend")
elif benutzer_note >= 50:
    print("Ausreichend")
elif benutzer_note >= 30:
    print("Mangelhaft")
else:
    print("Ungenügend")
