from multiprocessing import Process
import time
import os

def work(task_name):
    print(f"{task_name} started by process {os.getpid()}")
    time.sleep(2)
    print(f"{task_name} finished by process {os.getpid()}")

if __name__ == "__main__":
    # Create processes
    p1 = Process(target=work, args=("Task 1",))
    p2 = Process(target=work, args=("Task 2",))

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("All tasks completed using Processes!")
