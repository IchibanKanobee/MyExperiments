#https://www.youtube.com/watch?v=IEEhzQoKtQU&ab_channel=CoreySchafer
import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print("Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done sleeping")

threads = []

seconds = 1.5

for _ in range(10):
    t = threading.Thread(target=do_something, args=[seconds])   
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()
         
print(f'Finished in {round(finish-start, 2)} second(s)')
