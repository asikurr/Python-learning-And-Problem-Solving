# car = ['Toyota', 'Lambargini', 'Odi']
# print(car)
# car.append('Ferrary')
# print(car)
# fruits = []
# fruits.append('mango')
# print(fruits)

#insert into list 

# fruits1 = ['apple', 'banana', 'mango']
# fruits1.insert(1,'apple')
# print(fruits1)

#join tow list

# fruist1 = ['banana', 'apple']
# fruits2 = ['mango','pinapple']

# fruits = fruist1 + fruits2
# print(fruits)

#Extend Method and 'append - list inside list'

fruist1 = ['banana', 'apple','mango','pinapple']
fruits2 = ['mango','pinapple']

# fruist1.extend(fruits2)
# print(fruist1)

# fruist1.append(fruits2)
# print(fruist1)

#Delete data from list using pop, del, remove

# fruist1.pop()
# print(fruist1)
# fruist1.pop(0) #position delete
# print(fruist1)

# del fruist1[1]
# print(fruist1)

#fruist1.remove('mango')
#print(fruist1)

# Check element in list
if 'mango' in fruist1:
    print("Mango is present")
else:
    print("Not present")