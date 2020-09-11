# Else and finally clause Exception handling


while True:
    try:
        number = int(input('Enter any Number : '))
    except ValueError:
        print('You enter wrong input. Please try again...')
    except:
        print('Unexpected Error.')
    else:
        print(f'You Input {number}')
        break
    finally:
        print('You are block..!')


