# Erstellt euch eine Klasse Student, mit den Attributen Name, Note und Alter
# erzeugt daraus dann 2 Objekte, und weist deren Attributen unterschiedliche Werte zu
# und gebt diese dann aus
# class Auto:
#     def __init__(self):
#         self.farbe = "grün"
#         self.geschwindigkeit = 0

# # Objekt erzeugen mit Klassenname()
# auto1 = Auto()
# auto2 = Auto()

# # Attribut ändern
# auto2.farbe = "blau"
# auto2.geschwindigkeit = 80

# # Attribut lesen/ausgeben
# print(auto1.farbe)
# print(auto1.geschwindigkeit)

# print(auto2.farbe)
# print(auto2.geschwindigkeit)

# Lösung
class Student:
    def __init__(self):
        self.name = "name"
        self.note = "note"
        self.alter = "alter"

student1 = Student()
student1.name = "Max"
student1.note = "sehr gut"   
student1.alter  = "20"

student2 = Student()
student2.name = "Lisa"
student2.note = "sehr gut"   
student2.alter  = "22"

print(student1.name), 
print(student1.note),
print(student1.alter)

print(student2.name), 
print(student2.note),
print(student2.alter)

