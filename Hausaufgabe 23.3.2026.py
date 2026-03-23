import os

pfad = "C:\Users\Sebas\Desktop\TQ5\Repo\TQ5-1\Kurstage\2026-03-23\photos"
Dateien = os.listdir(pfad)
for eintrag in Dateien:
    print(eintrag)
