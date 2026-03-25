import os

basis_ordner = os.path.dirname(__file__)
photos_ordner = os.path.join(basis_ordner, "photos")

dateien = os.listdir(photos_ordner)

for datei in dateien:
    teile = datei.split("-")

    titel = teile[2]
    datum_zeit = teile[3]

    datum, zeit_mit_endung = datum_zeit.split("_")
    zeit = zeit_mit_endung.replace("h", "").replace(".jpg", "")

    tag, monat, jahr = datum.split(".")

    neuer_name = f"{jahr}-{monat}-{tag}-{zeit} {titel}.jpg"

    alter_pfad = os.path.join(photos_ordner, datei)
    neuer_pfad = os.path.join(photos_ordner, neuer_name)

    os.rename(alter_pfad, neuer_pfad)

    print(f"{datei}  ->  {neuer_name}")

    