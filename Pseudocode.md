
number1 = INPUT
number2 = INPUT
operator = INPUT

IF operator = "+"
    result = number1 + number2
ELSE IF operator = "-"
    result = number1 - number2
ELSE IF operator = "*"
    result = number1 * number2
ELSE IF operator = "/"
    result = number1 / number2
ELSE 
    OUTPUT "Bitte Operator angeben"
END IF
OUTPUT result


##Andreas Lösung
INPUT operand1
INPUT operand2
INPUT operator

IF operator is "+" THEN
    OUTPUT operand1 + operand2
END IF
IF operator is "-" THEN
    OUTPUT operand1 - operand2
END IF
IF operator is "*" THEN
    OUTPUT operand1 * operand2
END IF
IF operator is "/" THEN
    OUTPUT operand1 / operand2
END IF