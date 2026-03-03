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