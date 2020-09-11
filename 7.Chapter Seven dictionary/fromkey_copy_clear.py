#fromkey in dictionary 
user = {

    'name'     : 'Asikur',
    'age'      :  24,
    'fav_car'  :  ['Lamborghini', 'Audi'],
    'fav_movie':  ['Inception','Imitation Game'],
}

d = dict.fromkeys(['name','age','height'],['unknown',24,'168cm'])
# d = dict.fromkeys(range(1,11),['unknown','list'])
# print(type(d))
# for i,j in d.items():
#     print(f"{i} - {j}")

# if d.get('namea'):
#     print('Present')
# else:
#     print('Not Present')

# d.clear()
# print(d)
dic_copy = d.copy()
dic_copy.popitem()
print(dic_copy)
print(d)
# print(d is dic_copy)