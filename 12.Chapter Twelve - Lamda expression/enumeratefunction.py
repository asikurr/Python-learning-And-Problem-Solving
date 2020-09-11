# Enumerate function use
lists = ['asikur','rahaman','fayez','abc']
#give output value position
#basic function 

# def pos_value(l):
#     pos = 0
#     for name in l:
#         # print(f'{pos}----->{name}')
#         pos+=1
#     return pos,name

# pos_value(lists)

#inumerable function

# for po , na in enumerate(lists):
#     print(f'{po}----->{na}')

#practics
#Define a function tack two arguments
#1.One list contain string
#2.one string for find the position of list items
#this function will return index of list string and 
# if string is not present in list then return -1 value

def find_index(lists,target):
    for pos , name in enumerate(lists):
        if name == target:
            return pos
    return -1

print(find_index(lists,'asikurr'))

