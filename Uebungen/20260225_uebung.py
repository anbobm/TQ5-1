 
class Haustier:
    def __init__(self, besitzer, name):
        self.besitzer = besitzer
        self.name = name
    
    def ausgabe(self):
        print(f"Ich bin das Haustier namens {self.name} und gehöre {self.besitzer}")

class Katze(Haustier):
    def __init__(self, besitzer, name, rasse):
        super().__init__(besitzer, name)
        self.rasse = rasse
    def miauen(self):
        print("Miau!")
    def ausgabe(self):
        super().ausgabe()
        print(f"Ich bin eine Katze")
        print(f"Meine Rasse ist {self.rasse}")

class Hund(Haustier):
    def __init__(self, besitzer, name, impfstatus):
        super().__init__(besitzer, name)
        self.impfstatus = impfstatus
    
    def bellen(self):
        print("Wuff!")
        
    def ausgabe(self):
        super().ausgabe()
        print("Ich bin ein Hund und")  
        if self.impfstatus == "geimpft":
            print("geimpft")
        else:
           print("nicht geimpft") 
        return f"Hund: {self.name}, Status: {self.impfstatus}"

Hund = Hund("Angela", "Porti", "geimpft")

Hund.ausgabe()
Hund.bellen()
 
# Die Klasse Hund soll ein eigenes Attribut geimpft bekommen.
# Überschreibe in der Klasse Hund die Ausgabemethode.

   
 