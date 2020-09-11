#More about Decorator
from functools import wraps
def decorator_func(functions):
    @wraps(functions)
    def inner_f(*args,**kwargs):
        """"This is inner function"""
        print('This is Awesome Function')
        return functions(*args,**kwargs) # if you use return function you should use return before this function 
    return inner_f

# @decorator_func
# def message(msg):
#     print(f'This message from {msg} function')

# message('Decorator')

@decorator_func
def add(a,b):
    '''This is add function'''
    return a+b

print(add(2,3))

print(add.__doc__)