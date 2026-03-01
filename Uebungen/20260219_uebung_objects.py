# Erstellt euch eine Klasse Student, mit den Attributen Name, Note und Alter
# erzeugt daraus dann 2 Objekte, und weist deren Attributen unterschiedliche Werte zu
# und gebt diese dann aus


# class student:
#     def __init__(self):
#         self.name = ""
#         self.alter = 0
#         self.note = ""
        
        
# student1 = student()
# student2 = student()

# student1.name = "Anja"
# student1.alter = 23
# student1.note = "1,6"

# student2.name = "Christorbal"
# student2.alter = 57
# student2.note = "3,4"

# print(student1.name)
# print(student1.alter)
# print("Vergleich: ", student2.name, student2.alter)


        
        
      
# class Auto:
#     def __init__(self):
#     self.farbe = "grün"
#     self.geschwindigkeit = 0

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

class Auto():
    def __init__(self, marke, modell, farbe, jahr, raeder, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.farbe = farbe
        self.jahr = jahr
        self.raeder = 4
        self.tueren = tueren
        self.ps = ps
    def info(self):
        print("Hallo Michael, ich bin", self.marke, self.modell)
    
    def fahren(self):
        print("Ich fahre mit", self.ps, "PS")
     
        
auto1 = Auto("Ford", "S-Max", "weiß", 2014, 4, 5, 203)
auto2 = Auto("Ford", "Galaxy", "grau", 2008, 4, 5, 150)
auto3 = Auto("Ford", "FX150", "schwarz", 2021, 6, 4, 350)

auto3.raeder = 6

print(f"Das Auto ist ein {auto1.marke} {auto1.modell}, Farbe: {auto1.farbe} aus dem Jahr {auto1.jahr}. \
    Grundausstattung sind {auto1.raeder} Räder und dieser {auto1.marke} {auto1.modell} ist ein {auto1.tueren}-Tuerer.")
print("")
print(f"Das Auto ist ein {auto2.marke} {auto2.modell}, Farbe: {auto2.farbe} aus dem Jahr {auto2.jahr}. \
    Grundausstattung sind {auto2.raeder} Räder und dieser {auto2.marke} {auto2.modell} ist ein {auto2.tueren}-Tuerer.")
print("")
print(f"Das Auto ist ein {auto3.marke} {auto3.modell}, Farbe: {auto3.farbe} aus dem Jahr {auto3.jahr}. \
    Grundausstattung sind {auto3.raeder} Räder und dieser {auto3.marke} {auto3.modell} ist ein {auto3.tueren}-Tuerer.")
print("")

auto1.info()
auto1.fahren()
auto2.info()
auto2.fahren()
auto3.info()
auto3.fahren()