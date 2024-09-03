#https://www.youtube.com/watch?v=IEEhzQoKtQU&ab_channel=CoreySchafer
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return ("Done sleeping...")

seconds = 1.5

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, seconds)
    print(f1.result())


# threads = []


# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[seconds])   
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()
         
print(f'Finished in {round(finish-start, 2)} second(s)')
