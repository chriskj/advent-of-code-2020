import re
import json

with open('18/input.txt', 'r') as fp:
    data = fp.read().split('\n')

def calculate(expression): # The actual calculator when we don't have any paranthesis
    if '(' in expression or ')' in expression:
        raise 'Paranthesis cannot be in expression'

    l = expression.split()
    for idx, entry in enumerate(l):
        if idx == 0:
            res = int(entry)
        elif entry in ['*', '+']:
            operator = entry
        else:
            if operator == '*':
                # print('Multiplying %s and %s' % (res, entry))
                res = res * int(entry)
            elif operator == '+':
                # print('Adding %s and %s' % (res, entry))
                res = res + int(entry)

    return res

def calculate_part2(expression): # The actual calculator when we don't have any paranthesis
    if '(' in expression or ')' in expression:
        raise 'Paranthesis cannot be in expression'

    l = expression.split()
    while '+' in l:
        for idx, entry in enumerate(l):
            if entry == '+':
                replacement = int(l[idx-1]) + int(l[idx+1])
                del l[idx-1:idx+2]
                l.insert(idx-1, replacement)
                break

    res = 1
    for entry in l:
        if entry != '*':
            res *= int(entry)
    return res

def find_levels(expression):
    global levels
    levels = {}
    i = 0

    for idx, letter in enumerate(expression):
        if letter == '(':
            i += 1
            levels[idx] = i
        
        if letter == ')':
            i -= 1
            levels[idx] = i

def solve(puzzle):
    global levels
    remaining = True

    if '(' not in puzzle:
        return calculate(puzzle)

    while remaining:
        find_levels(puzzle)
        top = max([value for key, value in levels.items()])

        stop = False
        for key, value in levels.items():
            if stop is True: # We found one max in last iteration
                stopidx = key
                break
            elif value == top:
                startidx = key
                stop = True

        replace = calculate(puzzle[startidx+1:stopidx])
        puzzle = '%s%s%s' % (puzzle[:startidx], replace, puzzle[stopidx+1:])

        if '(' not in puzzle and ')' not in puzzle: # No more paranthesis to solve
            remaining = False

    return calculate(puzzle)

def solve_part2(puzzle):
    global levels
    remaining = True

    if '(' not in puzzle:
        return calculate_part2(puzzle)

    while remaining:
        find_levels(puzzle)
        top = max([value for key, value in levels.items()])

        stop = False
        for key, value in levels.items():
            if stop is True: # We found one max in last iteration
                stopidx = key
                break
            elif value == top:
                startidx = key
                stop = True

        replace = calculate_part2(puzzle[startidx+1:stopidx])
        puzzle = '%s%s%s' % (puzzle[:startidx], replace, puzzle[stopidx+1:])

        if '(' not in puzzle and ')' not in puzzle: # No more paranthesis to solve
            remaining = False

    return calculate_part2(puzzle)

amounts = []
for puzzle in data:
    res = solve(puzzle)
    amounts.append(res)
print(sum(amounts))    

amounts = []
for puzzle in data:
    res = solve_part2(puzzle)
    amounts.append(res)
print(sum(amounts))
