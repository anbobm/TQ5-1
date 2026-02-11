fruit = input("Gib eine Frucht ein: ")

match fruit:
    case "apple":
        print("Du hast Bock auf Apfel")
    case "pear":
        print("Du hast Bock auf Birne")
    case "banana":
        print("Du hast Bock auf Banane")
    case "cherry":
        print("Du hast Bock auf Kirsche")
    case _:
        print("Die Frucht kenn ich nicht")

if fruit == "apple":
    print("Du hast Bock auf Apfel")
elif fruit == "pear":
    print("Du hast Bock auf Birne")
elif fruit == "banana":
    print("Du hast Bock auf Banane")
elif fruit == "cherry":
    print("Du hast Bock auf Kirsche")
else:
    print("Die Frucht kenn ich nicht")