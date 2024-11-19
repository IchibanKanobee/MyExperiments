#https://www.youtube.com/watch?v=IEEhzQoKtQU&ab_channel=CoreySchafer
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return (f'Done sleeping {seconds} seconds...')

seconds = [5,4,3,2,1]

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, sec) for sec in seconds]

    for f in concurrent.futures.as_completed(results):
        print (f.result())


finish = time.perf_counter()
         
print(f'Finished in {round(finish-start, 2)} second(s)')
