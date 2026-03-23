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

# Aufgabe 5

Angriffe sollen jetzt eine Zufallskomponente beinhalten. Es soll nicht immer der volle Schaden bewirkt werden. Benutze dazu `random.randint(..)`.

# Aufgabe 6

Schreibe eine Methode `ist_tot()` die zurückgibt ob der Charakter tot ist (keine Lebenspunkte mehr hat).

# Aufgabe 7

Erstelle zwei Charaktere und lasse sie in einer Schleife gegeneinander Kämpfen, bis einer von ihnen tot ist.