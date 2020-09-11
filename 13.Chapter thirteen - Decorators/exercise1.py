# execution time calculation with decorator function
from functools import wraps
import time
def calculation_func(time_cal):
    @wraps(time_cal)
    def inner_time(*args,**kwargs):
        print(f'Execution function name --- {time_cal.__name__}')
        t1 = time.time()
        cal_t = time_cal(*args,**kwargs)
        t2 = time.time()
        total = t2 - t1
        print(f'The total time execution {total} seconds')
        return cal_t
    return inner_time

@calculation_func
def li(l):
    return [i**5 for i in range(1,l+1)]

print(li(100))