from dataclasses import dataclass

@dataclass
class TemperaturMessung:
    wert: float
    datum: str
    uhrzeit: str

    def __repr__(self):
        return f"TemperaturMessung({self.wert}, '{self.datum}', '{self.uhrzeit}')"


def read_file(path):
    temperaturen = []
    
    with open(path, "r") as file:
        for zeile in file:
            if not zeile.strip():
                continue

            wert_str, datum_raw, uhrzeit_raw = zeile.split()
            jahr, monat, tag = datum_raw.split("-")
            datum = f"{tag}.{monat}.{jahr}"
            uhrzeit = uhrzeit_raw.removesuffix("Uhr")
            temperaturen.append(TemperaturMessung(float(wert_str), datum, uhrzeit))
    
    return temperaturen

temperaturen = read_file("TQ5-1/Kurstage/2026-03-17/temps.txt")

for temp in temperaturen:
    print(temp)