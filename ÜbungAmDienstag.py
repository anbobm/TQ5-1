print("Das ist ein Programm, das Fahrenheit in Celsius umrechnet und andersrum.")

def fahrenheit_in_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_in_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

Auswahl = input("Möchtest du Fahrenheit in Celsius haben (1) oder Celsius in Fahrenheit (2)? ")
Wahrhaftig = False

while Wahrhaftig == False:
    if Auswahl == "1":
        try:
            fahrenheit = float(input("Gib die Temperatur in Fahrenheit ein(ohne Zeichen): "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
            continue
        else:
            celsius = fahrenheit_in_celsius(fahrenheit)
            print(f"{fahrenheit} Grad Fahrenheit entsprechen {celsius} Grad Celsius.")
            Wahrhaftig = True
    elif Auswahl == "2":
        try:
            celsius = float(input("Gib die Temperatur in Celsius ein(ohne Zeichen): "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
            continue
        else:
            fahrenheit = celsius_in_fahrenheit(celsius)
            print(f"{celsius} Grad Celsius entsprechen {fahrenheit} Grad Fahrenheit.")
            Wahrhaftig = True
    else:
        Auswahl = input("Gib eine Auswahl zwischen 1 und 2 ein: ")
