
#revers list with pop method

def revers_pop(l):
    rev_list = []
    for i in range(len(l)):
        ij = l.pop()
        rev_list.append(ij)
    return rev_list



# def reverse_list(j):
#     j.reverse()
#     return j

# def rev_list(k):
#     return k[::-1]

number = list(range(1,101))

print(revers_pop(number))
