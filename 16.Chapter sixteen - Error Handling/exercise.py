# ZeroDivisionError
# More error handling

def divided(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print('division by zero not possible.')
    except TypeError:
        print('Please enter integer Number')
    except:
        print('Unexcepted Error...!')

print(divided(10,'0'))