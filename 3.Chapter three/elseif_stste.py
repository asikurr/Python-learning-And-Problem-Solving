age = input("Input Your Age : ")
age = int(age)

if 0<age<=3:
    print("Ticket is free for you. ")
elif 3<age<=10:
    print("Ticket price is 150 tk.")

elif 10<age<=20:
    print("Ticket price is 250 tk.")
elif 20<age<=150:
    print("Ticket Price is 350 tk.")
elif age == 0 or 0>age or age>150:
    print("Sorry... You are not exist in the World")