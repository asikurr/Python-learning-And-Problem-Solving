#Use of dictionary 
# why we use dictionary 
# because limitation of list , list are not enough to represent real data
# Example : 
user = ['Asikur',25,['Lamborghini', 'Audi'],['Inception','Imitation Game']]
#This list contain user name,age,favourite car, movie 
#but this way is not good represent data so we use dictionary
#what is dictionary
#A dictionary is unordered collection of data with key value pair
# Creat a dictionary
user_info = {
    'name' : 'Asikur',
    'age'  : 25 
}
# print(user_info['name'])
# print(type(user_info))
# Creat a dictionary another way
# user_in = dict(
#     name = 'Rahaman',
#     age = 25
#     )

# print(user_in)

#there no indexin in dictionary bacuase unorder collection of data
#Which type data store in dictionary
#1.num,2.string,3.list,4.dictinary inside dictionary

# Example nested dictionary
user_info1 = {

    'name'     : 'Asikur',
    'age'      :  24,
    'fav_car'  :  ['Lamborghini', 'Audi'],
    'fav_movie':  ['Inception','Imitation Game'],

    
    'user_info2' : {
    'name'     : 'Rahaman',
    'age'      :  25,
    'fav_car'  :  ['Ferrary', 'Toyota'],
    'fav_movie':  ['Harry potter','Coco'],
     },
}

print(user_info1['name'])
# print(user_info1['user_info2']['fav_car'])

#How to add data into empty dictionary
info = {}
info['book'] = 'Machine learning'
# print(info)