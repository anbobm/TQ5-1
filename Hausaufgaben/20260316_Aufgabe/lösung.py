path = "person.txt"

def write_to_file():
    while True:
        vorname = input("Vorname? ")
        nachname = input("Nachname? ")
        alter = input("Alter? ")
        print(f"{vorname}, {nachname}, {alter}")
    
        with open(path, "a") as person_file:
            person_file.write(vorname + "," + nachname + "," + alter + "\n")           
        
        eingabe = input("Weiter? (j/n) ")
        if eingabe == 'n':
            break

def read_from_file():
    with open(path, "r") as person_file:
        for lines in person_file:
            print(lines, end="")
    print()

def get_person_info():
    person_list = []
    with open(path, 'r') as file_with_person:
        person_rows = file_with_person.readlines()
        for person in person_rows:
            person = person.split(',')
            persons = {}
            persons['vorname'] = person[0]
            persons['nachname'] = person[1]
            persons['alter'] = person[2].strip()
            person_list.append(persons)
        file_with_person.close()
    return person_list

def hauptmenu():
    while(True):
        selection = int(input("1.Eingabe\t\t2.Ausgabe\t\t3.Get Info\t\t4.Exit\nWählen Sie ein Punkt aus: "))
        match selection:
            case 1: write_to_file()
            case 2: read_from_file()
            case 3: 
                for person in get_person_info():
                    print(person)
            case 4: break
            case _: print("Ungültige Eingabe")

def main():
    hauptmenu()

main()