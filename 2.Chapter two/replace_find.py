stri = "The Quick Bround fox Jump Over the lazy dog"
rep = stri.replace(" ", "-")
print(rep)

#Find() usese

language = "Python is very powerful programming language.it is very useful language"
# print(language.find("is"))
first_posi = language.find("is")
second_position = language.find("is",first_posi + 1)
print(f"Second position of 'is' is : {second_position}")