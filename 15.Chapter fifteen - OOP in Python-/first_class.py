#first class of pytho object oreanted programming
class People:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    

p1 = People('Asikur','Rahaman',25)

print(p1.first_name)
print(p1.last_name)
print(p1.age)


class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price =price
        self.name = brand_name+ '-'+model_name

laptop1 = Laptop('Lenovo','G80-50','55000Tk') 
print("Laptop Name   Brand  Model  Price")
print(laptop1.name,laptop1.brand_name,laptop1.model_name,laptop1.price )
