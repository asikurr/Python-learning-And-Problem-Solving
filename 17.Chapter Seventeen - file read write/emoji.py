#read emoji and big txt file

# with open ('emoji_text.txt','r' ,encoding='utf-8') as emo:
#     print(emo.encoding)
#     data = emo.read()
#     print(data)

# with open('lorem.txt','r') as txt:
#     data = txt.read(100)
#     print(data)

with open('lorem.txt','r') as txt:
    data = txt.read(100)
    # print(data)
    while len(data) > 0:
        print(data)
        data = txt.read(100)
