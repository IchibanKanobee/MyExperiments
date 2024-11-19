import multiprocessing as mp
from time import sleep

class A(object):
    def __init__(self, *args, **kwargs):
        # do other stuff
        pass

    def do_something(self, i):
#        sleep(0.2)
        print('%s * %s = %s' % (i, i, i*i))

    def run(self):
        pool = mp.Pool()

        for i in range(100000):
            pool.apply_async(self.do_something, args=(i,))

        pool.close()
        pool.join()

if __name__ == '__main__':
    a = A()
    a.run()
