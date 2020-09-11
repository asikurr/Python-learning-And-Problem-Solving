#Function with all parameter
#very important to know 

# Normal parameter
# *args
# default parameter
# **kwargs

def parameters(name,*args,last_name = 'Rahaman',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


parameters('Asikur',1,2,3, a=3,b=5)