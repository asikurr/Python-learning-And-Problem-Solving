# generator comprehension

def num_squar(n):
    square = (i**2 for i in range(1,n+1))
    return square

print(num_squar(10))
n = num_squar(10)
for i in n:
    print(i)

for i in n:
    print(i)
