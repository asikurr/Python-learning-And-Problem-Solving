# Update method in dictionary 

user = {

    'name'     : 'Asikur',
    'age'      :  24,
    'fav_car'  :  ['Lamborghini', 'Audi'],
    'fav_movie':  ['Inception','Imitation Game'],
}

more_info = {
    'name'     : 'Asikur Asikur',
    'p_language'      :  'Python',
    'Religion'  :  'Islam'
}

user.update(more_info)
for i,j in user.items():
    print(f"{i} - {j}")