# Aufgabe 3

import os

pfad = os.path.join(os.path.dirname(__file__), "foobar2.txt")
datei = open(pfad, "r")

text = datei.read()

woerter = text.split()

anzahl = woerter.count("foo")

print("foo kommt", anzahl, "mal vor")

datei.close()