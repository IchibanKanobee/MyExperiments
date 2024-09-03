#https://stackoverflow.com/questions/39429243/python-multiprocessing-pool-map-cancel-all-running-processes-if-one-returns

import multiprocessing as mp

def unique(somelist):
    return len(set(somelist)) == len(somelist)

somelist = [[1,2,3,4,5,6,7,8,9,10,11,12,13,2], [1,2,3,4,5], [1,2,3,4,5,6,7,8,9,1], [0,1,5,1]]

pool = mp.Pool()    
reslist = pool.imap_unordered(unique, somelist)
pool.close()
for res in reslist:
    if res:  # or set other condition here
        pool.terminate()
        break
pool.join()
