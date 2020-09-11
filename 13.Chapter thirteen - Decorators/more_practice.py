#More practics with decorator function with list comprehension 
from functools import wraps

def valid_input(func):
    @wraps(func)
    def inner_fuc(*args,**kwargs):
        if all([type(i)==int for i in args]):#list comprehension
            return func(*args,**kwargs)
        return "Please input valid number..."
        # new_type = []
        # for i in args:
        #     new_type.append(type(i) == int) #basic method
        # if all(new_type):
        #     return func(*args,**kwargs)
        # return "Please input valid number..."
    return inner_fuc

@valid_input
def add_all(*args):
    total = 0
    for i in args:
        total+=i
    return total

print(add_all(8,2,3,4,5))