# # Aufgabe 1
# rechnen = int(input("Gebe eine Zahl ein: "))

# for i in range(1, 11):
#     print(rechnen, "*", i, "=", rechnen * i)

# # Aufgabe 2
# import random
# suchende_zahl = random.randint(1, 10)
# gefunden = False

# while gefunden == False:
#     eingabe = int(input("Gebe eine Zahl zwischen 1 und 10 ein: "))
#     if eingabe == suchende_zahl:
#         print("Du hast die Zahl gefunden!")
#         gefunden = True
#     else:
#         print("Leider falsch, versuche es nochmal!")

# # Aufgabe 3
# import random
# suchende_zahl = random.randint(1, 10)
# gefunden = False

# while gefunden == False:
#     eingabe = int(input("Gebe eine Zahl zwischen 1 und 10 ein: "))
#     if eingabe == suchende_zahl:
#         print("Du hast die Zahl gefunden!")
#         gefunden = True
#     elif eingabe < suchende_zahl:
#         print("Die gesuchte Zahl ist größer als deine Eingabe. Versuche es nochmal!")
#     else:
#         print("Die gesuchte Zahl ist kleiner als deine Eingabe. Versuche es nochmal!")

# Aufgabe 4
import random
suchende_zahl = random.randint(1, 10)
gefunden = False

while gefunden == False:
    eingabe = int(input("Gebe eine Zahl zwischen 1 und 10 ein: "))
    if eingabe == suchende_zahl:
        print("Du hast die Zahl gefunden!")
        nochmal = input("Möchtest du nochmal spielen? (ja/nein): ")
        if nochmal == "ja":
            print("Super, lass es uns nochmal versuchen!")
            suchende_zahl = random.randint(1, 10)
        else:
            gefunden = True
    elif eingabe < suchende_zahl:
        print("Die gesuchte Zahl ist größer als deine Eingabe. Versuche es nochmal!")
    else:
        print("Die gesuchte Zahl ist kleiner als deine Eingabe. Versuche es nochmal!")