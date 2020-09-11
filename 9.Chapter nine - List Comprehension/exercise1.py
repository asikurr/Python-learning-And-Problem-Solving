# input = [True, False,['asikur','rahaman'],[1,2,5,4],1.1,1.5,9.7]
#output = [['asikur','rahaman'],[1,2,5,4],1.1,1.5,9.7]

def int_float(n):
    return [i for i in n if (type(i)==int or type(i) == float or type(i) == list)]

val = [True, False,['asikur','rahaman'],[1,2,5,4],1.1,1.5,9.7]
print(int_float(val))