#tuple return two value
def return_func(i,j):
    add = i+j
    multiply = i*j
    output = add, multiply
    return output

print(return_func(5,7)) #return tuple value 
k,l = return_func(5,7) # return single value
print(k)
print(l)

