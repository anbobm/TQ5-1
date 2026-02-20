# Erstelle eine Klasse Auto mit den Attributen _farbe (String), _geschwindigkeit (Integer) und _max_geschwindigkeit (Integer).

# Die initialen Werte für _farbe und _max_geschwindigkeit sollen über den Konstruktor (__init__(...)) erhalten werden. _geschwindigkeit soll initial auf 0 gesetzt werden.


# Wie durch die Konvention festgelegt, sind die Attribute privat, sollen also von außen nicht gesetzt werden. Dies wird durch den _ am Anfang des Attributnamens gekennzeichnet. Der Inhalt dieser Attribute soll sich also nur von innen, also über Methoden der Klasse ändern oder ausgelesen werden.

# Schreibe nun Methoden für die Klasse:

# info(): Die Methode gibt einen String aus, der den Zustand des Objekts darstellt, z.B.: "Dieses Auto hat die Farbe grün und die Maximalgeschwindigkeit 220. Aktuelle Geschwindigkeit ist 30".

# beschleunigen(...): die Methode bekommt einen Betrag übergeben, und die aktuelle Geschwindigkeit _geschwindigkeit des Objekts, soll um diesen erhöht werden.

# Wenn ein auto1 die Geschwindigkeit 30 hat und die Methode mit auto1.beschleunigen(15) aufgerufen wird, dann soll die Geschwindigkeit _geschwindigkeit jetzt 45 betragen.

# Ein Beschleunigen auf mehr als die Maximalgeschwindigkeit _max_geschwindigkeit soll nicht möglich sein. Wenn mit auto1.beschleunigen(15) die Maximalgeschwindigkeit überschritten werden würde, dann soll die _geschwindigkeit auf die Maximalgeschwindigkeit gesetzt werden.

# bremsen(...): Genau wie beschleunigen(...), aber die Geschwindigkeit soll um den übergebenen Betrag reduziert werden, und die Geschwindigkeit soll höchstens auf 0 reduziert werden - negative Geschwindigkeiten sollen nicht möglich sein.

class auto:
    def __init__(self, _farbe, _geschwindigkeit, _max_geschwindigkeit):
        self._farbe = _farbe
        self._geschwindigkeit = 0
        self._max_geschwindigkeit = _max_geschwindigkeit
        
    def info(self):
        print("Dieses Auto hat die Farbe", self._farbe, "und die Maximalgeschwindigkeit", self._max_geschwindigkeit, ". Aktuelle Geschwindigkeit ist", self._geschwindigkeit)
    
    def beschleunigen(self, pluskmh):
        if self._geschwindigkeit + pluskmh > self._max_geschwindigkeit:
            self._geschwindigkeit = self._max_geschwindigkeit
        else:
            self._geschwindigkeit += pluskmh
            
    def bremsen(self, minuskmh):
        if self._geschwindigkeit - minuskmh < 0:
            self._geschwindigkeit = 0
        else:
            self._geschwindigkeit -= minuskmh
            
    