number = input()
number = int(number)
ausgabe = 0

for i in range(2, number, 2):
    print(i)
    print("+")
    if i > ausgabe:
        ausgabe = ausgabe + i
else:
    print(number)
    print("=")
    print(ausgabe+number)
    