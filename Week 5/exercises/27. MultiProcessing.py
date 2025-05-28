import multiprocessing
import time


# Every process has its own address space. Program variables are not shared between two processes.
# IPC (Inter process communication) needs to be used to share data between two processes'
# In multi threading, only one address space is used.
# The threads share the same address space with the main process.
# In multiprocessing each process has its own address space

def odd():
    for i in range(1,10,2):
        time.sleep(1)
        print(i)

def even():
    for i in range(0,10,2):
        time.sleep(1)
        print(i)


if __name__ == "__main__":
    # Create a process with even as the target function and no arguments
    process1 = multiprocessing.Process(target=even)
    process2 = multiprocessing.Process(target=odd)

    # Start the process
    process1.start()
    process2.start()

    process1.join()  # While process in inactive continue execution of main program
    process2.join()
