# * args is one kind of flexible function
# for example

def num(m,n):
    return m+n

#print(num(2,5,2,4))# This is limitation
def numbers(*args):
    total = 0
    for i in args:
        total+=i
    return total

# It's contain tuple we can use it for take multiple args or number input or pass to function
print(numbers(11,12,13)) # Solve limitation 