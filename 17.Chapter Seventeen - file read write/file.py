# readfile
# open funtion
# read method
# seek method
# tell method
# readline method
# readlines method
# close method 

f = open("file.txt")
print(f.readline())
# print(f.readlines()[:3])
# print(f'coursor position = {f.tell()}')
# print(f.read())
# print(f'coursor position = {f.tell()}')
# f.seek(108)

# print(f'coursor position = {f.tell()}')
# print(f.read())
# for i in f.readlines():
#     print(i,end='')

# print(len(f.readlines()))
f.close()
# print(f.closed)