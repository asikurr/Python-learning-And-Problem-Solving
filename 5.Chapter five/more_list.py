#Generate lists with range function
#Some thing more about pop
#index method
#pass list to function

#numbers = list(range(1,11))
#pop_numb = numbers.pop()

#print(pop_numb)

#pass functions
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def negative_func(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_func(number))