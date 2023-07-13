from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# create the list where to store all process
processes = []
# no. of CPU on my machine
num_processes =  os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)


# start the processes
for p in processes:
    p.start()

# Join the processes
# Means wait for a process to finish and while i'm waiting ; i'm blocking main thread
for p in processes:
    p.join()

# reach this point all processes are done
print('end main')