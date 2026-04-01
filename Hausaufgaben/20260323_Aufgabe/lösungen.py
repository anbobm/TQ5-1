import os

#Aufgabe 1

def parse_filename(filename):
    teile = filename.split("-")

    datum_zeit = teile[-1].removesuffix(".jpg")

    tag, monat, rest = datum_zeit.split(".")
    jahr, uhrzeit = rest.split("_")

    uhrzeit = uhrzeit.replace("h", "")

    beschreibung = " ".join(teile[2:-1])

    return jahr, monat, tag, uhrzeit, beschreibung


def build_new_name(jahr, monat, tag, uhrzeit, beschreibung):
    return f"{jahr}-{monat}-{tag}-{uhrzeit} {beschreibung}.jpg"


def rename_photos(ordner):
    for dateiname in os.listdir(ordner):

        jahr, monat, tag, uhrzeit, beschreibung = parse_filename(dateiname)

        neuer_name = build_new_name(jahr, monat, tag, uhrzeit, beschreibung)

        alt_pfad = os.path.join(ordner, dateiname)
        neu_pfad = os.path.join(ordner, neuer_name)

        os.rename(alt_pfad, neu_pfad)


# rename_photos("Kurstage/2026-03-23/photos")

#Aufgabe 2

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result: {result}")

def result_output():       
    while True:
        try:
            user_input = input("Input a string: ")   
            operation, a, b = user_input.split()

            a = int(a)
            b = int(b)

            match operation:

                case 'durch':
                    do_operation(a, b, lambda a, b: a / b)
                case 'plus':
                    do_operation(a, b, lambda a, b: a + b)
                case 'minus':
                    do_operation(a, b, lambda a, b: a - b)
                case 'mal':
                    do_operation(a, b, lambda a, b: a * b)
                case _:
                    print("Unknown operation. Try Again (minus, plus, durch or mal)")
    
        except ValueError as exception:
            print(exception)

result_output()