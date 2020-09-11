user_name = input("Enter your Name : ")
user_age = input("Enter Your age : ")
user_age = int(user_age)

if user_age>=10 and (user_name[0] == 'A' or user_name[0] == 'a'):
    print("You can watch coco movie ! \U0001F60D ")
else:
    print("You cannot watch coco movie ! \U0001F62A ")