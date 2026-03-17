from datetime import datetime

#Aufgabe 1

def count_words():
    _words = []
    length = 5
    with open("input.txt", "r") as file:
        text = file.read()
        words = text.split()
        for word in words:
            if len(word) > length:
                _words.append(word)
    return _words
                    
def write_to_file():
    with open("lange_worter.txt", "w") as file:
        for word in count_words():
            file.writelines(word + '\n')

#Aufgabe 2

def aufgabe_zwei():
    text = input("Bitte einen String eingeben: ")
    suffix = "bar"
    if text.endswith(suffix):
        result_text = text[:-len(suffix)]
    else:
        result_text = text
    print(result_text)


#aufgabe 3

def aufgabe_drei_read_from_file(): 
    dates_list = []
    with open("dates.txt", "r") as file:
        dates_rows = file.readlines()     
        for date in dates_rows:
            date = date.split()
            dates = {}
            dates['date'] = date[0]
            dates['uhrzeit'] = date[1].rstrip("Uhr")
            dates_list.append(dates)
        file.close()
    return dates_list

def aufgabe_drei_write_to_file():
    with open("formatted_dates.txt", "w+") as file:
        for dates in aufgabe_drei_read_from_file():
            file.writelines(f"Datum: {dates['date']}\nUhrzeit: {dates['uhrzeit']}\n\n")
        file.close()

#aufgabe 4
def aufgabe_vier_write_to_file():
    with open("formatted_dates.txt", "w+") as file:
        for dates in aufgabe_drei_read_from_file():
            date_obj = datetime.strptime(dates['date'], "%Y-%m-%d") 
            formatted_date = f"{date_obj.day}.{date_obj.month}.{date_obj.year}"
            file.writelines(f"Datum: {formatted_date}\nUhrzeit: {dates['uhrzeit']}\n\n")
        file.close()


def hauptmenu():
    print("\n1. Aufgabe 1. \n2. Aufgabe 2. \n3. Aufgabe 3. \n4. Aufgabe 4. \n5. Exit\n")
    while True:      
        punkt_menu = int(input("Wahlen Sie ein Punktmenu aus: "))
        match punkt_menu:
            case 1:
                write_to_file()
                print("Success")
            case 2:
                aufgabe_zwei()
            case 3:
                aufgabe_drei_write_to_file()
                print("Success")
            case 4:
                aufgabe_vier_write_to_file()             
            case 5:
                break
            case _:
                print("Ungultige Wert")
def main():
    hauptmenu()

main()