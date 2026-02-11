# # Aufgabe 3
# Summiere alle Zahlen von 0 bis 100 auf.

sum = 0

# for i in range(0,100):
#     sum = sum + i
# print(sum)

# i = 0
# while i < 100:
#     sum = sum + i
#     i = i + 1
# print(sum) 

# # Aufgabe 4
# Summiere alle geraden Zahlen von 0 bis 100 auf.

# for i in range(0,100):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)

i = 0

while i < 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)