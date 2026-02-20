# Erstelle eine Klasse Auto mit den Attributen _farbe (String), _geschwindigkeit (Integer) und _max_geschwindigkeit (Integer).

# Die initialen Werte für _farbe und _max_geschwindigkeit sollen über den Konstruktor (__init__(...)) erhalten werden. _geschwindigkeit soll initial auf 0 gesetzt werden.


# Wie durch die Konvention festgelegt, sind die Attribute privat, sollen also von außen nicht gesetzt werden. Dies wird durch den _ am Anfang des Attributnamens gekennzeichnet. Der Inhalt dieser Attribute soll sich also nur von innen, also über Methoden der Klasse ändern oder ausgelesen werden.

# Schreibe nun Methoden für die Klasse:

# info(): Die Methode gibt einen String aus, der den Zustand des Objekts darstellt, z.B.: "Dieses Auto hat die Farbe grün und die Maximalgeschwindigkeit 220. Aktuelle Geschwindigkeit ist 30".

# beschleunigen(...): die Methode bekommt einen Betrag übergeben, und die aktuelle Geschwindigkeit _geschwindigkeit des Objekts, soll um diesen erhöht werden.

# Wenn ein auto1 die Geschwindigkeit 30 hat und die Methode mit auto1.beschleunigen(15) aufgerufen wird, dann soll die Geschwindigkeit _geschwindigkeit jetzt 45 betragen.

# Ein Beschleunigen auf mehr als die Maximalgeschwindigkeit _max_geschwindigkeit soll nicht möglich sein. Wenn mit auto1.beschleunigen(15) die Maximalgeschwindigkeit überschritten werden würde, dann soll die _geschwindigkeit auf die Maximalgeschwindigkeit gesetzt werden.

# bremsen(...): Genau wie beschleunigen(...), aber die Geschwindigkeit soll um den übergebenen Betrag reduziert werden, und die Geschwindigkeit soll höchstens auf 0 reduziert werden - negative Geschwindigkeiten sollen nicht möglich sein.

# Einen getter für das Attribut _farbe: get_farbe(...), um die Farbe auslesen zu können.

# Einen setter für das Attribut _farbe: set_farbe(...), um die Farbe setzen zu können. Der setter soll sicherstellen, dass die Farbe nur auf eine der vorgeschriebenen Farben gesetzt werden kann: "rot", "grün", "blau", "schwarz", "weiß"
# Erstelle dir von der Klasse Auto dann zwei Objekte und probiere alle Methoden aus.

# Teste vor allem, ob sich durch beschleunigen(...) und bremsen(...) Geschwindigkeiten ergeben können, die nicht zugelassen sind (also kleiner 0 oder größer der Maximalgeschwindigkeit), oder Farben gesetzt werden können die nicht zugelassen sind.

# Es ist möglich, dass der Aufrufende die Methoden beschleunigen und bremsen mit negativen Werten aufruft. Das würde mit der Bedeutung von Beschleunigen und Bremsen kollidieren, außerdem könnte es dazu führen, dass unzulässige Geschwindigkeiten doch erreicht werden. Prüfe also in beiden Methoden, ob der Betrag 0 oder größer ist.




class auto:
    def __init__(self, farbe, geschwindigkeit, max_geschwindigkeit):
        self.__farbe = farbe
        self.geschwindigkeit = geschwindigkeit
        self.__max_geschwindigkeit = max_geschwindigkeit
    
    @property
    def farbe(self):
        return self.__farbe
    
    @farbe.setter
    def farbe(self, neue_farbe):
        if neue_farbe in ["rot", "grün", "blau", "schwarz", "weiß"]:
            self.__farbe = neue_farbe
        else:
            print("Ungültige Farbe")
    
    def info(self):
        print("Dieses Auto hat die Farbe", self.__farbe, "und die Maximalgeschwindigkeit", self.__max_geschwindigkeit, ". Aktuelle Geschwindigkeit ist", self.geschwindigkeit)
    
    def beschleunigen(self, pluskmh):
        if self.geschwindigkeit + pluskmh > self.__max_geschwindigkeit:
            self.geschwindigkeit = self.__max_geschwindigkeit
        else:
            self.geschwindigkeit += pluskmh
            
    def bremsen(self, minuskmh):
        if self.geschwindigkeit - minuskmh < 0:
            self.geschwindigkeit = 0
        else:
            self.geschwindigkeit -= minuskmh
            
auto1 = auto("grün", 0, 220)
auto2 = auto("schwarz", 0, 185)


auto2.farbe = "lila"

auto2.beschleunigen(30)
auto1.bremsen(15)
auto1.info()
auto2.info()


            
    