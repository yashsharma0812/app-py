import threading
import time
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        item = f"Item-{i}"
        print(f"Produced {item}")
        q.put(item)
        time.sleep(1)
    q.put(None)  # signal end of production

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")
        time.sleep(2)
    print("Consumer done.")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()
