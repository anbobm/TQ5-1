#Aufgabe 1 

# wort = input("Geben Sie ein Wort ein: ")
# print(wort)

# dict = {}

# for buchstaben in wort:
#     if buchstaben in dict:
#         dict[buchstaben] = dict[buchstaben] + 1        
#     else:
#         dict[buchstaben] = 1

# for item in dict:
#     print(f"{item} kommt {dict[item]} mal vor")

#Aufgabe 2 

def main():

    lager = {
    "Apfel": {"preis": 2, "menge": 10},
    "Banane": {"preis": 1, "menge": 8},
    "Orange": {"preis": 3, "menge": 5}
    }

    while True:
        show_menue()
        launch_app(lager)

def show_menue():
    print("1. Kompletten Lagerbestand anzeigen")
    print("2. Lagerbestand von einem Artikel anzeigen")
    print("3. Menge von Artikeln entfernen (Verkauf)")
    print("4. Menge von Artikeln zufuegen (Einkauf)")
    print("5. Artikel loeschen")
    print("6. Exit")

def launch_app(lager): 
    menue_auswahl = int(input("Waehlen Sie Menuepunkt aus: "))

    match menue_auswahl:
        case 1:
            komplett_lagerbestand_anzeigen(lager)               
        case 2: 
            artikel_lagerbestand_anzeigen(lager) 
        case 3:
            menge_artikel_entfernen(lager)          
        case 4:
            menge_artikel_zufuegen(lager)         
        case 5:
            artikel_loeschen(lager)            
        case 6:
            exit()

#####
def komplett_lagerbestand_anzeigen(lager):
    for key, value in lager.items():
        print(f"Artikel {key}: Preis: {value["preis"]}, Menge: {value["menge"]}")

#####
def artikel_lagerbestand_anzeigen(lager):
    artikel = input("Welche Artikel? ")   

    if artikel in lager:
        __artikel = lager[artikel]
        print(f"Preis: {__artikel["preis"]} \nMenge: {__artikel["menge"]}")
    else:
        print("Artikel ist nicht gefunden")

#####
def menge_artikel_entfernen(lager):
    artikel = input("Welche Artikel? ")

    count_entnehmen = int(input("Wie viele entnehmen? "))
    if artikel in lager:
        __artikel = lager[artikel]
        print(f"{count_entnehmen} Stueck entnommen.")
        rest = __artikel["menge"] - count_entnehmen
        __artikel["menge"] = rest
        print(f"Es sind noch {rest} uebrig.")
    else:
        print("Artikel ist nicht gefunden")

#####
def menge_artikel_zufuegen(lager):
    artikel = input("Welche Artikel? ")

    count_hinzufügen = int(input("Wie viele hinzufügen? "))
    if artikel in lager:
        __artikel = lager[artikel]     
        __count = __artikel["menge"] + count_hinzufügen
        __artikel["menge"] = __count
        print(f"Es sind jetzt {__count} vorrätig.")
    else:
        preis = int(input("Preis des Artikels? "))
        lager[artikel] = {
            "preis": preis,
            "menge": count_hinzufügen
        }
        print(f"Es sind jetzt {count_hinzufügen} vorrätig.")

#####
def artikel_loeschen(lager):
    artikel = input("Welche Artikel? ")

    if artikel in lager:    
        __artikel = lager[artikel]     
        __artikel["menge"] = 0
        lager[artikel] = __artikel
        print(f" Lagerbestand auf 0 gesetzt.")
    else:
        print("Artikel ist nicht gefunden")


main()

