import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for event to be set...")
    event.wait()
    print("Event has been set! Continuing...")

def setter():
    time.sleep(2)
    print("Setting the event now!")
    event.set()

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()
t1.join()
t2.join()
