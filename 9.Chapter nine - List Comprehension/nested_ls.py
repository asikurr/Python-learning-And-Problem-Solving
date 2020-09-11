#list comprehension with nested list
li = [[1,2,3,],[4,5,6,],[7,8,9,],[10,11,11,],[12,13,14,]]
new_list = [[i for i in li] for j in range(1)]
print(new_list)