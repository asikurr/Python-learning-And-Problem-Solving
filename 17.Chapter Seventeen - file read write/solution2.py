#This program for read html link one file and write another file 
#Better Solution

with open ('index.html','r') as webpage:
    with open ('link.txt','a') as link:
        page = webpage.read()
        exist_link = True
        while exist_link:
            pos = page.find('<a href=')
            if pos == -1:
                exist_link = False
            else:
                first =page.find('\"',pos)
                last = page.find('\"',first+1)
                url = page[first+1:last]
                link.write(url+'\n')
                page = page[last:]



