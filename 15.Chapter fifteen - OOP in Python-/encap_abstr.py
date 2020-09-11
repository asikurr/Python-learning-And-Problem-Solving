# In this program we will learn
#In python all class function Method are public there no private exist here
# Encapsulation
# Abstruction
# Data private / _price
# Python change variavle name called Name Magnling /  _className__variable
#Dunder or magic method __name__

class Phone:
    def __init__(self,model_name,brand,price):
        self.model_name = model_name
        self.brand = brand
        self.__price = price #use ('_')or ('__') make Private
    
    def MakeCall(self,phone_no):
        return f'Calling .. {phone_no}...'
    
    def Name_model(self):
        return f'{self.brand} {self.model_name}'

p1 = Phone('N70','Nokia',2800)
print(p1.Name_model())
print(p1.MakeCall('01823980517'))
print(p1.__dict__)
print(p1._Phone__price)# If you use '__'