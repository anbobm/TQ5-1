# positive Zahlen: 1, 2, 3 ..
# negative Zahlen: -1, -2, -3
# die Null ist weder positiv noch negativ

zahl = int(input("Zahl! "))

if zahl > 0:
    print("Die Zahl ist positiv")
elif zahl < 0:
    print("Die Zahl ist negativ")
else:
    print("Die Zahl ist 0")

# Alternative mit gleichem Ergebnis, aber weniger ausdrucksstark

if zahl > 0:
    print("Die Zahl ist positiv")
if zahl < 0:
    print("Die Zahl ist negativ")
if zahl == 0:
    print("Die Zahl ist 0")