import threading
import time

lock = threading.Lock()
shared_counter = 0

def increment():
    global shared_counter
    for _ in range(5):
        lock.acquire()             # acquire the lock
        shared_counter += 1
        print(f"{threading.current_thread().name} incremented counter to {shared_counter}")
        lock.release()             # release the lock
        time.sleep(0.5)

t1 = threading.Thread(target=increment, name="Thread-1")
t2 = threading.Thread(target=increment, name="Thread-2")

t1.start()
t2.start()
t1.join()
t2.join()
print("Final Counter:", shared_counter)
