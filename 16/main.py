import re
import json

rules = []
nearby = []
with open('16/input.txt', 'r') as fp:
    data = fp.read().split('\n\n')
    
    for match in re.findall(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', data[0]):
        # print(match)
        rule = {
            'name': match[0],
            'min1': int(match[1]),
            'max1': int(match[2]),
            'min2': int(match[3]),
            'max2': int(match[4])
        }
        rules.append(rule)

    myticket = tuple([int(num) for num in data[1].split('\n')[1].split(',')])


    for ticket in data[2].split('\n'):
        if ticket != 'nearby tickets:':
            data = tuple([int(num) for num in ticket.split(',')])
            nearby.append(data)
        

# Part 1
def validate_field(number):
    global rules

    for rule in rules:
        if number >= rule['min1'] and number <= rule['max1']:
            return True
        elif number >= rule['min2'] and number <= rule['max2']:
            return True
    return False

# failed = 0
# for ticket in nearby:
#     for field in ticket:
#         if validate_field(field) is False:
#             failed += field

# print('Ticket scanning error rate: %s' % failed)

# Part 2
tickets = list(set(nearby.copy()))

# Remove invalid
for ticket in tickets.copy(): # Need to use a copy to avoid messing up the loop
    valid = True

    for number in ticket:
        if validate_field(number) == False:
            valid = False
    
    if valid == False:
        tickets.remove(ticket)


tickets_transposed = [list(x) for x in zip(*tickets)]
results = {} # field1: [seat, row] ++ as valids

def return_valid_fields(fieldvalues):
    global rules
    res = []
    for rule in rules:
        valid = True
        for number in fieldvalues:
            if number < rule['min1'] or number > rule['max2']: # These needs to be in order?
                valid = False
                break
            elif number > rule['max1'] and number < rule['min2']:
                valid = False
                break
        
        if valid is True:
            res.append(rule['name'])
    
    return res


for idx, values in enumerate(tickets_transposed):
    res = return_valid_fields(values)
    results[myticket[idx]] = res

l = []
r = 1
for key, value in sorted(results.items(), key=lambda x: len(x[1])): # Sort so the ones first is the one with only one match
    for entry in l: # Remove the ones that are already taken
        value.remove(entry)
    
    print('%s: %s' % (key, value))
    l.append(value[0]) # Register the one we took

    if 'departure' in value[0]:
        r *= key

print(r)