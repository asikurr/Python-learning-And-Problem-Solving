# Write mode using in File
# r for read date from file
# w for write data from file with replace previous data with new file
# a for append data in exist file or newFile
# r++ for read and write data into file using seek() method

with open("file.txt",'r+') as f:
    # f.seek(len(f.read()))
    # f.write('\nThis is our online shop')
    print(f.read())



