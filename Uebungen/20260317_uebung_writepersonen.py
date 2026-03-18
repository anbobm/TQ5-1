

## vorige Aufgabe
# with open("20260316_person.txt", "w") as datei:
#     while True:
#         vorname = input("Vorname?")
#         nachname = input("Nachname?")
#         alter = input("Alter?")
    
#         datei.write(f"{vorname}, {nachname}, {alter}\n")

#         weiter = input("Weitere Daten eingeben? (j/n)")
#         if weiter != "j":
#             print("Eingabe beendet.")
#             break
            
# datei.close()
 

# # Aufgabe 5
# Die Datensätze aus person.txt sollen eingelesen und in einer Liste aus Dictionaries gespeichert werden:

# personen = [
#     {"vorname": "Max", "nachname": "Mustermann", "alter": "30"},
#     {"vorname": "Maxine", "nachname": "Musterfrau", "alter": "25"},
#     ...
# ]
# Überprüfe mit print(personen) ob du erfolgreich warst.
personen = []
datei = open("20260316_person.txt")
for zeile in datei:
    vorname, nachname, alter = zeile.rstrip("\n").split(",")
    
    person = {
        "vorname": vorname,
        "nachname": nachname,
        "alter": alter
    }
    personen.append(person)
# personen = [datei.read().splitlines()]

print(personen)

datei.close()

