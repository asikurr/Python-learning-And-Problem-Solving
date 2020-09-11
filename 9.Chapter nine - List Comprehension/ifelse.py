#list comprehension with if else statement
# input = [1,2,3,4,5,6,7,8,9,10]
# output = [-1,4,-3,8,-5,12,-7,16,-9,20]

def number(n):
    new_n = []
    for i in n:
        if i%2 == 0:
            new_n.append(i*2)
        else:
            new_n.append(-i)
    return new_n
print(number([1,2,3,4,5,6,7,8,9,10]))

#list comprehension with if else statement
num = [1,2,3,4,5,6,7,8,9,10]
new_number = [i*2 if (i%2 == 0) else -i for i in num]
print(new_number)