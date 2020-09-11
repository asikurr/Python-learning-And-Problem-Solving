# Error handling part 1
# NotImplementedError
# Abstract Method// but in python language have no abstruct method

class Animal():
    def __init__(self,name):
        self.name = name
    
    def Sound(self): # This called Abstract function
        raise NotImplementedError('Please Define sub class Method')
    
class Bird(Animal):
    def __init__(self,name,baby):
        super().__init__(name)
        self.baby = baby
    
    def Sound(self):
        return 'kiu kiu'

class Cat(Animal):
    def __init__(self,name,baby):
        super().__init__(name)
        self.baby = baby
    
    def Sound(self):
        return 'meo meo'
    
b = Bird('Parrot','Small parrot')
c = Cat('Parrot','Small parrot')
print(b.Sound())
print(c.Sound())
