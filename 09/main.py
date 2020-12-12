import re
import json

# Parse the ruleset
with open('09/input.txt', 'r') as fp:
    data = fp.read().split('\n')
    data = [int(i) for i in data]


cut = 25

def codecheck(number, list):
    for x in list:
        for y in list:
            # print('Checking if %s and %s is %s' % (x,y, number))
            if x + y == number:
                # print('Found True')
                return True
          
    return False

def contiguous(needle, haystack):
    for i in range(0, len(haystack)):
        for j in range(i, len(haystack)):
            if sum(haystack[i:j]) == needle:
                print('found %s' % haystack[i:j])
                return min(haystack[i:j])+max(haystack[i:j])

    return False

# Part one
for i in range(cut, len(data)):
    number = data[i]
    last = data[i-cut:i]
    res = codecheck(number, last)
    if res is False:
        invalid = number
        print(invalid)
        break

# Part two
res2 = contiguous(invalid, data)
print(res2)