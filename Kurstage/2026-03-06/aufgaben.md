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

# Aufgabe 3

Ergänze die Klasse `Unternehmen` um eine Methode `info()`, die alle Informationen zum Unternehmen, den Abteilungen und ihrer Mitarbeiter ausgibt, z.B. so:

```
Unternehmen X
    Abteilung A
        Mitarbeiter 1
        Mitarbeiter 2
    Abteilung B
        Mitarbeiter 3
    Abteilung C
        Mitarbeiter 4
        Mitarbeiter 5
        Mitarbeiter 6
```

# Aufgabe 4

Ergänze die Klasse `Mitarbeiter` um ein Attribut `abteilung`. Mit diesem soll sichergestellt werden, dass man einen Mitarbeiter nur einer Abteilung zuweisen kann.

# Aufgabe 5

Wir wollen durchsetzen, dass die `personalnummer` des `Mitarbeiter`s in einem `Unternehmen` eindeutig ist. Dazu erstellen wir eine `mitarbeiter_erzeugen()` Methode in `Unternehmen`, der einen `Mitarbeiter` nur erstellt, wenn es die übergebene `personalnummer` nicht gibt. Der Konstruktor von `Mitarbeiter` soll nur von dieser Methode aufgerufen werden.