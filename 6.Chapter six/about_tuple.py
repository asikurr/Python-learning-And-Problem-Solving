#looping in tuple
#tuple in one element
# tuploe without paranthesis
# tuple unpacking
# list inside tuple
# some function that you can use tuple
mix = (2,1,4,1,4,5,6,32)
# i = 0
# while i<len(mix):
#     print(mix[i])
#     i+=1

# for i in mix:
#     print(i)

#Single element with tuple 

n = (1,)
s = ('asikur',)
# print(type(n))
# print(type(s))

#Tuple without paranthesis 
name = 'asikur', 'rahaman asikur', 'rahaman'
# print(type(name))

#Tuple upaking
n1,n2,n3 = (name)
# print(n1)

#List inside tuple
nam = ('asikur','rahaman asikur',['rahaman','fayez'])
# nam[2].pop()
nam[2].append("Abdur Rahaman")
# print(nam)

# some function using tuple max-min-sum-len-count
print(sum(mix))