# Aufgabe 1
class Produkt():
    def __init__(self, Name, Preis):
        self._Name = Name
        self._Preis = Preis
        self._Lagerbestand = 0
    
    def verkaufen(self, menge):
        if self._Lagerbestand >= menge and menge >= 0:
            self._Lagerbestand = self._Lagerbestand - menge
            return
        else:
            return "Der Lagerbestand ist zu niedrig um diese Menge zu verkaufen oder eine -Zahl kann nicht angegeben werden."

    def nachbestellen(self, menge):
        if menge > 0:
            self._Lagerbestand = self._Lagerbestand + menge
            return
        else:
            return "Nichts passiert."
        
    def set_preis(self, neuer_preis):
        if neuer_preis >= 0:
            self._Preis = neuer_preis
            return
        else:
            return "Das ist nicht möglich, da der Preis nicht negativ sein kann."
    
    def get_info(self):
        return (f"Der Produktname ist: {self._Name}, hat den Preis: {self._Preis} und hat den Lagerbestand: {self._Lagerbestand}.")
            

# Aufgabe 2
class Rechteck():
    def __init__(self, breite, höhe):
        self._breite = breite
        self._höhe = höhe
    
    def set_breite(self, wert):
        if wert > 0:
            self._breite = wert
            return
        else:
            return "Der Wert kann nicht unter Nulll Liegen oder keine Zahl sein."
    
    def set_hoehe(self, wert):
        if wert > 0:
            self._höhe = wert
            return
        else:
            return "Dieser Wert ist nicht möglich."
        
    def flaeche(self):
        return (f"Der Flächeninhalt beträgt {self._breite * self._höhe} in ²")
    
    def umfang(self):
        return (f"Der Umfang des Rechtecks beträgt {self._breite* 2 + self._höhe*2}.")
    
# Aufgabe 3

class Benutzer():
    def __init__(self, Benutzername, Passwort):
        self._Benutzername = Benutzername
        self._Passwort = Passwort
        self._Ist_eingeloggt = False
    
    def login(self, passwort):
        if passwort == self._Passwort:
            self._Ist_eingeloggt = True
            return "Der Login war Erfolgreich."
        else:
            return "Der Login war nicht Erfolgreich. Falsches Passwort."
    
    def logout(self):
        if self._Ist_eingeloggt == True:
            self._Ist_eingeloggt = False
            return
        else:
            return "Du bist garnicht eingeloggt!"
    
    def passwort_ändern(self, altes_pw, neues_pw):
        Passwortlänge = 0
        for i in neues_pw:
            Passwortlänge = Passwortlänge + 1
        if altes_pw != neues_pw and Passwortlänge >= 8:
            self._Passwort = neues_pw
            return
        else:
            return "Das ist das Selbe Passwort oder das Passwort ist zu kurz."
        
    def eingeloggt(self):
        if self._Ist_eingeloggt == True:
            return "User ist eingeloggt!"
        else: 
            return "User ist nicht eingeloggt."
    
# Aufgabe 4
class Temperatursensor():
    def __init__(self):
        self._aktuelle_Temperatur_celsius = 0
    
    def set_celsius(self, Temperatur):
        self._aktuelle_Temperatur_celsius = Temperatur
        return
    
    def get_celsius(self):
        return (f"Die Temperatur gerade beträgt {self._aktuelle_Temperatur_celsius} in celsius.")
    
    def get_fahrenheit(self):
        fahrenheit = (self._aktuelle_Temperatur_celsius * 9 / 5) + 32
        return (f"Die aktuelle Temperatur in Fahrenheit beträgt {fahrenheit}.")
    
    def ehoehen(self, wert):
        if wert > 0:
            self._aktuelle_Temperatur_celsius = self._aktuelle_Temperatur_celsius + wert
            return
        else:
            return "Die Erhöhung der Temperatur ist mit der Eingabe nicht übereinstimmbar."
        
    def senken(self, wert):
        if wert > 0:
            self._aktuelle_Temperatur_celsius = self._aktuelle_Temperatur_celsius - wert
            if self._aktuelle_Temperatur_celsius <= -273.15:
                self._aktuelle_Temperatur_celsius = self._aktuelle_Temperatur_celsius + wert
                return "Die Temperatur ist zu kalt!"
            return
        else:
            return "Die Senkung der Temperatur ist nicht möglich!"


            