# Aufgabe 1

## Klasse `Unternehmen`

### Attribute

* `name`
* `abteilungen`: Liste von Objekten vom Typ `Abteilung` ist

### Methoden

* `abteilung_hinzufügen(abteilung)`
* `abteilung_entfernen(abteilung)`

## Klasse `Abteilung`

### Attribute

* `bezeichnung`
* `mitarbeiter`: Liste von Objekten vom Typ `Mitarbeiter`

### Methoden

* `mitarbeiter_hinzufügen(mitarbeiter)`
* `mitarbeiter_entfernen(mitarbeiter)`

## Klasse `Mitarbeiter`

### Attribute

* `personalnummer`
* `name`


# Aufgabe 2

Ergänze die Klasse `Unternehmen` um folgende Methoden:

* `abteilung_finden(bezeichnung)`

* `alle_mitarbeiter_anzeigen()`

* `mitarbeiter_suchen(personalnummer)`