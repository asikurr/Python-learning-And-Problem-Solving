#Using **kwargs with a functions 
#Reverse string and make capital first character
# Or not reverse string
#input as a list
#output as a first char Capital of input string

def rev_func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
    
names = ['asikur','rahaman']
print(rev_func(names,reverse_str = True))