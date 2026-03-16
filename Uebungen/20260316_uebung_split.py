# Schreibe ein Python-Skript, welches einen Satz vom Benutzer einliest (z.B. "The quick brown fox jumps over the lazy dog") und dann zählt, wie viele Wörter in diesem String sind.

zeile = "The quick brown fox jumps over the lazy dog".split()
count = 0
for word in zeile:
    if word != "":
        count = count + 1
        print(f"Es gibt {count} Wörter im Satz.")
        
zeile = "The quick brown fox jumps over the lazy dog".split()
print(f"Es gibt {len(zeile)} Wörter im Satz.")