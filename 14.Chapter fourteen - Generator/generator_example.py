#Create a generator function with generator
#Why we use generator
#Because generator reduce memory space and make program faster

def print_num(n):
    for i in range(1,n+1):
        yield(i) #if i used generator function 'yield' new we can see that
# generator don't return any value
print(print_num(10))#generator created

num = print_num(10) # this sequence took memory one time

for n in num:
    print(n)

for n in num:
    print(n)