from threading import Thread, Lock, current_thread
from queue import Queue
import time
"""
    Queue is a data structure that follows the First-In-First-Out (FIFO) principle.
    for EXAMPLE, Queue of customer waiting in a line
"""

def worker(q, lock):
    while True:
        value = q.get()

        # processing
        with lock:
            print(f'in {current_thread().name} got {value}')
            q.task_done()

if __name__ == "__main__":

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock, ))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)
    
    q.join()

    print('end main')


"""
    Recap : Create & Start a thread 
            2. Share data btn threads and how to use logs to prevent race condition.
            3. Learn what's daemon process and how we can use a queue for thread safe data exchange
"""

# # Share data btn threads
# # Since thread live same memory space

# # shld simulate the database
# database_value = 0

# def increase(lock):
#     # modify global variable
#     global database_value

#     with lock:
#         # get value and store in local copy
#         local_copy = database_value
#         # processing
#         local_copy += 1
#         # time.sleep() => switches to another thread
#         time.sleep(0.1) # race condition happens here, therefore, it happen when two or more threads try to try to modify the same varible at the same time

#         # write new value to our DB
#         database_value = local_copy
    

# if __name__ == "__main__":

#     lock = Lock()
#     print('Start value', database_value)

#     # create 2 threads:
#     thread1 = Thread(target=increase, args=(lock, ))
#     thread2 = Thread(target=increase, args=(lock, ))
    
#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print('end value', database_value)


#     print('end main')