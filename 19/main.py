import re
import json

rules = {}
messages = []
with open('19/input.txt', 'r') as fp:
    data = fp.read().split('\n')
    for line in data:
        if ':' in line:
            key, value = line.split(':')
            
            if '"' in value:
                rules[int(key)] = value.replace('"', '').strip()
            else:
                rules[int(key)] = []
                rulesets = value.split('|')
                for ruleset in rulesets:
                    rulesequence = [int(nest) for nest in ruleset.split()]
                    rules[int(key)].append(rulesequence)

        elif line != "":
            messages.append(line)

def test(message, rulesequence):
    """
    Rules-sequence takes a list of rules to be checked, starting with [0]
    """
    global rules

    if len(rulesequence) == 0 or len(message) == 0:
        if len(rulesequence) == 0 and len(message) == 0:
            return True
        else:
            return False

    rule = rules[rulesequence[0]] # Get the first rule from sequence

    if isinstance(rule, str): # We have a rule with a letter (end)
        if message[0] == rule: # Check if match, and if match => continue with next letter/rulesequence
            return test(message[1:], rulesequence[1:])
        else:
            return False # Wrong letter

    else: # Rule is a list of rules
        return any(test(message, entry + rulesequence[1:]) for entry in rule)


# Part 1
i = 0
for message in messages:
    res = test(message, [0])
    if res is True:
        i += 1

print(i)


# Part 2 - modify some rules

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

i = 0
for message in messages:
    res = test(message, [0])
    if res is True:
        i += 1

print(i)