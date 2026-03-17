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