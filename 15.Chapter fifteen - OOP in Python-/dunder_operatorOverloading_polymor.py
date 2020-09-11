# Dunder/Magic method
#Operator overloading
#Polymorphism

class Phone:#parant class /base class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price=max(price,0)

    def specification(self):
        return f'Brand {self.brand} {self.model_name}'
    
    def __str__(self): #print class object directly like as Phone #called nicely formattion string
        return f'Brand {self.brand} {self.model_name} and price {self._price}'
    
    def __repr__(self): # represented method use by developer
        return f'Phone (\'{self.brand}\' ,\'{self.model_name}\',{self._price})'
    
    def __len__(self):
        return len(self.specification())
    
    def __add__(self,other): #operator over loading
        return self._price + other._price

    def __mul__(self,other): #operator over loading
        return self._price * other._price

class Smartphone(Phone):#Derive class / Child class
    def __init__(self,brand,model_name,price,rear_camera):
        super().__init__(brand,model_name,price)# we use this method and this call inheritance
        self.rear_camera = rear_camera

    def specification(self):#it also called polymorphism
        return f'Brand {self.brand} Model {self.model_name} price {self._price}Tk Camera {self.rear_camera}'


p1 = Phone('Nokia','N70',2800)
p2 = Phone('Huawei','honor 8x',10000)
p3 = Smartphone('Apple','10 max',100000 , '16 mp')
print(p1 * p2)
# print(len(p1))
# print(p1)
# print(repr(p1))
# print(p1.__repr__())
# print(p1.__len__())
print(p1.specification())# Polymorphism
print(p3.specification())# Polymorphism