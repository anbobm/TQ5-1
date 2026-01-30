# Git Uebung fuer Anfaenger (Python Kurs)

## Ziel

In dieser Uebung lernst du die wichtigsten Git Grundbefehle:

-   git init
-   git status
-   git add
-   git diff
-   git log

Du arbeitest an einem kleinen Python Projekt und verfolgst deine
Aenderungen mit Git.

------------------------------------------------------------------------

## Ausgangssituation

Du beginnst ein neues Python Projekt fuer ein einfaches Taschenrechner
Programm.

------------------------------------------------------------------------

## Aufgabe

### 1. Repository erstellen

1.  Erstelle einen neuen Ordner namens `rechner`.
2.  Wechsle in diesen Ordner.
3.  Initialisiere ein Git Repository.

Hinweis:

    git init

------------------------------------------------------------------------

### 2. Erste Datei anlegen

1.  Erstelle eine Datei `rechner.py`.
2.  Fuege folgenden Inhalt ein:

``` python
print("Einfacher Rechner")

a = 2
b = 3

summe = a + b

print("Summe:", summe)
```

3.  Pruefe den Status deines Repositories.

Hinweis:

    git status

Frage:

-   Wird die Datei von Git bereits verfolgt ("getracked")?

------------------------------------------------------------------------

### 3. Datei zur Staging Area hinzufuegen

1.  Fuege `rechner.py` zur Staging Area hinzu.
2.  Pruefe erneut den Status.

Hinweis:

    git add rechner.py
    git status

Frage:

-   Was hat sich im Status geaendert?

------------------------------------------------------------------------

### 4. Datei aendern und diff ansehen

1.  Aendere `rechner.py`:

``` python
print("Einfacher Rechner")

a = 2
b = 3
c = 4

summe = a + b + c

print("Summe:", summe)
```

2.  Schaue dir die Unterschiede zur letzten Version an (Unterschied zwischen dem aktuellen Zustand und dem Zustand der Staging Area).

Hinweis:

    git diff

Frage:

-   Welche Zeilen wurden als geaendert markiert?

------------------------------------------------------------------------

### 5. Aenderungen committen

1.  Fuege die letzten Aenderungen wieder zur Staging Area hinzu.
2.  Erstelle einen Commit mit einer passenden Nachricht.

Hinweis:

    git add rechner.py
    git commit -m "Erweitere Rechner um dritte Zahl"

------------------------------------------------------------------------

### 6. Log ansehen

1.  Zeige die Commit Historie an.

Hinweis:

    git log

Frage:

-   Wie viele Commits siehst du?
-   Welche Nachricht hat dein letzter Commit?

------------------------------------------------------------------------

### 7. Weitere Datei hinzufügen

-   Fuege deinem Repository eine weitere Datei zu (bliebiger Name und Inhalt) und committe diese.
-   Nutze wieder status, diff, add, commit und log.

------------------------------------------------------------------------

## Lernziel Check

Wenn du diese Fragen beantworten kannst, hast du das Ziel erreicht:

-   Wofuer ist git init?
-   Was zeigt git status?
-   Wozu dient git add?
-   Was zeigt git diff?
-   Was sieht man in git log?
