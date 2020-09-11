# filter even and odd number 

def ev_od_filter(l):
    even_num = []
    odd_num = []
    for i in l:
        if i%2 ==0:
            even_num.append(i)
        odd_num.append(i)
    output = [even_num,odd_num]
    return output

num = list(range(1,23))
print(ev_od_filter(num))