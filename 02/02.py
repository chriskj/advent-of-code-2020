import re

def pwcheck(pw, mode):
    pattern = r'(\d+)-(\d+) (\w): (.*)'
    m = re.search(pattern, pw)
    
    low = int(m.group(1))
    high = int(m.group(2))
    letter = m.group(3)
    string = m.group(4)

    if mode == 'first': # First part of task
        occur = string.count(letter)

        if low <= occur <= high:
            return True
        else:
            return False

    if mode == 'second':      
        if string[low-1] == letter and string[high-1] != letter:
            return True
        elif string[low-1] != letter and string[high-1] == letter:
            return True
        else:
            return False
            

i = 0
with open('02/input.txt', 'r') as fp:
    for entry in fp.readlines():
        if pwcheck(entry.strip(), 'first') is True:
            i = i+1
          
print('Total compliant passwords round 1: %d' % i)

i = 0
with open('02/input.txt', 'r') as fp:
    for entry in fp.readlines():
        if pwcheck(entry.strip(), 'second') is True:
            i = i+1
          
print('Total compliant passwords round 2: %d' % i)


