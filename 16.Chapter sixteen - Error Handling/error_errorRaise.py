# Syntex error 
# Type error
# Name error
# function error
# index error
# indentation error
# Value Error
# Attribute Error
# Key Error

# Raise Error
def add(a,b):
    if type(a) == int and type(b) == int:
        return a+b
    raise TypeError('Sorry you input wrong type value.')

print(add('3',4))
