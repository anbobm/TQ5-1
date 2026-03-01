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
        self._benutzername = benutzername
        self._passwort = passwort
        self._ist_eingeloggt = False
        
    def login(self, passwort):
        if self._passwort == passwort:
            self._ist_eingeloggt = True
            print(f"du bist eingeloggt")
        else:
            print(f"Passwort falsch")
    
    def logout(self):
        self._ist_eingeloggt = False
        print(f"du bist ausgeloggt")
    
    def passwort_ändern(self, altes_pw, neues_pw):
        if len(neues_pw) >= 8 and altes_pw == self._passwort:
            self._passwort = neues_pw
            print("Passwort geändert")
        else:
            print("Altes und neues Passwort stimmen nicht überein oder das Passwort ist zu kurz")
        
    def eingeloggt(self):
        if self._ist_eingeloggt == True:
            print("Du bist eingeloggt")
        else:
            print("Du bist ausgeloggt")
        
benutzer1 = Benutzer("user", "passwort123")
benutzer2 = Benutzer("benutzer", "keinpasswort")

benutzer1.login("hfdhfu") 

print(benutzer1._benutzername)
print(benutzer1._passwort)
print(benutzer2._benutzername)
print(benutzer2._passwort)

benutzer1.passwort_ändern("hagsdg", "passwortja")