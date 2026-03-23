# ohne Funktion

zahl = int(input("Gib Zahl! "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade")
else:
    print("Die Zahl ist ungerade")


# mit Funktion

def is_even(zahl):
    return zahl % 2 == 0

zahl = int(input("Gib Zahl! "))

if is_even(zahl):
    print("Die Zahl ist gerade")
else:
    print("Die Zahl ist ungerade")


# rest = zahl % 3

# if rest == 0:
#     print("Zahl ist durch 3 teilbar")
# else:
#     print("Zahl ist nicht durch 3 teilbar")