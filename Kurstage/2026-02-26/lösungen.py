# Aufgabe 1

# class Produkt:
#     def __init__(self, name, preis):
#         self._name = name
#         self._preis = preis
#         self._lagerbestand = 0

#     def verkaufen(self, menge):
#         if not menge > 0:
#             print("Negative Anzahl kann man nicht verkaufen")
#             return
        
#         if self._lagerbestand >= menge:
#             self._lagerbestand = self._lagerbestand - menge
#         else:
#             print("Nicht genug vorrätig")

#     def nachbestellen(self, menge):
#         if not menge > 0:
#             print("Negative Anzahl kann man nicht nachbestellen")
#             return

#         self._lagerbestand = self._lagerbestand + menge

#     def set_preis(self, neuer_preis):
#         if neuer_preis < 0:
#             print("Negative Preise sind nicht erlaubt")
#             return
        
#         self._preis = neuer_preis

#     def get_info(self):
#         print(f"Das Produkt heißt {self._name} und es kostet {self._preis}.")
#         print(f"Zur Zeit sind im Lager {self._lagerbestand} vorrätig.")

# produkt = Produkt("Apfel", 1)

# produkt.get_info()
# produkt.verkaufen(1)
# produkt.get_info()
# produkt.nachbestellen(10)
# produkt.get_info()
# produkt.verkaufen(7)
# produkt.get_info()
# produkt.verkaufen(3)
# produkt.get_info()
# produkt.set_preis(2)
# produkt.get_info()

# produkt.verkaufen(-3)
# produkt.nachbestellen(-10)
# produkt.set_preis(-1)

# Aufgabe 2

# class Rechteck:
#     def __init__(self, hoehe, breite):
#         self._hoehe = hoehe
#         self._breite = breite

#     def set_breite(self, wert):
#         if wert <= 0:
#             print("Nur positive Werte als Breite erlaubt")
#             return
        
#         self._breite = wert

#     def set_hoehe(self, wert):
#         if wert <= 0:
#             print("Nur positive Werte als Höhe erlaubt")
#             return
        
#         self._hoehe = wert

#     def flaeche(self):
#         return self._breite * self._hoehe
    
#     def umfang(self):
#         return 2 * (self._hoehe + self._breite)


# rechteck = Rechteck(10, 20)

# print(rechteck.flaeche())
# print(rechteck.umfang())

# rechteck.set_breite(-1)
# rechteck.set_hoehe(-1)

# Aufgabe 3

# class Benutzer:
#     def __init__(self, benutzername, passwort):
#         self._benutzername = benutzername
#         self._passwort = passwort
#         self._ist_eingeloggt = False

#     def login(self, passwort):
#         if passwort != self._passwort:
#             print("Passwort ist falsch")
#             return
        
#         self._ist_eingeloggt = True

#     def logout(self):
#         self._ist_eingeloggt = False

#     def passwort_ändern(self, altes_pw, neues_pw):
#         if altes_pw != self._passwort:
#             print("Falsches Passwort")
#             return
        
#         if len(neues_pw) < 8:
#             print("Neues Passwort muss mindestens 8 Zeichen lang sein")
#             return

#         self._passwort = neues_pw

#     def eingeloggt(self):
#         return self._ist_eingeloggt

# benutzer = Benutzer("foo", "passwort")

# benutzer.passwort_ändern("passwort", "Passwort1!")

# Aufgabe 4

class Temperatursensor:
    def __init__(self):
        self._aktuelle_temp = 0

    def set_celsius(self, wert):
        if wert < -273.15:
            print("Temperaturen unter -273.15 °C sind physikalisch unmöglich")
            return
        
        self._aktuelle_temp = wert

    def get_celsius(self):
        return self._aktuelle_temp
    
    def get_fahrenheit(self):
        return self._aktuelle_temp * 9 / 5 + 32
    
    def erhoehen(self, wert):
        if wert < 0:
            print("Temperatur erhöhen um negative Werte ist nicht erlaubt")
            return
        
        self._aktuelle_temp = self._aktuelle_temp + wert

    def senken(self, wert):
        if wert < 0:
            print("Temperatur erhöhen um negative Werte ist nicht erlaubt")
            return
        
        # Die Aufgabe legte nicht fest, was passieren soll wenn die Temperatur
        # zu tief wären würde: wird das senken dann gar nicht durchgeführt
        # oder nur bis zur kleinstmöglichen Temperatur
        # Hier: absenken bis zur kleinstmöglichen Temperatur

        self._aktuelle_temp = self._aktuelle_temp - wert

        if self._aktuelle_temp < -273.15:
            self._aktuelle_temp = -273.15
            
        # Alternative: kein Absenken

        # neue_temperatur = self._aktuelle_temp - wert

        # if neue_temperatur < -273.15:
        #     print("Temperatur kann nicht unter -273.15 liegen")
        #     return
        
        # self._aktuelle_temp = neue_temperatur

sensor = Temperatursensor()

print(sensor.get_celsius())
sensor.senken(273)
print(sensor.get_celsius())
sensor.senken(1)
print(sensor.get_celsius())
sensor.erhoehen(400)
print(sensor.get_celsius())

# print(sensor.get_celsius())
# sensor.set_celsius(30)
# print(sensor.get_celsius())
# print(sensor.get_fahrenheit())

# sensor.set_celsius(-273.151)
    
