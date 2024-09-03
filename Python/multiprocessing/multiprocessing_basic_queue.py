#https://stackoverflow.com/questions/3827065/can-i-use-a-multiprocessing-queue-in-a-function-called-by-pool-imap

import multiprocessing as mp

def f(x):
    f.q.put('Doing: ' + str(x))
    return x*x

#In Python, every function is an object (See docs.python.org/reference/… Callable Types). Therefore, f.q is setting an attribute named q on the function object f. It was just a quick and lightweight way to save the Queue object for use later.
def f_init(q):
    f.q = q

def main():
    jobs = range(1,6)

    q = mp.Queue()
    p = mp.Pool(None, f_init, [q])
    results = p.imap(f, jobs)
    p.close()

    for i in range(len(jobs)):
        print (q.get())
        print (results.next())

if __name__ == '__main__':
    main()
