# List comprehension means make list more easear with one line 
# before 
def info(n):
    user_info = []
    for i in range(1,n+1):
        user_info.append(i**3)
    return user_info
print(info(10))

#list comprehension 
new_list = [i**4 for i in range(1,11)]
print(new_list)

#before 
def negative_va(n):
    nagative = []
    for i in range(1,n+1):
        nagative.append(-i)
    return nagative
print(negative_va(10))

#list comprehension 
new_negative = [-i for i in range(1,11)]
print(new_negative)

#before    
names = ['asikur','rahaman','fayez','abdur']
name_lis = []
for name in names:
    name_lis.append(name)
print(name_lis)

#list comprehension 
new_name = [i  for i in names ]
print(new_name)