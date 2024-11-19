#https://stackoverflow.com/questions/3827065/can-i-use-a-multiprocessing-queue-in-a-function-called-by-pool-imap

import multiprocessing as mp
import datetime

def f(x):
    if f.threshold < x:
        f.q.put(x)
    return x

#In Python, every function is an object (See docs.python.org/reference/… Callable Types). Therefore, f.q is setting an attribute named q on the function object f. It was just a quick and lightweight way to save the Queue object for use later.
def f_init(q, threshold):
    f.q = q
    f.threshold = threshold

def main():
    count = 10000000
    data = []
    for i in range (count):
        data.append(i)
    threshold = count / 2

    start_time1 = datetime.datetime.now()
    results1 = []
    for i in range(count):
        if data[i] > threshold:
            results1.append(data[i])

    results1.sort(reverse=True)
    end_time1 = datetime.datetime.now()
    microseconds = (end_time1 - start_time1).microseconds
    print("Sequential elapsed time: %d microseconds" % (microseconds))
#    print(results1)


    start_time2 = datetime.datetime.now()

    q = mp.Queue()
    p = mp.Pool(None, f_init, [q, threshold])
    p.map(f, data)
    p.close()

    end_time2 = datetime.datetime.now()
    microseconds = (end_time2 - start_time2).microseconds
    print("Parallel elapsed time: %d microseconds" % (microseconds))

    results2 = []
    queue_len = q.qsize()
    for i in range(queue_len):
        results2.append(q.get())
    results2.sort(reverse=True)
#    print(results2)

    assert(results1==results2)

if __name__ == '__main__':
    main()
