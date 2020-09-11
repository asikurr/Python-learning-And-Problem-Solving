# Python debugging
import pdb # this module use for debugging
# commend is : l , c , n , q

pdb.set_trace()# this function for debugging
name = input('Enter your Name : ')
age = int(input('Enter your age : '))
print(f'Hello {name} , Your age is {age}.')
age1 = age + 5
print(f'You will be {age1} after 5 years.')

