# Erstellt euch eine Klasse Student, mit den Attributen Name, Note und Alter
# erzeugt daraus dann 2 Objekte, und weist deren Attributen unterschiedliche Werte zu
# und gebt diese dann aus


class student:
    def __init__(self):
        self.name = ""
        self.alter = 0
        self.note = ""
        
        
student1 = student()
student2 = student()

student1.name = "Anja"
student1.alter = 23
student1.note = "1,6"

student2.name = "Christorbal"
student2.alter = 57
student2.note = "3,4"

print(student1.name)
print(student1.alter)
print("Vergleich: ", student2.name, student2.alter)


        
        
        
        
#         class Auto:
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