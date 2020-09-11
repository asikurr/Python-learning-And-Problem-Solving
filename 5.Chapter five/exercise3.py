#Reverse list string

def rev_str(l):
    rev = []
    for i in l:
        rev.append(i[::-1])
    return rev

lis = ['abc','def','ghi','jkl','mno','pqur','stuvwxyz']

print(rev_str(lis))