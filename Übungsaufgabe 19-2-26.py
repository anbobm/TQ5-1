class Auto:
    def __init__(self):
        self.farbe = "grün"
        self.geschwindigkeit = 0

# Objekt erzeugen mit Klassenname()
auto1 = Auto()
auto2 = Auto()

# Attribut ändern
auto2.farbe = "blau"
auto2.geschwindigkeit = 80

# Attribut lesen/ausgeben
print(auto1.farbe)
print(auto1.geschwindigkeit)

print(auto2.farbe)
print(auto2.geschwindigkeit)

# Erstellt euch eine Klasse Student, mit den Attributen Name, Note und Alter
# erzeugt daraus dann 2 Objekte, und weist deren Attributen unterschiedliche Werte zu
# und gebt diese dann aus

class Student:
    def __init__(self):
        self.name = "Patrik"
        self.note = 5.0
        self.alter = 32

    def show_info(self):
        print("Name:", self.name)
        print("Note:", self.note)
        print("Alter:", self.alter)

student1 = Student()
student2 = Student()

student2.name = "Alex"
student2.note = 1.0
student2.alter = 18

student1.show_info()
student2.show_info()

