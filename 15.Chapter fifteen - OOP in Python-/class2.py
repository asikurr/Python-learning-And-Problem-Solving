class People:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def age_avobe_18(self):
        return self.age>18







p1 = People('Asikur','Rahaman',17)
print(p1.full_name())
print(p1.age_avobe_18())