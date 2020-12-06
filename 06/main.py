groups = []
group1 = set() # Set for Part 1
group2 = set() # Set for Part 2
newgroup = True

# One
with open('06/input.txt', 'r') as fp:
    for line in fp.readlines():        
        if line.strip() == "": # New group, add previous results and reset objects
            newgroup = True
            groups.append((group1, group2))
            group1 = set()
            group2 = set()
        else:
            if newgroup is True: # Checking for first line, this will be the max possible letters for Part 2
                newgroup = False
                for letter in line.strip():
                    group1.add(letter)
                    group2.add(letter)
            else:
                for letter in line.strip(): # We'll add the answer anyway in Part 1
                    group1.add(letter)
                for letter in group2.copy(): # For Part 2, we'll check if each letter already captured exist in the line
                    if letter not in line.strip():
                        group2.remove(letter) 

    groups.append((group1, group2))

i = 0
j = 0
for group in groups:
    i = i+len(group[0])
    j = j+len(group[1])

print('Total answers round 1: %d' % i)
print('Total answers round 2: %d' % j)
