#This is important 
#define a function and it can take any number of that contain number
#[1,2,3],[4,5,6],[7,8,9] and return average
#such as (1,4,7)/3 , (2,5,8)/3 , (3,6,9)/3
ls = [1,2,3],[4,5,6],[7,8,9]
def average(*args):
    ave = []
    for pair in zip(*args):
        ave.append(sum(pair)/len(pair))
    return ave

# print(average(*ls))

# Now try it in anonymous function like lambda with more number of list
new_ave = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(new_ave(*ls))

