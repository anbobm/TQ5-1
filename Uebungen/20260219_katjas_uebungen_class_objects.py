# 1. Erstelle eine Klasse „Auto“ mit den Attributen marke und ps.
# # Beispielziel: Ein Objekt erzeugen und die Werte ausgeben.
print("")
print("Aufgabe 1:")
print("")
class car:
    def __init__(self):
        self.brand = "none"
        self.ps = 0
    def fahren(self):
        print("Das Auto fährt")
        
          
car1 = car()
car2 = car()
car1.brand = "Lexus"
car1.ps = 256
car2.brand = "Dodge"
car2.ps = 450

print(car1.brand, car1.ps)
print(car2.brand, car2.ps)


# 2. Füge der Klasse „Auto“ eine Methode fahren() hinzu, die „Das Auto fährt“ ausgibt.
print("")
print("Aufgabe 2:")
print("")


car1.fahren()


# 3. Erstelle zwei Auto‑Objekte und gib jeweils die Marke aus.
print("")
print("Aufgabe 3:")
print("")
print("Auto 1 Marke:" + car1.brand, "Auto 2 Marke:" + car2.brand)

# 4. Schreibe eine Klasse „Hund“ mit Attribut name und einer Methode bellen().
print("")
print("Aufgabe 4:")
print("")
class hund:
    def __init__(self, name):
        self.name = name
    def bellen(self):
        print("Wuff, wuff!")
        
hund1 = hund("Wauzi")
hund1.bellen()


# 5. Erstelle eine Klasse „Rechteck“ mit Attributen breite und hoehe und einer Methode flaeche().
# print("")
# print("Aufgabe 5:")
# print("")
# class rechteck:
#     def __init_ (self, breite, hoehe):
#         self.breite = breite
#         self.hoehe = hoehe
#     def flaeche(self):
#             return self.breite * self.hoehe
        
# rechteck1 = rechteck(int(input("Breite: ")), int(input("Höhe: ")))

# print("Die Fläche ist ",rechteck1.flaeche(), "Quadratmeter.")


# 6. Schreibe eine Klasse „Schueler“ mit name und note. Gib die Note aus.
print("")
print("Aufgabe 6:")
class schueler:
    def __init_ (self, name, note):
        self.name = name
        self.note = note
   
   # 7. Füge der Klasse „Schueler“ eine Methode ist_bestanden() hinzu (Note ≤ 4).
    def status(self):
        if self.note <= 4:
            print("Bestanden")
        else:
            print("Nicht bestanden")   
            
schueler1 = schueler()
schueler2 = schueler()

schueler1.name = "Brit"
schueler2.name = "Daniel"
schueler1.note = 3
schueler2.note = 5

print(f"Die Note von {schueler1.name} ist {schueler1.note}; also {schueler1.status}")
print(f"Die Note von {schueler2.name} ist {schueler2.note}; also {schueler2.status}")
schueler1.status()
schueler2.status()


# 8. Erstelle eine Klasse „Konto“ mit kontostand und einer Methode einzahlen(betrag).

class Konto:
    def __init__(self, kontostand):
        self.kontostand = kontostand
        
    def einzahlen (self, betrag):
        if betrag <=0:
            print("Nur positive Beträge einzahlen")
        else:
            self.kontostand = self.kontostand + betrag
            print(f"Du hast {betrag}Euro eingezahlt. Dein Kontostand beträgt jetzt {self.kontostand}Euro.")
            
    # 9. Erweitere „Konto“ um eine Methode abheben(betrag).
    def abheben(self, betrag):
        if betrag > self.kontostand:
            print("Dein Guthaben reicht nicht aus.")
        else:
            self.kontostand = self.kontostand - betrag
            print(f"Du hast {betrag}Euro abgehoben. Dein Kontostand beträgt jetzt {self.kontostand}Euro.")
            
konto1 = Konto(2400)
konto2 = Konto(325)

konto1.einzahlen(4375)
konto2.abheben(500)


# 10. Schreibe eine Klasse „Person“ mit name und alter. Füge eine Methode vorstellen() hinzu.
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def vorstellen(self):
        print(f"Die Person heißt {self.name} und ist {self.alter} Jahre alt.")
        
person1 = Person("Herbert", 81)
person2 = Person("Christorbal", 45)
person3 = Person("Ihor", 24)

person1.vorstellen()
person2.vorstellen()
person3.vorstellen()


# 11. Erstelle eine Klasse „Lampe“ mit Attribut an (True/False) und Methoden einschalten() und ausschalten().



# 12. Schreibe eine Klasse „Buch“ mit titel, autor und einer Methode info().



# 13. Erstelle eine Klasse „Punkt“ mit x und y und einer Methode verschieben(dx, dy).
# 14. Schreibe eine Klasse „Timer“, die beim Erstellen eine Zahl bekommt und eine Methode tick() hat, die die Zahl um 1 verringert.
# 15. Erstelle eine Klasse „Spieler“ mit leben und einer Methode treffer(), die leben um 1 reduziert.