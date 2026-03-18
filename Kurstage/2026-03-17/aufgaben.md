# Aufgabe 1

Gegeben ist eine Datei `input.txt`. Lies diese Datei aus, und speichere alle Wörter, die länger als 5 Zeichen lang sind, in der Datei `lange_wörter.txt` (ein Wort pro Zeile).


`input.txt`:
```
Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum
```

# Aufgabe 2: rstrip()

Der Benutzer soll irgendetwas eingeben und von diesem Eingabe-String soll dann die Endung `bar`, sofern vorhanden, entfernt und der Rest ausgegeben werden. z.B.:

```
Eingabe? foobar
Ausgabe: foo

Eingabe? foobarbar
Ausgabe: foobar

Eingabe? Ich zahle bar
Ausgabe: Ich zahle 

Eingabe? Ich zahle bar.
Ausgabe: Ich zahle bar.
```

# Aufgabe 3: `split()`, `rstrip()`

Es ist eine Datei `dates.txt` gegeben. In dieser stehen Zeitpunkte, pro Zeile einer, mit Datum und Uhrzeit, z.B.: 

```
2026-3-22 10:24Uhr
2026-3-4 22:42Uhr
...
```

Diese Datei soll eingelesen werden und aus den Zeitpunkten eine Datei `formatted_dates.txt` generiert werden, die folgendes Format haben soll:

```
Datum: 2026-3-22
Uhrzeit: 10:24

Datum: 2026-3-4
Uhrzeit: 22:42

...
```

`dates.txt`:
```
2026-3-22 10:24Uhr
2026-3-4 22:42Uhr
2026-3-28 23:18Uhr
2026-7-21 10:25Uhr
2026-8-30 22:25Uhr
2026-3-24 20:4Uhr
2026-4-17 7:51Uhr
2026-6-26 23:39Uhr
2026-8-24 7:28Uhr
2026-5-4 19:48Uhr
2026-11-29 18:38Uhr
2026-7-18 16:30Uhr
2026-10-7 9:17Uhr
2026-6-16 19:7Uhr
2026-10-14 23:29Uhr
2026-2-8 16:34Uhr
2026-7-20 14:49Uhr
2026-6-15 17:15Uhr
2026-2-21 17:51Uhr
2026-7-1 3:41Uhr
2026-8-5 21:53Uhr
2026-7-1 19:16Uhr
2026-4-13 2:45Uhr
2026-8-10 6:28Uhr
2026-8-24 15:54Uhr
2026-6-30 0:37Uhr
2026-2-13 15:23Uhr
2026-2-22 6:47Uhr
2026-6-7 12:58Uhr
2026-10-1 21:50Uhr
```

# Aufgabe 4

Wie Aufgabe 3. Die gleiche Datei `dates.txt` soll genutzt werden, aber das Format von `formatted_dates.txt` soll so aussehen (Datumsformat jetzt Tag.Monat.Jahr anstelle von Jahr-Monat-Tag):

```
Datum: 22.3.2026
Uhrzeit: 10:24

Datum: 4.3.2026
Uhrzeit: 22:42

...
```

# Aufgabe 5

Generiere die Datei `formatted_temps.txt` im angegebenen Format aus der unten gegebenen Datei `temps.txt`.

Format von `formatted_temps.txt`:
```
Temperatur: 23.2 °C
Datum: 22.3.2026
Uhrzeit: 10:24

Temperatur: 6.0 °C
Datum: 4.3.2026
Uhrzeit: 22:42

...
```

`temps.txt`:
```
13.4 2026-10-19 19:58Uhr
19.9 2026-1-4 9:36Uhr
24.4 2026-1-10 16:42Uhr
13.3 2026-12-2 6:47Uhr
22.1 2026-3-26 9:15Uhr
11.6 2026-3-9 11:22Uhr
22.4 2026-4-4 13:3Uhr
16.3 2026-3-29 22:31Uhr
5.5 2026-8-30 2:52Uhr
20.8 2026-12-29 10:13Uhr
5.1 2026-9-20 5:38Uhr
20.1 2026-2-1 12:51Uhr
14.7 2026-6-27 22:50Uhr
8.7 2026-10-30 8:3Uhr
19.2 2026-7-17 21:38Uhr
13.5 2026-6-5 12:49Uhr
18.3 2026-1-7 7:28Uhr
6.4 2026-6-20 8:31Uhr
17.4 2026-4-11 6:57Uhr
24.0 2026-3-1 9:29Uhr
20.1 2026-4-23 11:10Uhr
6.7 2026-12-6 18:40Uhr
21.5 2026-5-2 20:44Uhr
16.1 2026-7-1 14:43Uhr
12.2 2026-2-11 0:9Uhr
14.1 2026-2-27 13:24Uhr
7.0 2026-5-16 19:24Uhr
13.8 2026-5-12 0:54Uhr
6.3 2026-8-22 8:44Uhr
22.1 2026-10-9 7:9Uhr
```

# Aufgabe 6

Erstelle eine Klasse `TemperaturMessung` mit den Attributen `wert` (`float` in Celsius), `datum` (String in der Form `22.12.2026`) und `uhrzeit` (String in der Form `3:14`).

Überschreibe in der Klasse die Methode `__repr__(self)`. Diese soll einen String **zurückgeben** der Form: `TemperaturMessung(24.5, "2026-12-24", "18:00")`.

Lies die Datei `temps.txt` ein, und erstelle eine Liste `temperaturen` von `TemperaturMessung`-Objekten, je eins pro Datensatz.

Gib dann die Liste aus mit `print(temperaturen)`.