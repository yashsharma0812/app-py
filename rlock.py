import threading

rlock = threading.RLock()

def task():
    rlock.acquire()
    print("Lock acquired first time")
    rlock.acquire()  # same thread can reacquire
    print("Lock acquired second time")
    rlock.release()
    rlock.release()

t = threading.Thread(target=task)
t.start()
t.join()
