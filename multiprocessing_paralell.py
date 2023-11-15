import time
import multiprocessing

init = time.perf_counter()

def calc_sum():
    print("Loading...")
    sum = 0 
    for i in range(99999999):
        sum = sum + 1
    print('End calc.')


item1 = multiprocessing.Process(target=calc_sum)
item2 = multiprocessing.Process(target=calc_sum)

if __name__ == '__main__': #block subprocess in Windows OS
    items = [item1, item2] 
   
    # Start each process individually
    for item in items:
        item.start()

    # Wait for each process to finish
    for item in items:
        item.join()

    end = time .perf_counter()

    total = round(end - init, 2)
    print(f'Time: {total}')

