#Zip function with tuple , dictionary , list

user_id = ['user1','user2','user3']
user_name = ['asikur','rahaman','fayez']
# user_age = [25,24,26]

# user_info = tuple(zip(user_id,user_name,user_age))
# user_info = list(zip(user_id,user_name,user_age))
user_info = dict(zip(user_id,user_name))
# print(user_info)
for i,j in user_info.items():
    print(f'{i} - {j}')

