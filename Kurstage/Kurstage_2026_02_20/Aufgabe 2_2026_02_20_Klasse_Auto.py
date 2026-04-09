# Aufgabe 2

class Auto:
    def __init__(self, farbe, max_geschwindigkeit):
        self._farbe = farbe
        self._max_geschwindigkeit = max_geschwindigkeit
        self._geschwindigkeit = 0

auto1 = Auto("Rot", 200)

print(auto1._farbe)
print(auto1._max_geschwindigkeit)
print(auto1._geschwindigkeit)