#Advance min and max function

# num = [2,5,4,7,8,9]
# print(max(num))

# print max len name from list

name = ['Asikur Rahaman', 'Rahaman','raha', 'a']

print(max(name,key = lambda item:len(item) ))

student1 = {
    'Asikur' : {'score' : 90, 'age' : 25},
    'Rahaman' : {'score' : 95, 'age' : 23},
    'ab' : {'score' : 70, 'age' : 22}
}

print(max(student1,key = lambda item:student1[item]['score']))

student2 = [
    {'name' : 'Asikur','score' : 90, 'age' : 25},
    {'name' : 'Rahaman','score' : 80, 'age' : 24},
    {'name' : 'ab','score' : 70, 'age' : 23}
]
print(max(student2,key = lambda i : i.get('age'))['name'])