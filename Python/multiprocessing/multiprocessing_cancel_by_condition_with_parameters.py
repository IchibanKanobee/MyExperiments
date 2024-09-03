#https://stackoverflow.com/questions/39429243/python-multiprocessing-pool-map-cancel-all-running-processes-if-one-returns
import multiprocessing as mp
from functools import partial

def func(a, b):
    c = a + b
    return (c > 10)

somelist = [1,2,3,4,5,6,7,8,9,10,11,12,13,2]
second_arg = 1

pool = mp.Pool()    
reslist = pool.imap_unordered(partial(func, b = second_arg), somelist)
pool.close()
for res in reslist:
    print (res)
    if res:  # or set other condition here
        print ("caclelling all jobs")
        pool.terminate()
        break
pool.join()
