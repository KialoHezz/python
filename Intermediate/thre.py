from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# create the list where to store all process
threads = []
# no. of CPU on my machine
num_threads =  10

# create processes
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)


# start the processes
for t in threads:
    t.start()

# Join the processes
# Means wait for a process to finish and while i'm waiting ; i'm blocking main thread
for t in threads:
    t.join()

# reach this point all processes are done
print('end main')