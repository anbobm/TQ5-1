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
        neue_temp = self.__celsius + wert
        if neue_temp < -273.15:
            self.__celsius = -273.15
        
        else:
            self.__celsius = neue_temp

    def senken(self,wert):
        neue_temp = self.__celsius - wert
        if neue_temp < -273.15:
            self.__celsius = -273.15
        else:
            self.__celsius = neue_temp


if __name__ == "__main__":
    sensor = Temperatursensor()

    print("Start:", sensor.get_celsius())

    sensor.set_celsius(20)
    print("Nach set_celsius(20):", sensor.get_celsius())

    print("In Fahrenheit:", sensor.get_fahrenheit())

    sensor.erhoehen(10)
    print("Nach erhoehen(10):", sensor.get_celsius())

    sensor.senken(50)
    print("Nach senken(50):", sensor.get_celsius())

    sensor.senken(500)
    print("Nach senken(500) (Grenze prüfen):", sensor.get_celsius())            


    


