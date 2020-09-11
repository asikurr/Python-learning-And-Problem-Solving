def is_palindom(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        return "This word is palindom"
    return "This words is not palindom"


a = input("Enter a word for palindom: ")
palindom = is_palindom(a)
print(f"{a} - {palindom}")