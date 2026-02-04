print("Hello, World!")
print("Habs herausgefunden!")

# Persönliche Informationen abfragen
namen = input("Gib deinen Namen ein: ")
print("Hallo, " + namen )
alter = int(input("Wie alt bist du? "))
print("Du bist also " + str(alter) + " Jahre alt.")
gewicht = input("Wie viel wiegst du? ")
print("Du wiegst " + gewicht + " kg.")
größe = input("Wie groß bist du (in cm)? ")
print("Du bist " + größe + " cm groß.")
hobby = input("Was ist dein Hobby? ")
print("Dein Hobby ist " + hobby + ".")
lieblingsfarbe = input("Was ist deine Lieblingsfarbe? ")
print("Deine Lieblingsfarbe ist " + lieblingsfarbe + ".")

# Abfragen mit If Else
note = float(input("Welche Note hast du in deinem letzten Test bekommen? "))
if note >= 1.0 and note <= 1.5:
    print("Sehr gut!")
elif note >= 1.6 and note <= 2.5:
    print("Gut!")
elif note >= 2.6 and note <= 3.5:
    print("Befriedigend!")
elif note >= 3.6 and note <= 4.5:
    print("Ausreichend!")
else:
    print("Nicht ausreichend!")



