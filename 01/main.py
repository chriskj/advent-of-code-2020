from itertools import permutations

def import_amounts():
    with open(r'../01/input.txt', 'r') as f:
        amounts = [int(x.strip()) for x in f.readlines()]

    return amounts

def two_sums_problem(amounts, target):
    solutions = []
    candidates = []
    for amount in amounts:
        candidate = target - amount
        if candidate in candidates:
            solutions.append([candidate, amount])
        candidates.append(amount)

    return solutions

def print_solutions(solutions, target):
    for solution in solutions:
        for perm in permutations(solution, len(solution)):
            add_string = ' + '.join(str(x) for x in perm) 
            print('we have a winner: ' + add_string + f' = {target}')

def three_sums_problem(amounts, target):

    amounts.sort()
    solutions = []

    n = len(amounts)
    for i in range(n-2):

        if i > 0 and amounts[i] == amounts[i-1]:
            continue

        l = i + 1
        r = n - l
        while l < r:
            
            candidates = [amounts[i], amounts[l], amounts[r]]
            test_target = sum(candidates)

            if test_target < target:
                l += 1
            elif test_target > target:
                r -= 1
            else:
                solutions.append(candidates)

                while l < n - 1 and amounts[l] == amounts[l+1]:
                    l += 1

                while r > 0 and amounts[r] == amounts[r-1]:
                    r -= 1

                l += 1
                r -= 1
    
    return solutions

if __name__ == '__main__':

    # main values
    amounts = import_amounts()
    target = 2020

    # two sums problem
    solutions = two_sums_problem(amounts, target)
    print_solutions(solutions, target)

    # thee sums problem
    solutions = three_sums_problem(amounts, target)
    print_solutions(solutions, target)

    print('War is over, go home')
