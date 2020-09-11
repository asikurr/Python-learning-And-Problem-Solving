# reverse list string with list comprehension
# before
def revers_string(l):
    stri = []
    for i in l:
        stri.append(i[::-1])
    return stri

print(revers_string(['abc','uvw','xyz']))
# List comprehension
def new_reverse(n):
    return [i[::-1] for i in n]

print(new_reverse(['abc','uvw','xyz']))