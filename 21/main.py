import json
import re

with open('21/input.txt', 'r') as fp:
    data = fp.read().split('\n')
    inputlist = []

    for line in data:
        m = re.match(r'(.*) \(contains (.*)\)', line)

        ingredients = m[1].strip().split()
        allergens = m[2].strip().split(', ')

        res = allergens, ingredients
        inputlist.append(res)

allergensdict = {} # Unique list of answers

# Populate list of all allergens
for entry in inputlist:
    for allergen in entry[0]:
        if allergen not in allergensdict.keys():
            allergensdict[allergen] = entry[1].copy()


def iterate():
    global remaining

    for allergens, ingredients in inputlist:
        for allergen in allergens:
            for known_ingredient in allergensdict[allergen]:
                if known_ingredient not in ingredients:
                    allergensdict[allergen].remove(known_ingredient)


    uniques = [value[0] for key, value in allergensdict.items() if len(value) == 1]
    for key, values in allergensdict.items():
        if len(values) > 1:
            for value in values:
                if value in uniques:
                    values.remove(value)

# Do the calculations
for i in range(50):
    iterate()

# Part 1
uniques = [value[0] for key, value in allergensdict.items() if len(value) == 1]
i = 0
for allergens, ingredients in inputlist:
    for ingredient in ingredients:
        if ingredient not in uniques:
            # print(ingredient)
            i += 1

print('Part 1: %s' % i)

# Part 2
sortedkeys = sorted(allergensdict)
sortedvalues = [allergensdict[item][0] for item in sortedkeys]

print('Part 2 canonical dangerous ingredient list %s' % ','.join(sortedvalues))
