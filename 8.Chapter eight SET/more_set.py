# more about set method
# Union and Intersection methode

s = {'a','b','v', 'd'}
# if 'as' in s:
#     print('Present')
# else:
#     print('Not present')

# for i in s:
#     print(i)

# Union operation
s1 = {1,2,3,3,4}

s2 = s | s1
# print(s2)

#Intersection 
s3 = {1,2,3,4,5,6,7,8,9}
s4 = {1,2,3,45,6,7,8,9,10,11,12}
s5 = s3 & s4
print(s5)
