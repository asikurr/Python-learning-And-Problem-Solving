#find max min number

num = [5,6,63,1,5,64,2]
# print(max(num))
# print(min(num))

def maxmin(l):
    return max(l) - min(l)

print(maxmin(num))