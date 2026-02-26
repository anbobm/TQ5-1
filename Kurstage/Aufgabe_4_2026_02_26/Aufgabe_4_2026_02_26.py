# Aufgabe_4 Klasse für Temperatursensor
class Temperatursensor:
    def __init__(self):
        self.__celsius = 0

    def set_celsius(self, wert):
        if wert < -273.15:
            self.__celsius = -273.15
        else:
            self.__celsius = wert 

    def get_celsius(self):
        return self.__celsius

    def get_fahrenheit(self):
        return self.__celsius * 9 / 5 + 32
    
    def erhoehen(self, wert):
        neue_temperatur = self.__celsius + wert
        if neue_temperatur < -273.15:
            self.__celsius = -273.15
        
        else:
            self.__celsius = neue_temp

    def senken(self,wert):
        neue_temp = self.__celsius - wert
        if neue_temp < -273.15:
            self.__celsius = -273.15
        else:
            self.__celsius = neue_temp


    


