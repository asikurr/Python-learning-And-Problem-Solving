#More about zip
#zip with unpacking list
l = [(5,4),(8,9),(10,2),(88,70)]
l1,l2 = list(zip(*l))
print(list(l1))
print(list(l2))

new_pair = []
for pair in zip(l1,l2):
    new_pair.append(min(pair))

print(new_pair)