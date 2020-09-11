#define a generator function 
#take any number as input and print sequence of even number
def even_generator(n):
    # for num in range(1,n+1):
    for num in range(2,n+1,2):#without if statement by range function
        # if num%2==0:
        yield(num)

n = even_generator(7)# it took single space of memory
for i in n:
    print(i)

for i in n:
    print(i)

# for i in even_generator(7):#if i use this it will work as a general process
#     print(i)

# for i in even_generator(7):
#     print(i)