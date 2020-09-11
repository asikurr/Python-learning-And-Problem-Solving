# Price discount
# Using class variavle
class Laptop:
    p_discount = 10 # Class Variable 
    def __init__(self,brand_name,model_name,price):#__init__ is a constructor
        self.brand_name = brand_name
        self.model_name = model_name
        self.price =price
        self.name = brand_name+ '-'+model_name
    
    def discount(self):
        dis_percent = self.price*self.p_discount/100
        print(f'Total Price is = {self.price}')
        print(f'{self.p_discount}% of discount is= {dis_percent} Tk')
        dis_price = self.price - dis_percent
        print(f'Your New Price is = {dis_price}')
        return dis_price


laptop1 = Laptop('**Lenovo','G80-50',55000) 
print("**Laptop Name   Brand  Model  Price")
print(laptop1.name,laptop1.brand_name,laptop1.model_name,laptop1.price )


print(laptop1.discount())
print(laptop1.__dict__)

laptop2 = Laptop('**Apple','NoteBook',115000) 
print("**Laptop Name   Brand  Model  Price")
print(laptop2.name,laptop2.brand_name,laptop2.model_name,laptop2.price )

laptop2.p_discount= float(input('Input your percentage : '))
# laptop2.p_discount = 15
print(laptop2.discount())
print(laptop2.__dict__) #Print name space or variale
