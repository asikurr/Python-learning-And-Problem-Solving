# Lambda Expression or annonymous function

#basic function
def add(a,b):
    return a+b

# print(add) #function have name

#lambda expresion
multi = lambda a,b : a*b
# print(multi(2,3))#this function have no name

#lambda expresion practice

even_odd = lambda i : i%2==0
#print(even_odd(4))

strin_len = lambda s : len(s) > 5
# print(strin_len('Asiku'))

last_str = lambda s : s[-1]
print(last_str('asikur'))
