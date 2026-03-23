class Auto:
    def __init__(self):
        self.farbe = "grün"
        self.geschwindigkeit = 0
        self.max_geschwindigkeit = 220

# Objekt erzeugen mit Klassenname()
auto1 = Auto()
auto2 = Auto()

# Attribut ändern
auto2.farbe = "blau"
auto2.geschwindigkeit = 230

# Attribut lesen/ausgeben
print(auto1.farbe)
print(auto1.geschwindigkeit)

print(auto2.farbe)
print(auto2.geschwindigkeit)


# Erstellt euch eine Klasse Student, mit den Attributen Name, Note und Alter
# erzeugt daraus dann 2 Objekte, und weist deren Attributen unterschiedliche Werte zu
# und gebt diese dann aus

class Student:
    def __init__(self, name, note, alter):
        self._name = name # Attribut mit _ bedeutet: "privat", soll von außen nicht geändert werden
        self._note = note
        self._alter = alter

student1 = Student("Paul", "sehr gut", 30)

student2 = Student("Petra", "sehr gut", 19)
# Attribut kann trotz _ geändert werden, ist im Normallfall keine gute Idee
student2._note = "gut"

print(student1._name)
print(student1._note)
print(student1._alter)

print(student2._name)
print(student2._note)
print(student2._alter)

auto = Auto
print(auto)