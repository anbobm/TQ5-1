# Listen

# definieren

liste = [3, 17, "apfel"]

# mit Index auslesen:

liste[0] # 3
liste[1] # 17
liste[2] # "apfel"
liste[3] # IndexError

# in Liste schreiben

liste[1] = 53 # Liste ist jetzt [3, 53, "apfel"]

# an Liste anhängen

liste.append("birne") # Liste ist jetzt [3, 53, "apfel", "birne"]

# aus Liste entfernen (erstes Auftreten)

liste.remove(3) # Liste ist jetzt [53, "apfel", "birne"]

# es gibt noch viele weitere Funktionen für Listen, z.B. index(), insert(), etc.