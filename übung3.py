#3.
# Find Maximum of Three Numbers
# Write pseudocode that takes three numbers as input and outputs the largest of the three.
# Example: Input 7, 2, 5 should output 7.

input = number1
input = number2
input = number3

function findmaximum(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        print(number1)
    else if number2 >= number1 and number2 >= number3:
        print(number2)
    else:
         print(number3)