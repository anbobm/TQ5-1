# Schleife die die Zahlen von 0 bis 9 ausgibt
n = 0

while n < 10:
    print(n)
    n = n + 1

# Schleife die den Benutzer so lange etwas eingeben lässt, bis er "ende" eingibt
eingabe = ""

while eingabe != "ende":
    eingabe = input()
    print(f"Du hast {eingabe} eingegeben")