#Aufgabe 1

liste = [1,2,3,4,5,66,7,8,9,10]

def max_element(liste):
    max = 0
    for item in liste:
        if item > max:
            max = item
    return max

print(f"Exersice 1 output: {max_element(liste)}")

#Aufgabe 2

liste = [1,2,-3,4,-5,6,-7,8,9,10]

def positive_element_count(liste):
    count = 0
    for item in liste:
        if item > 0:
            count = count + 1
    return count

print(f"Exersice 2 output: {positive_element_count(liste)}")

#Aufgabe 3

liste = [1,2,3,4,5,6,7,8,9,10]

def sum_odd_elements(liste):
    sum = 0
    for item in liste:
        if item % 2 == 1:
            sum = sum + item
    return sum

print(f"Exersice 3 output: {sum_odd_elements(liste)}")