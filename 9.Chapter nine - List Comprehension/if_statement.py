# list comprehension with if statement


# print(number)
def even_num(n):
    nu = []
    for i in n:
        if i%2 == 0:
            nu.append(i)
    return nu

number = list(range(1,11))
# print(even_num(number))

# list comprehension with if statement
even_numb = [i for i in number if i%2 == 0]
odd_numb = [i for i in number if i%2 != 0]
odd_numb1 = [i for i in range(1,11) if i%2 != 0]

print(even_numb)
print(odd_numb)
print(odd_numb1)