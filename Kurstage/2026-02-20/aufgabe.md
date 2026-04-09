# Aufgabe 1
 
Erstelle eine Klasse `Bankkonto` mit den Attributen `inhaber` (String, anfangs `""`)  und `kontostand` (Ganzzahl, anfangs `0`).
 
Erzeuge anschließend zwei Objekte aus dieser Klasse und gib ihren Attributen konkrete Werte.

# Aufgabe 2

Erstelle eine Klasse `Auto` mit den Attributen `_farbe` (String), `_geschwindigkeit` (Integer) und `_max_geschwindigkeit` (Integer).

Die initialen Werte für `_farbe` und `_max_geschwindigkeit` sollen über den Konstruktor (`__init__(...)`) erhalten werden. `_geschwindigkeit` soll initial auf `0` gesetzt werden.

Wie durch die Konvention festgelegt, sind die Attribute privat, *sollen* also von außen nicht gesetzt werden. Dies wird durch den `_` am Anfang des Attributnamens gekennzeichnet. Der Inhalt dieser Attribute soll nur von *innen*, also über Methoden der Klasse, ausgelesen oder geändert werden.

Schreibe nun Methoden für die Klasse:

* `info()`: Die Methode gibt einen String aus, der den Zustand des Objekts darstellt, z.B.: `"Dieses Auto hat die Farbe grün und die Maximalgeschwindigkeit 220. Aktuelle Geschwindigkeit ist 30"`.
* `beschleunigen(...)`: die Methode bekommt einen Betrag übergeben, und die aktuelle Geschwindigkeit `_geschwindigkeit` des Objekts, soll um diesen erhöht werden.

    Wenn ein `auto1` die Geschwindigkeit `30` hat und die Methode mit `auto1.beschleunigen(15)` aufgerufen wird, dann soll die Geschwindigkeit `_geschwindigkeit` jetzt `45` betragen.

    Ein Beschleunigen auf mehr als die Maximalgeschwindigkeit `_max_geschwindigkeit` soll nicht möglich sein. Wenn mit `auto1.beschleunigen(15)` die Maximalgeschwindigkeit überschritten werden würde, dann soll die `_geschwindigkeit` auf die Maximalgeschwindigkeit gesetzt werden.

* `bremsen(...)`: Genau wie `beschleunigen(...)`, aber die Geschwindigkeit soll um den übergebenen Betrag reduziert werden, und die Geschwindigkeit soll höchstens auf `0` reduziert werden - negative Geschwindigkeiten sollen nicht möglich sein.

* Einen **getter** für das Attribut `_farbe`: `get_farbe(...)`, um die Farbe auslesen zu können.
+ Einen **setter** für das Attribut `_farbe`: `set_farbe(...)`, um die Farbe setzen zu können. Der setter soll sicherstellen, dass die Farbe nur auf eine der vorgeschriebenen Farben gesetzt werden kann: `"rot"`, `"grün"`, `"blau"`, `"schwarz"`, `"weiß"`

Erstelle dir von der Klasse `Auto` dann zwei Objekte und probiere alle Methoden aus.

Teste vor allem, ob sich durch `beschleunigen(...)` und `bremsen(...)` Geschwindigkeiten ergeben können, die nicht zugelassen sind (also kleiner 0 oder größer der Maximalgeschwindigkeit), oder Farben gesetzt werden können die nicht zugelassen sind.

Es ist möglich, dass der Aufrufende die Methoden `beschleunigen` und `bremsen` mit negativen Werten aufruft. Das würde mit der Bedeutung von Beschleunigen und Bremsen kollidieren, außerdem könnte es dazu führen, dass unzulässige Geschwindigkeiten doch erreicht werden. Prüfe also in beiden Methoden, ob der Betrag 0 oder größer ist.