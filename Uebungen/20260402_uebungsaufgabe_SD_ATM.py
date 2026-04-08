# Aufgabe 3 - Sequenzdiagramm
# Gegeben sind folgende Klassen und ihre Verwendung im Hauptprogramm.

# Zeichne ein Sequenzdiagramm für den Aufruf customer.perform_withdrawal(50).

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