#input a list and give output as square list
#input [1,2,3,4] - output [1,4,9,16]

def squar_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

num = list(range(1,11))
print(squar_list(num))