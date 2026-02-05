

number = int(input("Gib eine Zahl ein: "))
for i in range(number):
    ausgangszahl = number - i
    if ausgangszahl  == 1:
        print("1")
        print("0")
    else:
        print(ausgangszahl)