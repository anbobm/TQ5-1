# Aufgabe 1
 
Erstelle eine Klasse `Bankkonto` mit den Attributen `inhaber` (String, anfangs `""`)  und `kontostand` (Ganzzahl, anfangs `0`).
 
Erzeuge anschließend zwei Objekte aus dieser Klasse und gib ihren Attributen konkrete Werte.

# Aufgabe 2

Erstelle eine Klasse `Auto` mit den Attributen `_farbe` (String), `_geschwindigkeit` (Integer) und `_max_geschwindigkeit` (Integer).

Die initialen Werte für `_farbe` und `_max_geschwindigkeit` sollen über den Konstruktor (`__init__(...)`) erhalten werden. `_geschwindigkeit` soll initial auf `0` gesetzt werden.

Wie durch die Konvention festgelegt, sind die Attribute privat, *sollen* also von außen nicht gesetzt werden. Dies wird durch den `_` am Anfang des Attributnamens gekennzeichnet. Der Inhalt dieser Attribute soll nur von *innen*, also über Methoden der Klasse, ausgelesen oder geändert werden.

Schreibe nun Methoden für die Klasse:

* `info()`: Die Methode gibt einen String aus, der den Zustand des Objekts darstellt, z.B.: `"Dieses Auto hat die Farbe grün und die Geschwindigkeit 30"`.
