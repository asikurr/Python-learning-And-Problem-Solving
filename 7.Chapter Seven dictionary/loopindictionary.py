# 'in' keyword and iteration method in dictionary
user = {

    'name'     : 'Asikur',
    'age'      :  24,
    'fav_car'  :  ['Lamborghini', 'Audi'],
    'fav_movie':  ['Inception','Imitation Game'],
}
# #Check key exist in dictionary

# if 'names' in user:
#     print("Key is present")
# else:
#     print("key is not present")

#Check Values exist in dictionary

# if 'Asikur' in user.values():
#     print("Key is present")
# else:
#     print("key is not present")


# for i in user.values():
#     print(i)

# for i in user.values():
#      print(i)

# dictionary with item

user_item = user.items()
# print(user_item)
# print(type(user_item))

for i,j in user_item:
    print(f" {j}")