# Aufgabe 1

Schreibe eine Klasse `Produkt` mit privaten **Attributen** für *Name*, *Preis* und *Lagerbestand*. Name und Preis erwartet der Konstruktor als Parameter. Der Lagerbestand soll initial `0` sein.

Sie soll außerdem folgende **Methoden** haben:

* `verkaufen(menge)`: Eine Stückzahl `menge` des Produkts wird verkauft (nur positive Stückzahlen zulässig), allerdings nur wenn es der Lagerbestand zulässt. 
* `nachbestellen(menge)`: Eine Stückzahl `menge` des Produkts wird nachbestellt. Nur positive Stückzahlen zulässig.
* `set_preis(neuer_preis)`: Keine negativen Preise zulässig
* `get_info()`: gibt String mit allen Infos zum Produkt zurück


# Aufgabe 2

Erstelle eine Klasse `Rechteck`.

Sie hat private **Attribute** für Breite und Höhe, die der Konstruktor als Parameter erwartet.

#### Methoden:

* `set_breite(wert)`: (nur positive Werte erlauben)
* `set_hoehe(wert)`: (nur positive Werte erlauben)
* `flaeche()`: gibt Flächeninhalt zurück
* `umfang()`: gibt Umfang zurück


# Aufgabe 3

Erstelle eine Klasse `Benutzer`.

Sie hat private **Attribute** für Benutzername und Passwort, die der Konstruktor als Parameter erwartet. Außerdem hat sie ein privates Attribut `ist_eingeloggt` (Boolean), zu Anfang `False`.

#### Methoden:

* `login(passwort)`: Loggt den Benutzer ein (`ist_eingeloggt` wird `True`), wenn das Passwort übereinstimmt
* `logout()`: Loggt den Benutzer aus (ändert `ist_eingeloggt`).
* `passwort_ändern(altes_pw, neues_pw)`: ändert das Passwort auf `neues_pw`, vorausgesetzt `altes_pw` stimmt mit dem hinterlegten Passwort überein und `neues_pw` ist mindestens 8 Zeichen lang.
* `eingeloggt()`: Gibt zurück ob der Nutzer eingeloggt ist (Boolean)


# Aufgabe 4

Erstelle eine Klasse `Temperatursensor`.

Sie hat ein privates **Attribut** für die aktuelle Temperatur (in Celsius), die zu Anfang auf 0 gesetzt wird.

#### Methoden:

* `set_celsius(wert)`: Setzt die Temperatur auf den übergebenen Wert.
* `get_celsius()`: Gibt die Temperatur in Celsius zurück
*  `get_fahrenheit()`: Gibt die Temperatur in [Fahrenheit](https://www.analytics-shop.com/de/umrechnen-celsius-in-fahrenheit) zurück
* `erhoehen(wert)`: Erhöht die Temperatur um den übergebenen Wert
* `senken(wert)`: Senkt die Temperatur um den übergebenen Wert. 

**Hinweis**: Die Temperatur darf nie kleiner als `-273.15` sein.

# Aufgabe 5

Erstelle eine Klasse `Mitarbeiter` mit privaten Attributen für den Namen und das Gehalt, die der Konstruktor als Parameter erwartet.

#### Methoden:

* `get_gehalt()` gibt das Gehalt zurück
* `gehalt_erhoehen(prozent)` erhöht das Gehalt um `prozent`. Nur positive Werte sind zugelassen.

Erstelle nun eine Klasse `Manager`. Ein Manager *ist* ein Mitarbeiter, die Klasse `Manager` soll also von der Klasse `Mitarbeiter` erben.

Darüber hinaus hat die Klasse `Manager` ein privates Attribut für den Bonus, welcher als Parameter im Konstruktor erwartet wird.

#### Methoden:

* Die Methode `get_gehalt()` der Basisklasse wird überschrieben und berücksichtigt jetzt auch den zusätzlichen Bonus des Managers (Gehalt + Bonus).
* `set_bonus(bonus)` setzt den Bonus auf den Wert `bonus`. Negative Werte sind nicht erlaubt.