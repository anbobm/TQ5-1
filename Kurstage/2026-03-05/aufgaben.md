# Aufgabe 1

Schreibe folgende Klassen:

## Medium

Basisklasse für Medien, die in der Bibliothek zur Verfügung stehen

### Attribute:

* titel
* ist_ausgeliehen

### Methoden:

* ausleihen()
* zurueckgeben()

## Buch

Erbt von Medium

### Attribute:

* seitenzahl
* autor

## Dvd

Erbt von Medium

### Attribute:

* laufzeit
* regisseur

## Bibliothek

### Attribute:

* medien (Liste von Medien)

### Methoden:

* ausgeliehene_medien(): gibt Liste von Medien zurück, die ausgeliehen sind