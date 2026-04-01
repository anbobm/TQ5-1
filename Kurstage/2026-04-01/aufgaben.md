# Aufgabe 1

Zeichne ein Klassendiagramm für folgende Klassen (mit Vererbung, Aggregation, Assoziation):

```python
class Fahrzeug:
    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def starten(self):
        print("Fahrzeug startet")


class Auto(Fahrzeug):
    def __init__(self, marke, baujahr, anzahl_tueren):
        super().__init__(marke, baujahr)
        self.anzahl_tueren = anzahl_tueren

    def hupen(self):
        print("Hup Hup!")


class Fahrrad(Fahrzeug):
    def __init__(self, marke, baujahr, typ):
        super().__init__(marke, baujahr)
        self.typ = typ

    def klingeln(self):
        print("Ring Ring!")


class Garage:
    def __init__(self, name):
        self.name = name
        self.fahrzeuge = []

    def add_fahrzeug(self, fahrzeug):
        self.fahrzeuge.append(fahrzeug)

    def liste_fahrzeuge(self):
        for f in self.fahrzeuge:
            print(f.marke)


class Besitzer:
    def __init__(self, name):
        self.name = name
        self.garage = None

    def set_garage(self, garage):
        self.garage = garage
```

# Aufgabe 2

Zeichne ein Klassendiagramm für folgende Klassen (mit Vererbung, Aggregation, Assoziation):

```python
class Benutzer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Kunde(Benutzer):
    def __init__(self, name, email, kundennummer):
        super().__init__(name, email)
        self.kundennummer = kundennummer
        self.bestellungen = []

    def bestellen(self, bestellung):
        self.bestellungen.append(bestellung)


class Admin(Benutzer):
    def __init__(self, name, email):
        super().__init__(name, email)

    def loesche_produkt(self, produkt):
        print("Produkt gelöscht")


class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis


class Bestellung:
    def __init__(self, datum):
        self.datum = datum
        self.positionen = []
        self.kunde = None

    def add_position(self, position):
        self.positionen.append(position)

    def set_kunde(self, kunde):
        self.kunde = kunde


class Bestellposition:
    def __init__(self, produkt, menge):
        self.produkt = produkt
        self.menge = menge


class Zahlung:
    def __init__(self, betrag):
        self.betrag = betrag


class Kreditkarte(Zahlung):
    def __init__(self, betrag, kartennummer):
        super().__init__(betrag)
        self.kartennummer = kartennummer


class PayPal(Zahlung):
    def __init__(self, betrag, email):
        super().__init__(betrag)
        self.email = email


class Shop:
    def __init__(self, name):
        self.name = name
        self.produkte = []
        self.bestellungen = []

    def add_produkt(self, produkt):
        self.produkte.append(produkt)

    def add_bestellung(self, bestellung):
        self.bestellungen.append(bestellung)
```

# Aufgabe 3 - Sequenzdiagramm

Gegeben sind folgende Klassen und ihre Verwendung im Hauptprogramm.

Zeichne ein Sequenzdiagramm für den Aufruf `customer.perform_withdrawal(50)`.


```python
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} eingezahlt. Neuer Kontostand: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} abgehoben. Neuer Kontostand: {self.balance}")
        else:
            print("Nicht genügend Guthaben")

class ATM:
    def __init__(self, account):
        self.account = account

    def withdraw_money(self, amount):
        print("ATM: Abhebung wird durchgeführt...")
        self.account.withdraw(amount)

class Customer:
    def __init__(self, name, account, atm):
        self.name = name
        self.account = account
        self.atm = atm

    def perform_withdrawal(self, amount):
        print(f"{self.name} möchte {amount} abheben")
        self.atm.withdraw_money(amount)


# Hauptprogramm
account = BankAccount("Max")
account.deposit(100)

atm = ATM(account)
customer = Customer("Max", account, atm)

customer.perform_withdrawal(50)
```