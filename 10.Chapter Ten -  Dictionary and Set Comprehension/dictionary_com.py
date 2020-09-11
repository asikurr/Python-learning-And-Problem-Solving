#Dictionary comprehension with example
#print square

square = {f"Squere of {num} number is ":num**2 for num in range(1,11)}
for i,j in square.items():
    print(f"{i} {j}")

name = "Asikur Rahaman"
nuw_dic = {na:name.count(na) for na in name}
for m,n in nuw_dic.items():
    print(f"{m} : {n}")
# print(nuw_dic)