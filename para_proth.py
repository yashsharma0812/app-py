import threading
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)  # simulate some work
    print(f"Task {name} finished")

# Create threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("All tasks completed using Threads!")
