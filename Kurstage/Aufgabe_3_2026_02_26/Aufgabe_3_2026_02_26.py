# Aufgabe Benutzer
class Benutzer:
    def __init__(self, benutzername, passwort):
        self._benutzername = benutzername
        self._passwort = passwort
        self._ist_eingeloggt = False

    def login(self, passwort):
        if passwort == self._passwort:
            self._ist_eingeloggt = True

    def logout(self):
        self._ist_eingeloggt = False

    def passwort_aendern(self, altes_pw, neues_pw):
        if altes_pw != self._passwort:
            return
        if len(neues_pw) < 8:
            return
        self._passwort = neues_pw

    def eingeloggt(self):
        return self._ist_eingeloggt

# Test
benutzer1 = Benutzer("natalia", "geheim123")
benutzer1.login("geheim123")
print(benutzer1.eingeloggt())

benutzer1.passwort_aendern("geheim123", "neuespasswort")
benutzer1.logout()
print(benutzer1.eingeloggt())                        