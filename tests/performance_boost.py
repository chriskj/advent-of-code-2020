from itertools import permutations
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

# check if we can make a performance boost on the two sums problem
@take_time
def original_2(amounts):
    for x in amounts:
        for y in amounts:
            if int(x) + int(y) == 2020:
                print('We have a winner: %s * %s = %d'% (x, y, int(x)*int(y)))

@take_time
def benchmark_2(amounts, target):
    solutions = []
    candidates = []
    for amount in amounts:
        candidate = target - amount
        if candidate in candidates:
            solutions.append([candidate, amount])
        candidates.append(amount)

    print_solutions(solutions, target)

    return solutions

def print_solutions(solutions, target):
    for solution in solutions:
        for perm in permutations(solution, len(solution)):
            add_string = ' + '.join(str(x) for x in perm) 
            print('we have a winner: ' + add_string + f' = {target}')

def print_performance(run_original, run_benchmark):
    print(f'original run time: {run_original}')
    print(f'benchmark run time: {run_benchmark}')
    print(f'performance boost: {run_benchmark / run_original - 1}')

if __name__ == '__main__':

    # test importing function
    run_original_1, _ = original_1()
    run_benchmark_1, amounts = benchmark_1()
    print_performance(run_original_1, run_benchmark_1)

    # test two sums problem
    run_original_2, _ = original_2(amounts)

    target = 2020
    run_benchmark_2, _ = benchmark_2(amounts, target)
    print_performance(run_original_2, run_benchmark_2)



