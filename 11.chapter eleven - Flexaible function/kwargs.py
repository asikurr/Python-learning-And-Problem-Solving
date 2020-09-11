#kwargs - keyword argument
#unpacking as dictionary

def kw_args(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} : {j}")

d = {'name' : 'Asikur Rahaman','age':25,'Religion' : 'Islam'}
kw_args(**d)