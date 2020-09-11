# file in with block

# f = open("file.txt")
# print(f.read())

with open("file.txt") as f:
    print(f.read)





















# class File():

#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.open_file = open(self.filename, self.mode)
#         return self.open_file

#     def __exit__(self, *args):
#         self.open_file.close()

# files = []
# for i in range(10):
#     with File('file.txt', 'w') as infile:
#         infile.write('Good job')
#         files.append(infile)