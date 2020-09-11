#This program solve input negative value
#this program using getter() and setter() method

class Phone:
    def __init__(self,model_name,brand,price):
        self.model_name = model_name
        self.brand = brand
        self._price=max(price,0)
        # if price>0:
        #     self._price = price #use ('_') make Private variable
        # else:
        #     self._price = 0
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
    
    def Name_model(self):
        return f'{self.brand} {self.model_name}'

p1 = Phone('N70','Nokia',2800)

# p1.price = 500
print(p1.price) # using getter() and setter() on price then don't need to use '_' private convansion
print(p1.specification)# if you use property decorator then no need to use perenthisis for function call it work as a instance
