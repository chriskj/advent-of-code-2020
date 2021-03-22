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

    print_solutions(solutions, target)

    return solutions

def print_solutions(solutions, target):
    for solution in solutions:
        for perm in permutations(solution, len(solution)):
            add_string = ' + '.join(str(x) for x in perm) 
            print('we have a winner: ' + add_string + f' = {target}')

if __name__ == '__main__':

    # main values
    amounts = import_amounts()
    target = 2020

    # two sums problem
    solutions = two_sums_problem(amounts, target)
    print_solutions(solutions, target)

    for x in amounts:
        for y in amounts:
            for z in amounts:
                if int(x) + int(y) + int(z) == 2020:
                    print('We have a new winner: %s * %s * %s = %d'% (x, y, z, int(x)*int(y)*int(z)))

    print('War is over, go home')
