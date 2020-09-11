# About custom error
class nameTooshort(ValueError): # inherite ValueError class for custom ErrorType
    pass


def name(n):
    if len(n)<8:
        # print('Input Name too short')
        raise nameTooshort('Your input is too short')

nam = input('Enter your name : ')
name(nam)
print(f'Hello {nam}')
