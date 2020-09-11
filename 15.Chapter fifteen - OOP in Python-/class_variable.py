#Class variable
#Object oreanted programming

class Circle:
    pi_variable = 3.14 #   This called class variable
    def __init__(self,radious):#__init__ is a constructor
        self.radious = radious
    def circumfrence(self):
        return 2*Circle.pi_variable*self.radious
    
c = Circle(3)
print(c.circumfrence())