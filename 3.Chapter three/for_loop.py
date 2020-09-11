
# num = input("Enter any number : ")

# total = 0
# for i in range(0,len(num)):
#     total+=int(num[i])
#     print(f"Total = {total} and Count = {num[i]}")

name = input("Enter your name : ")

temp_var = ""
for i in range(len(name)):
    if name[i] not in temp_var:
        print(f"{name[i]} : {name.count(name[i])}")
    temp_var+=name[i]