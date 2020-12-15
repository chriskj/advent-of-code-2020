# import re
import json

with open('15/input.txt', 'r') as fp:
    data = fp.read().split(',')

def number(history, number):
    if number not in history:
        return 0
    
    if history.count(number) == 1:
        return 0

    rev = history.copy()
    rev.reverse()

    first_idx = rev.index(number)
    rev_1idx = len(history)-first_idx

    sec_idx = rev.index(number, first_idx+1)
    rev_2idx = len(history)-sec_idx

    return rev_1idx-rev_2idx
    
history = []
for i in data:
    history.append(int(i))

# Part 1 - List
i = len(history)

while i < 2020:
    last_number = history[-1]
    # print('Check number: %s' % last_number)
    answer = number(history, last_number)
    history.append(answer)
    
    i += 1    

print(history[-1])

# Part 2 - Dict
results = {}

# Preload what we know
for i, value in enumerate(data):
    if int(value) not in results:
        results[int(value)] = []
    results[int(value)].append(i+1)
    last_number = int(value)

i = len(results) + 1


while i <= 30000000:
    if last_number not in results: # To avoid breaking checks
        results[last_number] = []
        next_number = 0

    if len(results[last_number]) == 1: # the first time the number had been spoken
        next_number = 0

    else: # Real result
        next_number = results[last_number][1]-results[last_number][0]
        

    # Need some magix to add the current turn to the dict
    if next_number not in results: # To avoid breaking checks
        results[next_number] = []

    results[next_number].append(i)
    results[next_number] = results[next_number][-2:]
    
    last_number = next_number
    i += 1
    
print(last_number)
