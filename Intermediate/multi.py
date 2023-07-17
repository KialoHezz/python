from multiprocessing import Pool

def cube(number):
    return number * number * number
        

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()
    # map, apply, join, close
    result = pool.map(cube, numbers)

    pool.close()
    pool.join()
    print(result)

    

"""
    Process pool objects controls a pool of worker process to which chops can be submitted and it can manage the avaible processes for you and split, for example, data into smaller chunks, which can then be processed in parallel by different processes
"""



