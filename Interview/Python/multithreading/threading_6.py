#https://www.youtube.com/watch?v=IEEhzQoKtQU&ab_channel=CoreySchafer
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return (f'Done sleeping {seconds} seconds')


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# threads = []


# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[seconds])   
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()
         
print(f'Finished in {round(finish-start, 2)} second(s)')
