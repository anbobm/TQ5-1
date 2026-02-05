## Aufgabe 1
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


## Andreas Lösung
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


## Aufgabe 2

INPUT Score

IF Score > 90
    OUTPUT Grade A
END IF
IF Score > 80 AND < 90
    OUTPUT Grade B
END IF
IF Score > 70 AND < 80
    OUTPUT Grade C
END IF
IF Score > 60 AND < 70 
    OUTPUT Grade D
END IF
IF Score < 60
    OUTPUT Grade F
END IF

## Aufgabe 3

INPUT number1
INPUT number2
INPUT number3

IF number1 > number2 AND > number3
    OUTPUT number1 + "ist die größte Zahl"
END IF
IF number2 > number1 AND > number3
    OUTPUT number2 + "ist die größte Zahl"
END IF
IF number3 > number2 AND > number1
    OUTPUT number3 + "ist die größte Zahl"
END IF

## Aufgabe 4

INPUT yournumber

FOR i IN range(yournumber)
    ausgangszahl = yournumber - i
    IF ausgangszahl = 1
        OUTPUT 1
        OUTPUT 0
    END IF
    OUTPUT ausgangszahl
END FOR

## Aufgabe 5

INPUT number
ausgabe = 0
IF number mod 2 = 0
    FOR i IN range(2, number, 2)
        OUTPUT i
        OUTPUT +
        IF i > ausgabe THEN
            ausgabe = ausgabe + i
        END IF
    ELSE 
        OUTPUT number
        OUTPUT =
        OUTPUT ausgabe + number
    END FOR
ELSE
    OUTPUT "Gibe eine grade Zahl ein"
END IF
        
            
    
        
