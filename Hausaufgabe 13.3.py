def zeile_finden(dateiname, suchbegriff):
    with open(dateiname, 'r') as datei:
        zeilennummer = 1
        while True:
            zeile = datei.readline()
            if not zeile:  
                break
            if suchbegriff in zeile:
                print(f"Der Begriff '{suchbegriff}' wurde in Zeile {zeilennummer} gefunden.")
            zeilennummer += 1

