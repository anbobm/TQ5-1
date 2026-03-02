# age = int(input("Gib dein Alter ein: "))
# if age <= 18:
#     print("Du bist zu jung")
# else:
#     print("Du kannst loslegen")


# print("")
# print("Aufgabe Ticket Video")
# print("")

# ticket_kinder = 5
# ticket_erwachsene = 10
# ticket_senioren = 7

# alter = int(input("Gib dein Alter ein: "))
# if alter < 18:
#     print("Der Ticketpreis beträgt", ticket_kinder, "Euro.")
# elif alter >= 18 and alter < 65:
#     print("Der Ticketpreis beträgt", ticket_erwachsene, "Euro.")
# else:
#     print("Der Ticketpreis beträgt", ticket_senioren, "Euro.")
    
# ticket_kauf = int(input("Wie viele Tickets möchtest du kaufen? "))
# if alter < 18:
#     print("Der Gesamtpreis beträgt", ticket_kinder * ticket_kauf, "Euro.")
# elif alter >= 18 and alter < 65:
#     print("Der Gesamtpreis beträgt", ticket_erwachsene * ticket_kauf, "Euro.")
# else:    print("Der Gesamtpreis beträgt", ticket_senioren * ticket_kauf, "Euro.")

# print("")
# print("Aufgabe Einkaufsliste")
# print("")

# einkaufsliste =[]
# fortfahren = "J"

# while fortfahren == "J":
#    einkaufsliste.append(input("Was möchtest du kaufen? "))
#    fortfahren = input("Möchtest du noch etwas hinzufügen? (J/N) ")

# print("Deine Einkaufsliste:", einkaufsliste)

# print("")
# print("Aufgabe erweiterte Einkaufsliste mit while-Schleife")
# print("")

# shoppinglist = []


# entfernen = 2
# anzeigen = 3
# beenden = 4

# while True:
#     print("Was möchtest du tun?")
#     print("")
#     print("1: Artikel hinzufügen")
#     print("")
#     print("2: Artikel entfernen")
#     print("")
#     print("3: Einkaufsliste anzeigen")
#     print("")
#     print("4: Beenden")
#     print("")
#     aktion = int(input("Gib die Nummer der Aktion ein: "))
    
#     if aktion == 1:
#         artikel = input("Welchen Artikel möchtest du hinzufügen? ")
#         shoppinglist.append(artikel)
#         print(artikel, "wurde hinzugefügt.")
    
#     elif aktion == 2:
#         artikel = input("Welchen Artikel möchtest du entfernen? ")
#         if artikel in shoppinglist:
#             shoppinglist.remove(artikel)
#             print(artikel, "wurde entfernt.")
#         else:
#             print(artikel, "ist nicht in der Einkaufsliste.")
#     elif aktion == 3:
#         print("Deine Einkaufsliste:", shoppinglist)
#     elif aktion == 4:
#         print("Programm wird beendet.")
#         break
#     else:
#         print("Ungültige Eingabe. Bitte versuche es erneut.")


# print("")
# print("Aufgabe Ratespiel")
# print("")

# from random import randint

# zahl = randint(1, 100)

# while True:
#     raten = int(input("Gib deine Zahl ein: "))
#     if raten < zahl:
#         print("Deine Zahl ist zu niedrig")
#     elif raten > zahl:
#         print("Deine Zahl ist zu hoch")
#     elif zahl == raten:
#         print("Glückwunsch!")
#         break
#     else:
#         print("Eingabe nicht gültig. Bitte nur Zahlen zwischen 1 und 100 eingeben.")
        
#       
# print("")
# print("Aufgabe mit for-Schleife")
# print("")


print("")
print("Aufgabe Telefonbuch mit Dictionary")
print("")





print("")
print("Aufgabe TicTacToe")
print("")

# Brett erstellen
def erstelle_brett():
    brett = []
    for i in range(3):
        zeile = [" ", " ", " "]
        brett.append(zeile)
    return brett

# Brett ausgeben
def drucke_brett(brett):
    for zeile in brett:
        print(" |".join(zeile))
        print("--------")
        
#drucke_brett(erstelle_brett())

# Zug ausführen
def zug_machen(brett, spieler, zeile, spalte):
    if brett[zeile][spalte] == " ":
        brett[zeile][spalte] = spieler
        return True
    else:
        return False

# Gewinn überprüfen
def pruefe_gewonnen(brett, spieler):
    for zeile in range(3):
        if brett[0] == brett[1] == [2] == spieler:
            return True
    
    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == [2][spalte] == spieler:
            return True
    
    if brett[0][0] == brett[1][1] == brett[2][2] == spieler or \
       brett[0][2] == brett[1][1] == brett[2][0] == spieler:
        return True
    
# prüfe unentschieden
def pruefe_unentschieden(brett):
    for zeile in brett:
        if " " in zeile:
            return False
    return True

# Hauptkörper
def spiele_tictactoe():
    brett = erstelle_brett()
    aktueller_spieler = "X"

    while True:
        drucke_brett(brett)
        zeile = int(input(f"Spieler {aktueller_spieler}, wähle eine Zeile (0-2)"))
        spalte = int(input(f"Spieler {aktueller_spieler}, wähle eine Spalte (0-2)"))
       
        if not zug_machen(brett, aktueller_spieler, zeile, spalte):
            print("Ungültig. Versuche es erneut.")
            continue
        if pruefe_gewonnen(brett, aktueller_spieler):
            drucke_brett(brett)
            print(f"Wow, Spieler {aktueller_spieler}, du hast gewonnen!")
            break    
        elif pruefe_unentschieden(brett):
            drucke_brett(brett)
            print("Unentschieden!")
            break 
        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"

spiele_tictactoe()