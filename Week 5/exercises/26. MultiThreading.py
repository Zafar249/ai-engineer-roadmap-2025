# ## Exercise: Multithreading
import time
import threading
# 1. Create any multithreaded code using for loop for creating multithreads

def square_num(num):
    print(num)
    time.sleep(0.2)
    print(num ** 2)

start = time.time()

for i in range(10):
    # Create a thread with the function as the target
    thread = threading.Thread(target=square_num, args=(i, ))  

    thread.start()  # Start the thread


    print("Active Threads: ", threading.active_count())  # Print number of active threads
    # thread.join()  # While thread is inactive continue execution of main program


print("It took", time.time() - start, "seconds to complete")
# 2. print total active threads in multithreaded code using threading.active_count()

