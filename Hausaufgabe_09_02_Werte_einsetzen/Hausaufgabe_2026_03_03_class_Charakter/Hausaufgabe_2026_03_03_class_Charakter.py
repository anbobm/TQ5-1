# Aufgabe_class_Charakter


class Charakter:
    def __init__(self, name, leben):
        self.name = name
        self.leben = leben

    def angreifen(self):
        return 10
    
    def erleiden_schaden(self, schaden):
        self.leben = self.leben - schaden
        if self.leben < 0:
            self.leben = 0
        print(self.name, "hat", schaden, "Schaden bekommen. Leben:", self.leben)




class Magier(Charakter):
    def __init__(self, name, leben, mana):
        super().__init__(name, leben)
        self.mana = mana    
    
    def zaubern(self):
        if self.mana > 0:
            self.mana = self.mana - 10
            if self.mana < 0:
                self.mana = 0
            return 20
        else:
            return 0
        


class Krieger(Charakter):
    def __init__(self, name, leben, ruestung):
        super().__init__(name, leben)
        self.ruestung = ruestung

    def angreifen(self):
        return 15   



 # Test
magier = Magier("Merlin", 50, 30)
krieger = Krieger("Conan", 80, 5)

schaden = magier.angreifen()
krieger.erleiden_schaden(schaden)

schaden = krieger.angreifen()
magier.erleiden_schaden(schaden)

schaden = magier.zaubern()
krieger.erleiden_schaden(schaden)