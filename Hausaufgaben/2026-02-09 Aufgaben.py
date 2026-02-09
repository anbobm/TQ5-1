#Aufgabe 1
#Lege eine Variable zahl fest
#Wenn die Zahl größer oder gleich 10 ist, gib "Die Zahl ist größer oder gleich 10" auf die Kommandozeile aus.
#Ansonsten gib "Die Zahl ist kleiner als 10" aus.
#Teste das Skript für verschiedene Werte von zahl: 9, 10, 11, 1001, -1

zahl = 9
if zahl >=10:
    print("Die Zahl ist größer oder gleich 10")
else:
    print("Die Zahl ist kleiner als 10")


#Aufgabe 2
#Genau wie Aufgabe 1, aber die Variable zahl
#soll von der Kommandozeile eingelesen werden. 

zahl = int(input("Bitte gib eine Zahl ein")) 
if zahl >= 10:
    print("Die Zahl ist größer oder gleich 10")
else:
    print("Die Zahl ist kleiner als 10") 

#Aufgabe 3
#Der Benutzer soll sein Alter eingeben. Anschließend wird, falls das Alter kleiner als 18 ist "minderjährig" 
#ausgegeben, ansonsten "volljährig".

alter = int(input("Bitte dein Alter eingeben"))
if alter < 18:
    print("minderjährig")
else:
    print("volljährig)")


#Aufgabe 4
#Der Benutzer soll ein Passwort eingeben. Wenn der Benutzer
#"password123" eingegeben hat, soll ausgegeben werden 
#"Du hast das Passwort erraten!" (ansonsten passiert nichts).   

passwort = input("Bitte Passwort eingeben")
if passwort == "passwort123":
    print("Du hast das Passwort erraten")