
score = int(input("Enter your score: "));

IF score >= 90 THEN 
print("Grade A");
ELSE IF score >= 80 THEN 
print("Grade B");
ELSE IF score >= 70 THEN
    Print("Grade C");
ELSE IF score >= 60 THEN
    Print("Grade D");
ELSE 
    Print("Grade F")
END IF

//Alternative

score = int(input("Bitte Punktzahl eingeben: ")) 
if score >= 90: grade = "A" 
elif score >= 80: grade = "B" 
elif score >= 70: grade = "C" 
elif score >= 60: grade = "D" 

else: grade = "F" 
print("Note:", grade)