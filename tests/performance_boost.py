import time


def take_time(func):

    def inner(*args, **kwargs):
        start_time = time.time()
        func_ret = func(*args, **kwargs)
        run_time = time.time() - start_time

        return (run_time, func_ret)

    return inner


# test if there is some performace to be done with the importing function

@take_time
def original_1():
    amounts = []
    with open('../01/input.txt', 'r') as fp:
        for entry in fp.readlines():
            amounts.append(entry.strip())

@take_time
def benchmark_1():
    with open(r'../01/input.txt', 'r') as f:
        amounts = [int(x.strip()) for x in f.readlines()]

    return amounts

def print_performance(run_original, run_benchmark):
    print(f'original run time: {run_original}')
    print(f'benchmark run time: {run_benchmark}')
    print(f'performance boost: {run_benchmark / run_original - 1}')

if __name__ == '__main__':

    # test importing function
    run_original, _ = original_1()
    run_benchmark, _ = benchmark_1()
    print_performance(run_original, run_benchmark)
