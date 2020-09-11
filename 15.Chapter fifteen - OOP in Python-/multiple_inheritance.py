# Multiple inheritance

class A:
    def class_a(self):
        return 'I\'m is for class A'
    
    def hello(self):
        return 'Hello for class A'

class B:
    def class_b(self):
        return 'I\'m is for class B'
    
    def hello(self):
        return 'Hello for class B'
    
class C(B,A):#You can change order (A or B) and this Called multiple inheritance
    pass

instance = C()
print(instance.hello())
# print(A.__mro__)
# print(C.mro())
print(help(C))