def user_info(first_name, last_name, age=24 ):
    print(f"First name is : {first_name}")
    print(f"Last name is : {last_name}")
    print(f"Your age is : {age}")

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
#age = input("Enter your age : ")

user_info(first_name,last_name)