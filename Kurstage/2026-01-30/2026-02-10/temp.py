temp = int(input("Gib Temperatur: "))

if temp < 0:
    print("Es ist eiskalt")
elif temp < 20:
    print("Es ist frisch")
elif temp < 30:
    print("Es ist warm")
else:
    print("Es ist zu heiss")