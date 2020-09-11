# This program is describeing how to pass argument in decorator
#How to check different type of data
from functools import wraps
def args_type(data_type):
    def decorator(func):
        @wraps(func)
        def inner_type(*args,**kwargs):
            if all([type(i) == data_type for i in args]):
                return func(*args,**kwargs)
            return 'Please Give valide input...!'
        return inner_type
    return decorator

@args_type(str)
def add_input(*args):
    string = ''
    for i in args:
        string+=i
    return string
print(add_input('Asikur',' Rahaman'))

@args_type(int)
def add_number_input(*args):
    string = 0
    for i in args:
        string+=i
    return string
print(add_number_input(1,2))

@args_type(list)
def add_list_input(*args):
    string = []
    for i in args:
        string.append(i)
    return string
print(add_list_input([1,2],['Asikur','Rahaman']))