def small_big(a,b):
    if a>b:
        return a
    return b
# return f"First number {num1} is biggest than second number {num2}"
#  return f"Second number {num2} is biggest than first number {num1}"

#a = int(input("Enter first number : "))
#b = int(input("Enter Second number : "))




def new_greatest(a,b,c):
    bigger = small_big(a,b)
    return small_big(bigger,c)
#c = int(input("Enter Third number : "))

print(new_greatest(5550,600,70))
# def greter_num(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# a = int(input("Enter first number : "))
# b = int(input("Enter Second number : "))
# c = int(input("Enter Third number : "))
# big = greter_num(a,b,c)
# print(f"Greates Number is : {big}")