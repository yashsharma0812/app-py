from multiprocessing import Process

def read():
    print("Reading data...")

def process():
    print("Processing data...")

def save():
    print("Saving data...")

if __name__ == "__main__":
    for func in [read, process, save]:
        p = Process(target=func)
        p.start()
