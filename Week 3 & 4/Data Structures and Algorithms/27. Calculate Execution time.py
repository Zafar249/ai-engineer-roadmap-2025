# This file will get the runtime of a program
import time

start_time = time.time()

time.sleep(3)

end_time = time.time()

duration = int(end_time - start_time)

print(duration, "s")