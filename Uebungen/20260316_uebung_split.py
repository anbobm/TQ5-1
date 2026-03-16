# Aufgabe 1
# # Schreibe ein Python-Skript, welches einen Satz vom Benutzer einliest (z.B. "The quick brown fox jumps over the lazy dog") und dann zählt, wie viele Wörter in diesem String sind.

# zeile = "The quick brown fox jumps over the lazy dog".split()
# count = 0
# for word in zeile:
#     if word != "":
#         count = count + 1
#         print(f"Es gibt {count} Wörter im Satz.")

# # mit lenght        
# zeile = "The quick brown fox jumps over the lazy dog".split()
# print(f"Es gibt {len(zeile)} Wörter im Satz.")

# # mit Eingabe des Nutzers
# eingabe = input("Gib einen Satz ein: ")
# wortliste = eingabe.split()
# wörter = len(wortliste)
# print(f"Es gibt {wörter} Wörter im Satz.")


# Aufgabe 2
# Es gibt eine Datei foobar.txt mit folgendem Inhalt. Zähle die Wörter in dieser Datei mit einem Python-Skript.

# datei = open("20260316_foobar.txt")

# inhalt = datei.readline()


# wörter = inhalt.split()
# print(f"Es gibt {len(wörter)} Wörter in der Datei.")

# anzahl = 0
# for inhalt in datei:
#     anzahl = anzahl + len(inhalt.split())
# print(f"Es gibt {anzahl} Wörter in der Datei.")   
   
# Aufgabe 3
# Es gibt eine Datei foobar2.txt mit folgendem Inhalt. Zähle wie oft das Wort foo in dieser Datei vorkommt.
datei = open("20260316_foobar2.txt")

anzahl = 0

for word in datei.read().split():
    if word == "foo":
        anzahl = anzahl + 1
print(f"Es gibt {anzahl} mal das Wort \"foo\" in der Datei.")
 
    