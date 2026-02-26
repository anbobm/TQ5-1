# Aufgabe 3
# Erstelle eine Klasse Benutzer.

# Sie hat private Attribute für Benutzername und Passwort, die der Konstruktor als Parameter erwartet. Außerdem hat sie ein privates Attribut ist_eingeloggt (Boolean), zu Anfang False.

# Methoden:
# login(passwort): Loggt den Benutzer ein (ist_eingeloggt wird True), wenn das Passwort übereinstimmt
# logout(): Loggt den Benutzer aus (ändert ist_eingeloggt).
# passwort_ändern(altes_pw, neues_pw): ändert das Passwort auf neues_pw, vorausgesetzt altes_pw stimmt mit dem hinterlegten Passwort überein und neues_pw ist mindestens 8 Zeichen lang.
# eingeloggt(): Gibt zurück ob der Nutzer eingeloggt ist (Boolean)

class Benutzer:
    def __init__(self, benutzername, passwort):
        self.__benutzername = benutzername
        self.__passwort = passwort
        self.__ist_eingeloggt = False
        
    def login(self, passwort):
        if self.__passwort == passwort:
            self.__ist_eingeloggt = True
            return f"du bist eingeloggt"
        else:
            return f"Passwort falsch"
    
    def logout(self):
        self.__ist_eingeloggt = False
        return f"du bist ausgeloggt"
    
    def passwort_ändern(self, altes_pw, neues_pw):
        if len(neues_pw) >= 8 and altes_pw == neues_pw:
            self.__passwort = neues_pw
            return "Passwort geändert" 
        else:
            return "Altes und neues Passwort stimmen nicht überein"
        
    def eingeloggt(self):
        if self.__ist_eingeloggt == True:
            return "Du bist eingeloggt"
        else:
            return "Du bist ausgeloggt"
        
        