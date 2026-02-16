# Aufgabe 1 
# import random

# def Max_zahl():
#     liste = [random.randint(1, 100) for _ in range(20)]
#     Höckste_zahl = max(liste)
#     return Höckste_zahl, liste

# Höckste_zahl, liste = Max_zahl()
# print("Liste:", liste)
# print("Höchste Zahl:", Höckste_zahl)

# Aufgabe 2

# import random

# def Posetive_zahlen(die_liste):
#     zahll = 0
#     for zahl in die_liste:
      
#         if zahl > 0:
#             zahll = zahll + 1
#     return zahll

# zufalls_liste = [random.randint(-50, 50) for _ in range(20)]


# ergebnis = Posetive_zahlen(zufalls_liste)

# print("Die Zufallsliste:", zufalls_liste)
# print("Anzahl der positiven Zahlen darin:", ergebnis)

#Aufgabe 3
# import random


# def summe_ungerade(die_liste):
#     gesamtsumme = 0
#     for zahl in die_liste:
       
#         if zahl % 2 != 0: 
#             gesamtsumme = gesamtsumme + zahl
#     return gesamtsumme


# zufalls_liste = [random.randint(1, 100) for _ in range(15)]
# ergebnis = summe_ungerade(zufalls_liste)


# print("Die Liste:", zufalls_liste)
# print("Die Summe der ungeraden Zahlen ist:", ergebnis)