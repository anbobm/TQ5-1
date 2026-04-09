s = "2026-03-11 15:14Uhr"

# statt:
# liste = s.split()
# datum = liste[0]
# uhrzeit = liste[1]

datum, uhrzeit = s.split()

print(f"Datum: {datum}")
print(f"Uhrzeit: {uhrzeit}")