path = "person.txt"

def write_to_file():
    while True:
        vorname = input("Vorname? ")
        nachname = input("Nachname? ")
        alter = input("Alter? ")
        print(f"{vorname}, {nachname}, {alter}")
    
        with open(path, "a") as person_file:
            person_file.write(vorname + ", " + nachname + ", " + alter + "\n")           
        
        eingabe = input("Weiter? (j/n) ")
        if eingabe == 'n':
            break

def read_from_file():
    with open(path, "r") as person_file:
        for lines in person_file:
            print(lines, end="")
    print()

def hauptmenu():
    while(True):
        selection = int(input("1.Eingabe\t\t2.Ausgabe\t\t3.Exit\nWählen Sie ein Punkt aus: "))
        match selection:
            case 1: write_to_file()
            case 2: read_from_file()
            case 3: break
            case _: print("Ungültige Eingabe")


def main():
    hauptmenu()

main()