# List vs generator
#how many Time adn memory space needs list and generators
import time

# t1 = time.time()
# ls = [i**2 for i in range(10000000)]# 10 millions count
# t2 = time.time() - t1
# print(t2)

t1 = time.time()
gen = (i**2 for i in range(10000000000000000000000000000000000000000000))# i think infinity
t2 = time.time() - t1
print(t2)