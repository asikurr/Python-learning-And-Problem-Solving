# Error raise example 2

class Mobile:
    def __init__(self,name):
        self.name = name
    
class Mobilestore:
    def __init__(self):
        self.mobiles = []
    
    def add_mobiles(self,new_mobile):
        if isinstance (new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be object of Mobile Class')
    

huawei = Mobile('Honor P30')
samsung = 'S10+'

mobo_stores = Mobilestore()
# print(mobo_stores.mobiles).
mobo_stores.add_mobiles(huawei)
new_mobo = mobo_stores.mobiles
print(new_mobo[0].name)

# print(mobo_stores.mobiles)