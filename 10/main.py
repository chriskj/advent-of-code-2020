import re
import json

# Parse the ruleset
with open('10/input.txt', 'r') as fp:
    data = fp.read().split('\n')
    data1 = sorted([int(i) for i in data], reverse=True)
    data2 = sorted([int(i) for i in data])

# # Part one
# ones = []
# threes = []
# curr_joltage = 0

# while len(data1) > 0:
#     item = data1.pop()
#     if item - curr_joltage == 1:
#         ones.append(item)
#         curr_joltage = item
#     elif item - curr_joltage == 3:
#         threes.append(item)
#         curr_joltage = item
#     else:
#         print('No match')
    
#     if len(data1) == 0:
#         threes.append(item+3)

# print('Ones: %d' % len(ones))
# print('Threes: %s' % len(threes))
# print('Multiplied: %d' % (len(ones)*len(threes)))

# Part two

max_joltage = max(data2)+3
toc = {}

def find_next(number): # Returns a list of next numbers
    res = []
    for i in range(1,4):
        next_num = number + i
        if next_num in data2:
            res.append(next_num)
    return res


def find_combinations(number): # returns number of combinations from current number and out
    global toc
    global max_joltage
    
    n = 0 # number of combinations for this number

    if number in toc.keys(): # Already cached
        return toc[number]

    next_values = find_next(number) # find next potentials for this number
    
    if len(next_values) == 0:
        n = 1
    else:
        for i in next_values:
            n = n+find_combinations(i)

    toc[number] = n
    return n
        

find_combinations(0)
print(toc[0])


