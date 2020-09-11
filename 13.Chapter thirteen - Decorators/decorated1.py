#Decorator function - that increase the other functions functionality
#It is '@' call syntactic sugar in python this use for call decorator function call

def decorator_func(functions):
    def inner_f():
        print('This is Awesome Function')
        functions()
    return inner_f


@decorator_func
def func1():
    print('This is function one')

func1()

@decorator_func #shortcut method of decorator
def func2():
    print('This is function Two')

func2()

# func2 = decorator_func(func2) # long method 
# func2()