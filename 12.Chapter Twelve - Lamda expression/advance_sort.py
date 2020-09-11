# practice advance sort function

fruits1 = ['grapes','mango','apple']
f1 = sorted(fruits1)
print(f1)

fruits2 = ('grapes','mango','apple')
f2 = sorted(fruits2)
print(f2)

fruits3 = {'grapes','mango','apple'}
f3 = sorted(fruits3)
print(f3)

fruits = [
    {'name':'apple','price':150},
    {'name':'banana','price':50},
    {'name':'grapes','price':250},
    {'name':'mango','price':80}
]

sr = sorted(fruits, key = lambda i:i.get('price'),reverse =True)
print(sr)