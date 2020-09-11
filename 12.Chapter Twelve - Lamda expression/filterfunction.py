#filter function with lamda expression 

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def is_even(n):
    return n%2==0

# even_num = list(filter(is_even,numbers))
even_num = list(filter(lambda a:a%2==0,numbers))
for i in even_num:
    print(i)
print(even_num)

#by list comprehension 
evens = [i for i in numbers if i%2==0 ]
print(evens)