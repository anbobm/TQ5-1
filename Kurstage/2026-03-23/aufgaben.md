# Aufgabe 1

Im Ordner `/photos` befinden sich Dateien mit Namen in folgender Form:

```
DCIM-169-Geburtstagsfeier Stefan Süßmaus-29.01.2025_17h51.jpg
DCIM-258-Geburtstagsfeier Paul Pausenfreu-13.09.2025_00h32.jpg
...
```

Diese Dateien sollen mit einem Python-Skript umbenannt werden:

```
2025-01-29-1751 Geburtstagsfeier Stefan Süßmaus.jpg
2025-09-13-0032 Geburtstagsfeier Paul Pausenfreu.jpg
...
```

Du kannst dafür die die Funktionen `listdir(pfad)` zum Auflisten von Dateien in einem Ordner, und `rename(von, nach)` zum umbenennen nutzen, beide im `os`-Modul.


# Aufgabe 2: textbasierter einfacher Taschenrechner

Der Benutzer soll z.B. eingeben `"plus 3 19"`, `"minus 2 7"`, `"mal 11 5"` oder `"durch 18 3"` und das Programm soll entsprechend ausgeben `22`, `-5`, `55` oder `6`.

Benutze `split()` und denk dran, dass du Strings erst in eine Zahl umwandeln musst um damit rechnen zu können.

# Aufgabe 3

Zeichne mit [Draw.io](https://draw.io) Klassendiagramme (mit Vererbungspfeilen) für die in den vorherigen Aufgaben besprochenen Klassen (wo es Vererbung gibt).