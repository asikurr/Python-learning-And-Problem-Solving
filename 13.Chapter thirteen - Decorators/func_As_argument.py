#function 
#function as a argument
l = [2,4,6,8]
def square(a):
    return a**2

# s = square
# print(s(5))

# print(list(map(lambda n:n**3,l)))

#function as a argument
def my_map(func,l):
    new_l = []
    for i in l:
        new_l.append(func(i))
    return new_l

print(my_map(square,l))
print(my_map(lambda item:item**3,l))#lanbda expression

def my_map2(fun,l):
    return [fun(i) for i in l]
print(my_map2(lambda item:item**4,l))#List comprehension