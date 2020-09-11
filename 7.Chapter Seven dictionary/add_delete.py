# add and delete data in Dictionary 

user = {

    'name'     : 'Asikur',
    'age'      :  24,
    'fav_car'  :  ['Lamborghini', 'Audi'],
    'fav_movie':  ['Inception','Imitation Game'],
}
# add data in dictionary
# user['songs'] = ['duniya','lamberghini']
# print(user)
# print(type(user['songs']))

#delete from dictionary
# popped_data = user.pop('age')
# print(popped_data)
# print(user)

# popped item from dictionary

pop = user.popitem()
print(pop)
print(user)