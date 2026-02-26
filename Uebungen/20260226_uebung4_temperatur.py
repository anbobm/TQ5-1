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
import math
class Temperatur:
    def __init__(self):
        self._temp_celsius = 0
        
    def set_celsius(self, wert):
        self._temp_celsius = wert
        if wert >= -273.15:
            print(f"Temperatur auf {wert}°C gesetzt.")
        else:
            print("Die Temperatur kann nicht unter -273.15 °C liegen.")
        
    
    def get_celsius(self): 
        print(self._temp_celsius)
        
    def get_fahrenheit(self):
        print(f"Temperatur von {self._temp_celsius}°C sind {self._temp_celsius * 9/5 + 32}° Fahrenheit")
    
    def erhoehen(self, wert):
        self.temp_celsius = self._temp_celsius + wert 
        print(f"Temperatur um {wert}°C erhöht.Es sind jetzt {self._temp_celsius + wert}°C.")
    
    def senken(self, wert):
        self.temp_celsius = self._temp_celsius - wert
        if wert <= -273.15:
            print("Die Temperatur kann nicht unter -273.15°C liegen.")
        else:
            print(f"Temperatur um {wert}°C gesenkt. Es sind jetzt {self._temp_celsius - wert}°C.")
        
temp1 = Temperatur()
temp2 = Temperatur()

temp1.set_celsius(20)
temp2.set_celsius(33)



temp1.erhoehen(7)
print(temp1.get_celsius())
print(temp1.get_fahrenheit())

temp2.senken(17)
print(temp2.get_fahrenheit())

