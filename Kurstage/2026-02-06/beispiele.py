# eingabe = input()
# zahl = int(eingabe)
# zahl = zahl + 1
# print(zahl)

# name = input("Wie heißt du? ")
# print("Dein Name ist " + name)

# alter = int(input("Gib dein Alter ein: "))
# alter = alter + 10
# print("In 10 Jahren bist du " + str(alter) + " Jahre alt")

# zahl = 34
# zahl2 = 35
# summe = zahl + zahl2
# print(summe)

# dividend = 7
# divisor = 3
# ganzzahliger_quotient = 7 // 3
# rest = 7 % 3
# print(str(dividend) + " durch " + str(divisor) + " ist " + str(ganzzahliger_quotient) + " Rest " + str(rest))

# compound assignments
# zahl = 5

# zahl += 3
# zahl = zahl + 3

# zahl -= 3
# zahl = zahl - 3

# zahl *= 3
# zahl = zahl * 3

# zahl /= 3
# zahl = zahl / 3

# zahl //= 3
# zahl = zahl // 3

# zahl %= 3
# zahl = zahl % 3

# def zieh_ab(zahl, noch_eine_zahl):
#     result = zahl - noch_eine_zahl
#     return result

# variable = 11
# variable2 = 15
# rückgabewert = zieh_ab(variable, variable2)
# print(rückgabewert)

# def add_3(zahl):
#     return zahl + 3

# def divide_by_2(zahl):
#     return zahl / 2

# a = add_3(5)
# print(a)

# b = divide_by_2(10)
# print(b)

# c = divide_by_2(add_3(5))
# print(c)


# from math import sqrt, pi, sin
# #sqrt: square root
# print(sqrt(16))
# print(pi)
# print(sin(pi))

# from random import randint
# print(randint(1, 6))

eingabe = input("2+2? ")

if eingabe == "4":
    print("Richtig!")
else:
    print("Falsch!")