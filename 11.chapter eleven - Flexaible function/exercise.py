# Exercise for normal argument and * args with list comprehension 

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "Sorry...You don't pass any argument"

ls = [2,3,4]
print(to_power(4,*ls))
         