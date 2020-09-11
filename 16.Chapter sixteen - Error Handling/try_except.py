# Exception handling
# Try Except else finally

while True:
    try:
        age = int(input('Enter Your Age : '))
        break
    except ValueError:
        print('May be you enter wrong input, please try again...! ')
    except:
        print('Unexpected Error..! ')

if age>=18:
    print('You can play this game.')
else:
    print('You can\'t play this game.')