
# # 1.	Lege drei Variablen an: name, alter, stadt und gib sie aus.
# var1 = first_name
# var2 = age
# var3 = city

# print(var1, var2, var3)


# 2.	Rechne 7 + 3 und speichere das Ergebnis in einer Variable. Gib es aus.
print("")
print("Aufgabe 2:")
print("")

zahl_a = 7
zahl_b = 3
summe = zahl_a + zahl_b
print(summe)




# 3.	Wandle eine Zahl in einen String um.
print("")
print("Aufgabe 3:")
print("")

zahl = 42
zahl_string = str(zahl)

# 4.	Wandle einen String in eine Zahl um.
print("")
print("Aufgabe 4:")
print("")
variable = "11"
variable_zahl = int(variable)

# 5.	Frage den Nutzer nach seinem Namen und begrüße ihn.
print("")
print("Aufgabe 5:")
print("")

nutzer_name = input("Whats your name? ")
print("Hello, " + nutzer_name)


# 6.	Erstelle eine Liste mit 5 Tieren und gib das dritte Tier aus.
print("")
print("Aufgabe 6:")
print("")

Tierliste = ["Ape", "Giraffe", "Fox", "Swan", "Duck"]
print(Tierliste[2])

# 7.	Füge ein Tier am Ende der Liste hinzu.
print("")
print("Aufgabe 7:")
print("")

Tierliste.insert(len(Tierliste), "Fly")
print(Tierliste)


# 8.	Füge ein Tier an Position 1 ein.
print("")
print("Aufgabe 8:")
print("")

Tierliste.insert(0, "Elephant")
print(Tierliste)


# 9.	Entferne das letzte Element.
print("")
print("Aufgabe 9:")
print("")

Tierliste.pop(len(Tierliste) - 1)
print(Tierliste)

print("")
print("Alternative mit del:")
print("")

del Tierliste[len(Tierliste) - 1]
print(Tierliste)

# 10.	Gib alle Elemente der Liste in einer Schleife aus.
print("")
print("Aufgabe 10:")
print("")

for tier in range(len(Tierliste)):
    print(Tierliste[tier])


# 11.	Gib nur die Elemente mit geradem Index aus.
print("")
print("Aufgabe 11:")
print("")

for tier in range(len(Tierliste)):
    if tier % 2 == 0:
        print(Tierliste[tier])


# 12.	Gib das letzte Element mit negativem Index aus.
print("")
print("Aufgabe 12:")
print("")

print(Tierliste[-1])

# 13.	Tausche das erste und das letzte Element.
print("")
print("Aufgabe 13:")
print("")

Tierliste[0], Tierliste[len(Tierliste) - 1] = Tierliste[len(Tierliste) - 1], Tierliste[0]
print(Tierliste)


# 14.	Sortiere eine Liste von Zahlen.
print("")
print("Aufgabe 14:")
print("")

Tierliste.sort()
print(Tierliste)

Tierliste.sort(reverse=True)
print(Tierliste)



# 15.	Zähle, wie oft ein bestimmtes Element vorkommt.
print("")
print("Aufgabe 15:")
print("")  

count = 0
for tier in range(len(Tierliste)):
    if Tierliste[tier] == "Giraffe":
        count = count + 1
    elif Tierliste[tier] == "Elephant":
        count = count + 1
        print(Tierliste[tier], "kommt", count, "mal vor.")
    elif Tierliste[tier] == "Swan":
        count = count + 1
        print(Tierliste[tier], "kommt", count, "mal vor.")
    elif Tierliste[tier] == "Duck":
        count = count + 1
        print(Tierliste[tier], "kommt", count, "mal vor.")
    elif Tierliste[tier] == "Ape":
        count = count + 1
        print(Tierliste[tier], "kommt", count, "mal vor.")
    elif Tierliste[tier] == "Fox":
        count = count + 1
        print(Tierliste[tier], "kommt", count, "mal vor.")
    elif Tierliste[tier] == "Fly":
        count = count + 1
        print(Tierliste[tier], "kommt", count, "mal vor.")
    
