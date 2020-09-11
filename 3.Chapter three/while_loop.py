# while loop

# i = 1
# while i<=50:
#     print(f"Asikur Rahaman {i}")
#     i+=25

# total = 0
# i = 1

# while i<=50:
#     total =total + i
#     i = i + 1
#     print(f"Total = {total} and count {i}")

# total = 0
# i = 1
# num = input("Enter any number for sum : ")
# num = int(num)
# if num<0 or num == 0:
#     print("please input valide number !!")
# else:
#     while i<=num:
#         total += i
#         i += 1
#     print(f"Total = {total} and count = {i}")

# num = input("Enter any number for sum : ")
# #num = int(num)
# total = 0
# i = 0
# while i < len(num):
#     total += int(num[i])
#     i +=1
# print(f"Total = {total} and count = {i}")

name = input("Enter your name : ")
i = 0
temp_var = ""
while i<len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])} "  )
    
    i += 1

