# Word counter in dictionary

def str_count(s):
    counter = {}
    for i in s:
        counter[i] = s.count(i)
    return counter

print(str_count('Asikur rahaman'))