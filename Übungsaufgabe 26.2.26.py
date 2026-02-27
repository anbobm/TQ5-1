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
            print("Nichts passiert.")
            return 
        
    def set_preis(self, neuer_preis):
        if neuer_preis >= 0:
            self._Preis = neuer_preis
            return
        else:
            print("Das ist nicht möglich, da der Preis nicht negativ sein kann.")
            return 
    
    def get_info(self):
        print (f"Der Produktname ist: {self._Name}, hat den Preis: {self._Preis} und hat den Lagerbestand: {self._Lagerbestand}.")
        return 
            
Produkt1 = Produkt("Apfel", 3)

Produkt1.nachbestellen(-2)
Produkt1.get_info()
Produkt1.nachbestellen(3)
Produkt1.get_info()

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
            print("Der Wert kann nicht unter Null Liegen oder keine Zahl sein.")
            return 
    
    def set_hoehe(self, wert):
        if wert > 0:
            self._höhe = wert
            return
        else:
            print("Dieser Wert ist nicht möglich.")
            return 
        
    def flaeche(self):
        print(f"Der Flächeninhalt beträgt {self._breite * self._höhe} in ²")
        return 
    
    def umfang(self):
        print(f"Der Umfang des Rechtecks beträgt {self._breite* 2 + self._höhe*2}.")
        return 
    
# Aufgabe 3

class Benutzer():
    def __init__(self, Benutzername, Passwort):
        self._Benutzername = Benutzername
        self._Passwort = Passwort
        self._Ist_eingeloggt = False
    
    def login(self, passwort):
        if passwort == self._Passwort:
            self._Ist_eingeloggt = True
            print("Der Login war Erfolgreich.")
            return 
        else:
            print("Der Login war nicht Erfolgreich. Falsches Passwort.")
            return 
    
    def logout(self):
        if self._Ist_eingeloggt == True:
            self._Ist_eingeloggt = False
            return
        else:
            print("Du bist garnicht eingeloggt!")
            return 
    
    def passwort_ändern(self, altes_pw, neues_pw):
        Passwortlänge = 0
        for i in neues_pw:
            Passwortlänge = Passwortlänge + 1
        if altes_pw != neues_pw and Passwortlänge >= 8:
            self._Passwort = neues_pw
            return
        else:
            print("Das ist das Selbe Passwort oder das Passwort ist zu kurz.")
            return 
        
    def eingeloggt(self):
        if self._Ist_eingeloggt == True:
            print("User ist eingeloggt!")
            return 
        else: 
            print("User ist nicht eingeloggt.")
            return 
    
# Aufgabe 4
class Temperatursensor():
    def __init__(self):
        self._aktuelle_Temperatur_celsius = 0
    
    def set_celsius(self, Temperatur):
        self._aktuelle_Temperatur_celsius = Temperatur
        return
    
    def get_celsius(self):
        print(f"Die Temperatur gerade beträgt {self._aktuelle_Temperatur_celsius} in celsius.")
        return 
    
    def get_fahrenheit(self):
        fahrenheit = (self._aktuelle_Temperatur_celsius * 9 / 5) + 32
        print(f"Die aktuelle Temperatur in Fahrenheit beträgt {fahrenheit}.")
        return 
    
    def ehoehen(self, wert):
        if wert > 0:
            self._aktuelle_Temperatur_celsius = self._aktuelle_Temperatur_celsius + wert
            return
        else:
            print("Die Erhöhung der Temperatur ist mit der Eingabe nicht übereinstimmbar.")
            return 
        
    def senken(self, wert):
        if wert > 0:
            self._aktuelle_Temperatur_celsius = self._aktuelle_Temperatur_celsius - wert
            if self._aktuelle_Temperatur_celsius <= -273.15:
                self._aktuelle_Temperatur_celsius = self._aktuelle_Temperatur_celsius + wert
                print("Die Temperatur ist zu kalt!")
                return 
            return
        else:
            print("Die Senkung der Temperatur ist nicht möglich!")
            return 

# Aufgabe 5
class Mitarbeiter():
    def __init__(self, Namen, Gehalt):
        self._Namen = Namen
        self._Gehalt = Gehalt
    
    def get_gehalt(self):
        print(f"Der Mitarbeiter {self._Namen} bekommt das Gehalt {self._Gehalt}.")
        return 
    
    def gehalt_erhoehen(self, prozent):
        if prozent > 0.0:
            self._Gehalt = self._Gehalt + self._Gehalt * prozent
            return
        else:
            print("Funktioniert so nicht.")
            return 
    
class Manager(Mitarbeiter):
    def __init__(self, Namen, Gehalt, Bonus):
        super().__init__(Namen, Gehalt)
        self._Bonus = Bonus
    
    def get_gehalt(self):
        print(f"Der Manager {self._Namen} bekommt das Gehalt {self._Gehalt + self._Bonus}.")
        return 
    
    def set_bonus(self,bonus):
        if bonus > 0:
            self._Bonus = bonus
            return
    
    

