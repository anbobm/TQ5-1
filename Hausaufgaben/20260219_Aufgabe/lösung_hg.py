class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property #getter
    def age(self):
        return self.__age
    
    @age.setter  #setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Ungültiges Alter")

    @property  #getter
    def name(self):
        return self.__name
    
    def print_person(self):
        print(f"Name: {self.__name}\tAlter: {self.__age}")
    
bob = Person("Bob", 20)
bob.print_person()
bob.age = 240
bob.age = 25
bob.print_person()