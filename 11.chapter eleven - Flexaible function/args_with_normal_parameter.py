# *args with normal parameter 

def normal_para(*args):
    multiple = 1
    for i in args:
        multiple*=i
    return multiple

# print(normal_para(2,3,4))

# *args work with list or tuple  by passing parameter 
def list_para(*args):
    multiple = 1
    for i in args:
        multiple*=i
    return multiple

# ls = [2,3,4]
ls = (9,2,4)
print(list_para(*ls))
