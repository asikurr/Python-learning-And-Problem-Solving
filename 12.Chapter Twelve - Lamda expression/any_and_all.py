# Any and all function practice

num1 = [2,4,7,8,10]
num2 = [1,3,5,7,9,11]

# def even(ls):
#     tr = []
#     for i in ls:
#         tr.append(i%2==0)
#     return tr

# print(any(even(num1)))
# print(all(even(num1)))

# n=[]
# for i in num1:
#     n.append(i%2==0)

# print(n)

lam =  [i%2==0 for i in num1]
# print(lam)

# print(all([True, True, True, True]))

# Practice of any and all

def valid_input(*args):

    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for i in args:
            total+=i
        return total
    else:
        return "Please give integer of float number ...!"


print(valid_input(1,2,3,4,5,*[2,4,7,8,10]))