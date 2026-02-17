# Aufgabe
# Gegeben ist folgende Beispielliste:

# liste = [4, 7, 2, 9, 3, 8, 5]
# Daraus soll ein Code berechnet werden nach folgendem Schema.

# Die Liste soll durchlaufen werden, und:
# Wenn der Wert gerade ist, dann soll er zum Code addiert werden
# Wenn der Wert ungerade ist, dann soll er vom Code subtrahiert werden
# aber:
# wenn der Index des Wertes gerade ist, wird er vorher verdoppelt
# wenn der Index ungerade ist, wird er nicht verdoppelt
# Für die Liste oben:

# liste[0] = 4: Index ist gerade: verdoppeln, Wert ist gerade: addieren. also +8
# liste[1] = 7: Index ist ungerade: nicht verdoppeln, Wert ist ungerade: subtrahieren. Also -7
# liste[2] = 2: Index ist gerade: verdoppeln, Wert ist gerade: addieren. Also +4
# liste[3] = 9: Index ist ungerade: nicht verdoppeln, Wert ist ungerade: subtrahieren. Also -9
# liste[4] = 3: Index ist gerade: verdoppeln, Wert ist ungerade: subtrahieren. Also -6
# liste[5] = 8: Index ist ungerade: nicht verdoppeln, Wert ist gerade: addieren. Also +8
# liste[6] = 5: Index ist gerade: verdoppeln, Wert ist ungerade: subtrahieren. Also -10
# Der Code ist also 0 + 8 - 7 + 4 - 9 - 6 + 8 - 10 = -12 für die Beispielliste.

# Finde jetzt den Code für

liste = [3, 9, 6, 6, 5, 5, 5, 4, 5, 8, 2, 8, 6, 7, 3, 7, 6, 8, 6, 9, 9, 3, 7, 9, 1, 5, 5, 7, 8, 5, 2, 1, 3, 9, 7, 9, 8, 9, 6, 9, 6, 5, 6, 3, 3, 7, 4, 9, 9, 5, 4, 9, 9, 8, 1, 9, 8, 9, 8, 6, 1, 8, 3, 3, 2, 4, 9, 2, 6, 2, 9, 3, 9, 6, 8, 4, 5, 4, 4, 3, 8, 8, 1, 3, 4, 2, 8, 3, 5, 7, 4, 4, 1, 3, 3, 3, 2, 9, 9, 8]

wert = 0
for i in range(len(liste)):
    if i % 2 == 0: 
        if liste[i] % 2 == 0:  
            wert += liste[i] * 2
        else:  
            wert -= liste[i] * 2
    else: 
        if liste[i] % 2 == 0: 
            wert += liste[i]
        else: 
            wert -= liste[i]
            print(wert) 
            


# andere Lösung:
            wert = 0
for i in range(len(liste)):
    if i % 2 == 0: 
        if liste[i] % 2 == 0:  
            wert = wert + liste[i] * 2
        else:  
            wert = wert -liste[i]
    else: 
        if liste[i] % 2 == 0:  
            wert = wert + wert
        else: 
            wert = wert - wert
print(wert)


#  Katja:
    
code = 0
for i in range(len(liste)):
    x = liste[i]
    if i % 2 == 0:
        x *= 2
    code += x if x % 2 == 0 else -x
print(code)