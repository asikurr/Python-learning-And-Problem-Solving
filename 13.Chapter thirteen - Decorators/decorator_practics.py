# Decorator practice 
from functools import wraps
def function_data(func):
    @wraps(func)
    def inner_func(*args,**kwargs):
        print(f'This function called {func.__name__} function')
        print(f'{func.__doc__}')
        return func(*args,**kwargs)
    return inner_func

@function_data
def addition(a,b):
    '''This function take input two number and return their sum'''
    return a+b

print(addition(5,9))