#Instance or object count in this program using class method
#class variable

class People:
    count_instance = 0
    def __init__(self,first_name,last_name,age):# __init__ is a constructor
        People.count_instance +=1 # Count people class instance or object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod # This is decorator function use for class method
    def count_class_instances(cls):
        return f'You have created {cls.count_instance} instances of {cls.__name__} class'

    

p1 = People('Asikur','Rahaman',25)
p2 = People('Asikur','Rahaman',25)
p3 = People('Asikur','Rahaman',25)

print(p1.first_name)
print(p1.last_name)
print(p1.age)

print(People.count_class_instances())
# print(p1.count_class_instances())# you can also do this but it is not clear