#Fibonacci serice

def fibonacci_seri(n):
    a=0
    b=1
    if n==0:
        print(0) 
    elif n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print (a, b, end = " ")
        for j in range(n-2):
            c = a + b
            a = b
            b = c
            print( b, end = " ")

num = int(input("Enter any number for fibonacci serice : "))
fibonacci_seri(num)

    