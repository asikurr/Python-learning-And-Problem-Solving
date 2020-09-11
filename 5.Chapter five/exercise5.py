#find common number from different list 

def commn_num(k,l):
    output = []
    for i in k:
        if i in l:
            output.append(i)
            output.sort()
    return output

print(commn_num([1,5,4,7,8,9,6],[1,5,9,6,7,5,8,4,2]))