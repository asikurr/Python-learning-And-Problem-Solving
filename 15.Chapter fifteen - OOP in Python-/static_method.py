###Static method , it is not related with class method or instance . it can work directly
###It use with decorator method
##Method as Constructor
#Instance or object count in this program using class method and Decorated function
#class variable

class People:
    count_instance = 0
    def __init__(self,first_name,last_name,age):#Default __init__ is a constructor
        People.count_instance +=1 # Count people class instance or object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def user_constructor(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @staticmethod
    def called():
        print('This is static method...!')


    @classmethod # This is decorator function use for class method
    def count_class_instances(cls):
        return f'You have created {cls.count_instance} instances of {cls.__name__} class'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def age_avobe_18(self):
        return self.age>18

People.called()   ### Static method Ex : https://python-reference.readthedocs.io/en/latest/docs/functions/staticmethod.html

p1 = People('Asikur','Rahaman',25)
p2 = People('Asikur','Rahaman',25)
p3 = People.user_constructor('Abdul,Rahaman,25')#use user define constructor
print(p3.age)#Print from user define constructor

# print(p3.full_name())

print(p1.first_name)
print(p1.last_name)
print(p1.age)

print(People.count_class_instances())
# print(p1.count_class_instances())# you can also do this but it is not clear