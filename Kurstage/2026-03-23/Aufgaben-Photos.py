import os

pfad = "C:\\Users\\brainyuser\\Desktop\\TQ5\\TQ5 Repository\\Hausaufgaben\\photos"
Dateien = os.listdir(pfad)

# for eintrag in Dateien:
    

for datei in os.listdir(pfad):
    datei_geteilt = datei.split("-")
    titel = datei_geteilt[2]
    date_time = datei_geteilt[3]
    date, time = date_time.split("_")
    time = time.removesuffix(".jpg")
    tag, monat, jahr = date.split(".")
    neues_datum = f"{jahr}-{monat}-{tag}"
    hour, minute = time.split("h")
    neue_zeit = f"{hour}{minute}"
    datei_neu = f"{neues_datum}-{neue_zeit} {titel}.jpg"

    alte_datei = os.path.join(pfad, datei)
    neue_datei = os.path.join(pfad, datei_neu)
    os.rename(alte_datei, neue_datei)
    print(f"{datei} \n{datei_neu}")