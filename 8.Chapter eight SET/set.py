# Set is unordered collection of unique data item
# why we user set method 
# Because it contain unique data
#but we cannot user 'list' and 'dictionary' in set
# what is we do by set functon
# list data unique and tuple data unique

s = {1,2,3}
# print(s)

list1 = [6,3,4,5,4,3,5,4,4,3,3,4,6,8]
l = list(set(list1)) # Removed Duplicate data from list using set method
# print(l)

s.add(4)# add data in set 
#s.remove(2)# Remove dat from set
#s.discard(4)
# s.clear()
s1 = s.copy()#copy set

print(s)