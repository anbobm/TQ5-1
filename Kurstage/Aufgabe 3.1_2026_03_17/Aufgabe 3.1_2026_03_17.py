# Aufgabe 3.1

with open("Kurstage/Aufgabe 3.1_2026_03_17/dates.txt", "r") as f:
    lines = f.readlines()

with open("Kurstage/Aufgabe 3.1_2026_03_17/formatted_dates.txt", "w") as f:
    for line in lines:
        line = line.rstrip()              
        parts = line.split()             

        datum = parts[0]
        uhrzeit = parts[1].rstrip("Uhr")  

        f.write("Datum: " + datum + "\n")
        f.write("Uhrzeit: " + uhrzeit + "\n\n")