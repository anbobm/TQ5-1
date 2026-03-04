# Aufgabe 1: RPG-System

Erstelle eine Basisklasse `Charakter` mit:

* `name`
* `leben`
* Methode `angreifen()`, die z.B. 10 Schaden zurückgibt

Erstelle zwei Unterklassen:

## Magier

* zusätzlich: `mana`
* Methode `zaubern()` (verbraucht Mana und macht mehr Schaden)

## Krieger

* zusätzlich: `ruestung`
* Überschreibt `angreifen()` (mehr Schaden)

## Bonus

Baue eine Methode `erleiden_schaden(schaden)` ein.

# Aufgabe 2

Schreibe die `angreifen()` Methode so um, dass sie jetzt nicht mehr den Schaden zurückgibt, sondern das angegriffene Objekt (Ziel) übergeben bekommt und dort den Schaden anrichtet.

# Aufgabe 3

Die Rüstung des Kriegers soll dafür sorgen, dass Angriffe auf ihn weniger Schaden verursachen.

# Aufgabe 4

Ändere die Funktionsweise von `zaubern()` so dass sie funktioniert wie `angreifen(ziel)`.