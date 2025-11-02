import threading
import time

sem = threading.Semaphore(2)  # max 2 threads at a time

def access_resource(i):
    print(f"Thread-{i} waiting to access...")
    with sem:
        print(f"Thread-{i} accessing resource...")
        time.sleep(2)
        print(f"Thread-{i} done.")

threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
