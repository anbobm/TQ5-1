# Aufgabe 1

Schreibe ein Python-Skript, welches einen Satz vom Benutzer einliest (z.B. `"The quick brown fox jumps over the lazy dog"`) und dann zählt, wie viele Wörter in diesem String sind.

# Aufgabe 2

Es gibt eine Datei `foobar.txt` mit folgendem Inhalt. Zähle die Wörter in dieser Datei mit einem Python-Skript.

```
foo foo foo foo foo bar bar bar foo foo bar foo foo foo 
foo foo foo foo bar foo foo bar bar bar foo foo bar 
foo foo bar foo foo bar bar bar foo foo foo foo bar 
foo bar bar foo foo foo 
foo foo foo 
bar bar bar bar foo bar foo foo bar 
bar bar foo 
bar foo 
foo foo 
bar foo foo foo foo bar foo bar bar foo foo foo bar foo foo bar foo foo bar 
foo 
bar foo foo foo 
foo bar bar foo bar bar foo 
bar foo bar foo foo 
bar foo foo bar bar bar foo 
bar foo bar foo bar foo foo bar foo bar bar bar bar bar bar foo foo foo bar foo foo bar foo 
foo bar 
bar foo foo 
bar bar bar 
bar bar bar foo foo 
foo bar bar foo bar foo bar foo 
foo 
foo bar foo bar bar foo bar bar bar bar bar foo bar bar foo bar foo bar bar bar bar foo foo bar bar foo foo bar foo foo foo 
bar 
bar foo foo bar 
foo 
foo 
foo bar bar foo foo bar foo 
bar foo foo foo foo foo bar bar 
foo bar 
bar 
foo foo 
foo foo bar bar foo bar bar foo bar bar bar foo 
bar 
foo bar bar foo bar foo bar bar foo foo bar foo bar bar foo foo bar bar foo foo bar bar foo 
bar 
foo foo foo bar bar 
bar foo bar bar foo foo foo bar bar foo bar bar foo foo 
bar foo foo bar foo bar 
bar 
foo foo bar foo foo foo 
bar bar foo bar foo foo bar bar foo foo foo foo 
foo foo 
bar foo foo foo 
foo bar bar bar bar bar bar bar bar bar foo bar bar bar foo foo foo bar bar bar foo foo bar bar bar foo bar foo foo foo bar foo foo bar bar bar foo bar bar bar foo bar foo bar foo foo bar foo bar bar 
foo foo bar 
foo foo foo bar foo bar bar foo bar foo bar foo bar 
bar foo bar bar foo foo foo bar foo bar bar bar bar 
foo bar bar bar bar foo bar bar bar foo bar foo foo foo 
bar foo bar foo foo bar bar foo bar 
foo foo 
bar foo foo bar bar foo bar foo foo 
bar bar foo foo bar 
bar foo bar 
foo 
```

# Aufgabe 3

Es gibt eine Datei `foobar2.txt` mit folgendem Inhalt. Zähle wie oft das Wort `foo` in dieser Datei vorkommt.

```
bar foo foo foo bar bar foo foo bar foo 
bar foo bar bar foo bar bar bar foo foo foo foo foo bar 
bar foo bar foo foo foo bar bar foo foo foo bar bar foo bar bar bar foo 
foo bar foo bar bar bar foo bar foo bar bar bar bar bar foo bar bar bar bar bar foo bar bar foo bar foo bar bar foo foo foo foo foo 
bar foo foo 
foo foo 
bar bar bar bar 
bar 
bar foo foo bar bar foo foo bar foo bar foo 
bar foo 
foo bar 
foo foo foo 
bar bar foo foo bar 
bar foo foo bar foo foo bar foo foo bar 
foo 
foo bar foo bar 
bar foo 
bar foo foo foo foo foo bar bar foo bar foo bar bar 
```

# Aufgabe 4

Der Benutzer soll Vornamen, Nachnamen und sein Alter eingeben. Z.B.

```
Vorname? Max
Nachname? Mustermann
Alter? 30
```

Anschließend sollen die eingebenen Daten in der Datei `person.txt` geschrieben werden, in folgender Form: `Max,Mustermann,30`

**Zusatz**:

Der Nutzer kann so lange Personendaten eingeben, bis er abbrechen möchte:

```
Vorname? Max
Nachname? Mustermann
Alter? 30
Weiter? (j/n) j
Vorname? Maxine
Nachname? Musterfrau
Alter? 25
Weiter? (j/n) n
```

Anschließend landen alle Daten in der Datei `person.txt`, pro Zeile ein Datensatz:

```
Max,Mustermann,30
Maxine,Musterfrau,25
Paul,Pausenfreu,17
Ingrid,Individuell,23
```

# Aufgabe 5

Die Datensätze aus `person.txt` sollen eingelesen und in einer Liste aus Dictionaries gespeichert werden:

```python
personen = [
    {"vorname": "Max", "nachname": "Mustermann", "alter": "30"},
    {"vorname": "Maxine", "nachname": "Musterfrau", "alter": "25"},
    ...
]
```

Überprüfe mit `print(personen)` ob du erfolgreich warst.