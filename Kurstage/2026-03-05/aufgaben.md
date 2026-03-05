# Aufgabe 1

Schreibe folgende Klassen:

## Medium

Basisklasse für Medien, die in der Bibliothek zur Verfügung stehen

### Attribute:

* `titel`
* `ist_ausgeliehen`

### Methoden:

* `ausleihen()`
* `zurueckgeben()`

## Buch

Erbt von Medium

### Attribute:

* `seitenzahl`
* `autor`

## Dvd

Erbt von Medium

### Attribute:

* `laufzeit`
* `regisseur`

## Bibliothek

### Attribute:

* `medien` (Liste von Medien)

### Methoden:

* `ausgeliehene_medien()`: gibt Liste von Medien zurück, die ausgeliehen sind


# Aufgabe 2

Erweitere die Klasse `Bibliothek` so, dass man mit `hinzufuegen(medium)` neue Medien hinzufügen kann.

# Aufgabe 3

Erstelle eine Klasse `Benutzer` mit dem Attribut `name`.

Erweitere die Klasse Medium um das Attribut `ausgeliehen_von`, welches den ausleihenden `Benutzer` speichert. Füge die Methoden `ausleihen(benutzer)` und `zurückgeben()` hinzu.

# Aufgabe 4

Füge der Klasse `Bibliothek` hinzu:

* `anzahl_medien()`: gibt die Anzahl aller Medien zurück
* `anzahl_buecher()`: gibt die Anzahl aller Bücher zurück (`type(..)`)
* `anzahl_dvds()`: gibt die Anzahl aller Dvds zurück
* `anzahl_ausgeliehen()`: gibt die Anzahl der ausgeliehenen Medien zurück
* `anzahl_verfügbar()`: gibt die Anzahl der verfügbaren Medien zurück

