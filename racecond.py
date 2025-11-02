import threading
import time

shared_counter = 0

def increment():
    global shared_counter
    for _ in range(100000):
        shared_counter += 1  # race condition here!

threads = []
for i in range(5):  # create 5 threads
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter (expected 500000):", shared_counter)
