#map function use

number = [2,3,4,5,6]
def squere(n):
    new = []
    for i in n:
        new.append(i**2)
    return new
# print(squere(number))
#number list with list, map, lambda expression
new_num = list(map(lambda a:a**2, number))
# print(new_num)

#list comprehension 
new_list = [i**2 for i in number]
print(new_list)

#pass function in map
def sq(n):
    return n**2

n = list(map(sq,number))
print(n)

# find length with map function / using tuple or list

name = ['asikur','rahaman','fayez','abdur']
length = tuple(map(len,name))
print(length)

for i in length:
    print(i)