# count number of list in list

def list_count(k):
    count = 0
    for a in k:
        if type(a) == list:
            count+=1
    return count

li = [1,2,5,3,[4,54,5,44]]
print(list_count(li))
