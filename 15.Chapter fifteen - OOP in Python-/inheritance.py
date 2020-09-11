#This program about inheritance
#Discuss with two type of inheritance system

class Phone:#parant class /base class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price=max(price,0)

    @property  #whe use Decorator in method then this function work as instance
    def specification(self):
        return f'Brand {self.brand} {self.model_name} and price {self._price}'
    
    #getter() & setter()
    @property  #in python decorator property work as a getter() method
    def price(self):
        return self._price
    
    @price.setter #this called setter method it need to define after getter method
    def price(self,new_price):
        self._price = max(new_price,0)

    def MakeCall(self,phone_no):
        return f'Calling .. {phone_no}...'
    @property
    def Name_model(self):
        return f'{self.brand} {self.model_name}'

class Smartphone(Phone):#Derive class / Child class
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        # Phone.__init__(self,brand,model_name,price) # one way
        super().__init__(brand,model_name,price)# we use this method and this call inheritance
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    @property
    def specification(self):#it also called polymorphism
        return f'Brand {self.brand} Model {self.model_name} price {self._price}Tk Ram {self.ram} Internal Memory {self.internal_memory} Camera {self.rear_camera}'

p1 = Phone('Nokia','N70',2800)
smartphone = Smartphone('Huawei','P-30',90000,'8 GB','256 GB','48 Megapixel')

# p1.price = 500
# print(p1.price) # using getter() and setter() on price then don't need to use '_' private convansion
# print(p1.specification)# if you use property decorator then no need to use perenthisis for function call it work as a instance
print(p1.Name_model)
print(smartphone.Name_model)
print(smartphone.ram)
print(smartphone.specification)
