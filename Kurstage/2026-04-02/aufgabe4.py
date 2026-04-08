class A:
    def __init__(self, b):
        self.b = b

    def methode1(self, value):
        if value == 0:
            self.b.methode1()
        elif value == 1:
            self.b.methode2()
        else:
            self.methode2()
    
    def methode2(self):
        pass

class B:
    def __init__(self, c):
        self.c = c

    def methode1(self):
        pass

    def methode2(self):
        self.c.methode1()

class C:
    def methode1(self):
        pass