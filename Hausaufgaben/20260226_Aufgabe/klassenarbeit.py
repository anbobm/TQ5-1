#aufgabe 1
class Produkt:
    def __init__(self, name, preis):
        self._name = name
        self._preis = preis if preis >= 0 else 0
        self._lagerbestand = 0

    def verkaufen(self, menge):
        if menge > 0 and menge <= self._lagerbestand:
            self._lagerbestand -= menge
            return True
        return False

    def nachbestellen(self, menge):
        if menge > 0:
            self._lagerbestand += menge
            return True
        return False

    def set_preis(self, neuer_preis):
        if neuer_preis >= 0:
            self._preis = neuer_preis
            return True
        return False

    def get_info(self):
        return f"Produkt: {self._name}, Preis: {self._preis}€, Lagerbestand: {self._lagerbestand}"
    
#aufgabe 2
class Rechteck:
    def __init__(self, breite, hoehe):
        self._breite = breite if breite > 0 else 1
        self._hoehe = hoehe if hoehe > 0 else 1

    def set_breite(self, wert):
        if wert > 0:
            self._breite = wert

    def set_hoehe(self, wert):
        if wert > 0:
            self._hoehe = wert

    def flaeche(self):
        return self._breite * self._hoehe

    def umfang(self):
        return 2 * (self._breite + self._hoehe)
    
#aufgabe 3
class Benutzer:
    def __init__(self, benutzername, passwort):
        self._benutzername = benutzername
        self._passwort = passwort
        self._ist_eingeloggt = False

    def login(self, passwort):
        if passwort == self._passwort:
            self._ist_eingeloggt = True
            return True
        return False

    def logout(self):
        self._ist_eingeloggt = False

    def passwort_aendern(self, altes_pw, neues_pw):
        if altes_pw == self._passwort and len(neues_pw) >= 8:
            self._passwort = neues_pw
            return True
        return False

    def eingeloggt(self):
        return self._ist_eingeloggt

#aufgabe 4
class Temperatursensor:
    def __init__(self):
        self._celsius = 0

    def set_celsius(self, wert):
        if wert >= -273.15:
            self._celsius = wert

    def get_celsius(self):
        return self._celsius

    def get_fahrenheit(self):
        return self._celsius * 9/5 + 32

    def erhoehen(self, wert):
        if self._celsius + wert >= -273.15:
            self._celsius += wert

    def senken(self, wert):
        if self._celsius - wert >= -273.15:
            self._celsius -= wert

#aufgabe 5
class Mitarbeiter:
    def __init__(self, name, gehalt):
        self.__name = name
        self.__gehalt = gehalt

    def get_gehalt(self):
        return self.__gehalt

    def gehalt_erhoehen(self, prozent):
        if prozent > 0:
            self.__gehalt += self.__gehalt * (prozent / 100)
        else:
            print("Nur positive Prozentwerte sind erlaubt.")


class Manager(Mitarbeiter):
    def __init__(self, name, gehalt, bonus):
        super().__init__(name, gehalt)
        self.__bonus = bonus

    def get_gehalt(self):
        return super().get_gehalt() + self.__bonus

    def set_bonus(self, bonus):
        if bonus >= 0:
            self.__bonus = bonus
        else:
            print("Der Bonus darf nicht negativ sein.")