#exercise functipon return function

# def func1():
#     def inner_func1():
#         print('hi this is asik')
#     return inner_func1

# var = func1()
# var()

def outer(msg):
    def inner():
        print(f'how are you {msg}')
    return inner

var = outer('asikur')
# var()

