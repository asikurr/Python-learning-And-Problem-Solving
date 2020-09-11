# User input in dictionary and print it in single line

user = {}

name = input('Enter your name : ')
age = input('Enter your age : ')
sex = input('Enter your sex : ')
fav_movie = input('Enter your favourite movies separated by coma : ').split(',')
fav_songs = input('Enter your favourite songs separated by coma : ').split(',')

user['name'] = name
user['age'] = age
user['sex'] = sex
user['fav_movie'] = fav_movie
user['fav_songs'] = fav_songs

for i,j in user.items():
    print(f'{i} - {j}')