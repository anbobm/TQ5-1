# Aufgabe 1.1

# Der Benutzer soll irgendetwas eingeben und von diesem Eingabe-String soll 
# dann die Endung bar, sofern vorhanden, 
# entfernt und der Rest ausgegeben werden. z.B.:

with open("Kurstage/Aufgabe 1.1_2026_03_17/input.txt", "r") as f:
    text = f.read()

words = text.split()

with open("Kurstage/Aufgabe 1.1_2026_03_17/lange_wörter.txt", "w") as f:
    for word in words:
        if len(word) > 5:
            f.write(word + "\n")

print("Fertig")