import time
import concurrent.futures

init = time.perf_counter()

def calc_sum(value):
    print("Loading...")
    sum = 0 
    for i in range(value):
        sum = sum + 1
    return 'End calc.'

if __name__ == '__main__': #block subprocess in Windows OS
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        item1 = executor.submit(calc_sum, 99999999)
        item2 = executor.submit(calc_sum, 99999999)

        items = [item1, item2]

        for item in items:
            print(item.result())
        
        end = time.perf_counter()

        total = round(end - init, 2)
        print(f'Time: {total}')