#String case insensetive

name , char = input("Enter a Name and a character separate by coma : ").split(",")
print(f"the length of your name : {len(name)}")
print(f"Number of Character in your name case sensetive: {name.count(char)}")#case sensetive
print(f"Number of Character in your name case insensetive: {name.lower().count(char)}")

#remove spacese
# name.strip().lower().count(char.strip().lower())
print(f"Number of Character in your name case insensetive: {name.strip().lower().count(char.strip().lower())}")