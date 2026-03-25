# Aufgabe 1
# Im Ordner /photos befinden sich Dateien mit Namen in folgender Form:

# DCIM-169-Geburtstagsfeier Stefan Süßmaus-29.01.2025_17h51.jpg
# DCIM-258-Geburtstagsfeier Paul Pausenfreu-13.09.2025_00h32.jpg

# Diese Dateien sollen mit einem Python-Skript umbenannt werden:

# 2025-01-29-1751 Geburtstagsfeier Stefan Süßmaus.jpg
# 2025-09-13-0032 Geburtstagsfeier Paul Pausenfreu.jpg
# ...
# Du kannst dafür die die Funktionen listdir(pfad) zum Auflisten von Dateien in einem Ordner, und rename(von, nach) zum umbenennen nutzen, beide im os-Modul

from os import listdir, rename, path 

ordner = r"C:\Users\brainyuser\Documents\TQ5\Test\TQ5-1\photos"
# datei = open("C:/Users/brainyuser/Documents/TQ5/Test/TQ5-1")
for datei in listdir(ordner):
    if not datei.endswith(".jpg"):
        continue
    datei_nackt = datei.removesuffix(".jpg")
    datei_geteilt = datei_nackt.split("-")
           
for wert in datei_geteilt:
    typ = wert[0],
    nummer = wert[1],
    anlass = wert[2],
    datum_uhrzeit = wert[4]
    
    datum, zeit = datum_uhrzeit.split("_")
    tag, monat, jahr = datum.split(".")
    datum_neu = f"{jahr}-{monat}-{tag}"
    stunde, minute = zeit.split("h")
    zeit_neu = f"{stunde}{minute}"
    
    datei_neu = f"{datum_neu}-{zeit_neu}-{anlass}.jpg"
    
    alte_datei = "C:/Users/brainyuser/Documents/TQ5/Test/TQ5-1/photos, datei"
    neue_datei = "C:/Users/brainyuser/Documents/TQ5/Test/TQ5-1/photos, datei_neu"
    
    rename(alte_datei, neue_datei)
    
    print(f"Umbenannte von: {datei} in {datei_neu}")
