# Exercise 1
a = input("Bitte geben Sie eine Zahl ein: ")
b = input("Bitte geben Sie eine weitere Zahl ein: ")
operator = input("Bitte geben Sie einen Operator ein (+, -, *, /): ")

if operator == "+":
    result = float(a) + float(b)
elif operator == "-":
    result = float(a) - float(b)
elif operator == "*":
    result = float(a) * float(b)
elif operator == "/":
    if float(b) != 0:
        result = float(a) / float(b)
    else:
        result = "Fehler: Division durch Null ist nicht erlaubt."
else:
    result = "Fehler: Ungültiger Operator."

print("Das Ergebnis ist:", result)

# Exercise 2

score = int(input("Bitte geben Sie Ihre Punktzahl ein (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Ihre Note ist:", grade)

# Exercise 3

a = int(input("Bitte geben Sie die erste Zahl ein: "))
b = int(input("Bitte geben Sie die zweite Zahl ein: "))
c = int(input("Bitte geben Sie die dritte Zahl ein: "))

max = a
if b > max:
    max = b
if c > max:
    max = c
print("Die größte Zahl ist:", max)

# Exercise 4

number = int(input("Bitte geben Sie eine Zahl ein: "))

while number > 0:
    print(number)
    number = number - 1
print("Fertig!")

# Exercise 5

n = int(input("Bitte geben Sie eine Zahl ein: "))
sum = 0
i = 0
while i <= n:
    if i % 2 == 0:   
        sum = sum + i
    i = i + 1
print("Die Summe: ", sum)