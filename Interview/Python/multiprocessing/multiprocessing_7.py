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
    results = executor.map(do_something, seconds)

for result in results:
    print(result)

finish = time.perf_counter()
         
print(f'Finished in {round(finish-start, 2)} second(s)')
