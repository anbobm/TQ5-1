# Der Benutzer soll Vornamen, Nachnamen und sein Alter eingeben. Z.B.

# Vorname? Max
# Nachname? Mustermann
# Alter? 30
# Anschließend sollen die eingebenen Daten in der Datei person.txt geschrieben werden, in folgender Form: Max,Mustermann,30
with open("20260316_person.txt", "w") as datei:
    while True:
        vorname = input("Vorname?")
        nachname = input("Nachname?")
        alter = input("Alter?")
    
        datei.write(f"{vorname}, {nachname}, {alter}\n")

        weiter = input("Weitere Daten eingeben? (j/n)")
        if weiter != "j":
            print("Eingabe beendet.")
            break
            
datei.close()
# Zusatz:

# Der Nutzer kann so lange Personendaten eingeben, bis er abbrechen möchte:

# Vorname? Max
# Nachname? Mustermann
# Alter? 30
# Weiter? (j/n) j
# Vorname? Maxine
# Nachname? Musterfrau
# Alter? 25
# Weiter? (j/n) n
# Anschließend landen alle Daten in der Datei person.txt, pro Zeile ein Datensatz:

# Max,Mustermann,30
# Maxine,Musterfrau,25
# Paul,Pausenfreu,17
# Ingrid,Individuell,23


# eingabe = input("Gib einen Satz ein: ")
# wortliste = eingabe.split()
# wörter = len(wortliste)

# print(f"Der Satz hat {wörter} Wörter.")