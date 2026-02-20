# Erstellt euch eine Klasse Bankkonto mit den Attributen Inhaber und Kontostand
# erzeugt daraus 2 Objekte und weist deren Attributen unterschiedliche Werte zu
# und gebt diese dann aus.
# Aufgabe 1
class Bankkonto:
    def init(self, inhaber, kontostand):
        self.inhaber = inhaber
        self._kontostand = kontostand

    def ausgeben(self):
        print(f"Dies ist das Konto von {self.inhaber} und der Kontostand ist {self._kontostand}.")

    def einzahlen(self, betrag):
        if betrag < 0:
            print("Negative Beträge können nicht eingezahlt werden")
            return

        self._kontostand = self._kontostand + betrag
    
    def auszahlen(self, betrag):
        if betrag < 0:
            print("Negative Beträge können nicht ausgezahlt werden")
            return

        neuer_kontostand = self._kontostand - betrag

        if neuer_kontostand >= 0:
            self._kontostand = neuer_kontostand
        else:
            print("Nichts ausgezahlt, Konto nicht ausreichend gedeckt")

konto1 = Bankkonto("Max", 10)

konto1.einzahlen(-20)
konto1.ausgeben()

# konto1.ausgeben()
# konto1.einzahlen(50)
# konto1.ausgeben()
# konto1.auszahlen(70)
# konto1.ausgeben()
# konto1.auszahlen(60)
# konto1.ausgeben()

konto2 = Bankkonto("Petra", 950)

konto2.ausgeben()

