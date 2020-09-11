# Dictionary comprehension with if else
#print 1 to 10 and give even or odd

even_odd = {i:('even'if i%2==0 else 'odd') for i in range(1,11)}
for m,n in even_odd.items():
    print(f"{m} : {n}")

# Set comprehension 
s = {i**2 for i in range(1,11)}
print(s) # Unordered set