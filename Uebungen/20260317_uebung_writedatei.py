# Gegeben ist eine Datei input.txt. Lies diese Datei aus, und speichere alle Wörter, die länger als 5 Zeichen lang sind, in der Datei lange_wörter.txt (ein Wort pro Zeile).

datei = open("20260317_input.txt")
ausgabe = open("20260317_lange_woerter.txt", "w")

for zeile in datei:
    words = zeile.split()
    
    for word in words:
        if len(word) > 5:
              ausgabe.write(f"{word}\n")
              print(f"{word} wurde gespeichert.")
              
datei.close()
ausgabe.close()
