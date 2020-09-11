#This program for read html link one file and write another file 
with open ('index.html','r') as webpage:
    with open ('link.txt','a') as link:
        for li in webpage.readlines():
            if '<a href=' in li:
                pos = li.find('<a href=')
                first = li.find('\"',pos)
                last = li.find('\"',first+1)
                url = li[first+1:last]
                link.write(url+'\n')
