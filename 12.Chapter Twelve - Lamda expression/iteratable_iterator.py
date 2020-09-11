num = [2,3,4,5,7] #list,tuple,string ------- iterable
square = map(lambda a: a**2, num) #---------iterator
j = list(square)
for i in j:
    print(i)
#How to work for loop
# num_iter = iter(num)
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))