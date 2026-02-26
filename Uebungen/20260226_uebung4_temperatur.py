# Aufgabe 4
# Erstelle eine Klasse Temperatursensor.

# Sie hat ein privates Attribut für die aktuelle Temperatur (in Celsius), die zu Anfang auf 0 gesetzt wird.

# Methoden:
# set_celsius(wert): Setzt die Temperatur auf den übergebenen Wert.
# get_celsius(): Gibt die Temperatur in Celsius zurück
# get_fahrenheit(): Gibt die Temperatur in Fahrenheit zurück
# erhoehen(wert): Erhöht die Temperatur um den übergebenen Wert
# senken(wert): Senkt die Temperatur um den übergebenen Wert.
# Hinweis: Die Temperatur darf nie kleiner als -273.15 sein.

class Temperatur:
    def __init__(self):
        self.__temp_celsius = 0.0
        
    def set_celsius(self, wert):
        self.__temp_celsius = wert
        if wert >= -273.15
            print(f"Temperatur auf {wert}°C gesetzt.")
        else:
            print("Die Temperatur kann nicht unter -273.15 °C liegen.")
        
    
    def get_celsius(self): 
        return self.__temp_celsius
        
    def get_fahrenheit(self):
        return self.__temp_celsius * 9/5 + 32
    
    def erhoehen(self, wert):
        neue_temp = self.__temp_celsius + wert 
        return f"Temperatur um {wert} °C erhöht."
    
    def senken(self, wert):
        neue_temp = self.__temp_celsius - wert
        if wert <= -273.15:
            print("Die Temperatur kann nicht unter -273.15°C liegen.")
        else:
            return f"Temperatur um {wert} °C gesenkt."