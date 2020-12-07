import re
import json
ruledict = {}

# Parse the ruleset
with open('07/input.txt', 'r') as fp:
    rulelist = fp.read().split('\n')

for rule in rulelist: 
    key = re.match(r'^\w+ \w+', rule).group(0)
    ruledict[key] = []
    m = re.findall(r'(\d?) (\w+ \w+) (?:bag)', rule)
    for entry in m:
        if entry[0] != "":
            ruledict[key].append((entry[0], entry[1]))


matchcols = set()
def find_colours(ruleset, needle):
    i = 0
    embedded = set()
    global matchcols
    for key, val in ruleset.items():
        for rule in val:
            if rule[1] == needle:
                i = i+1
                embedded.add(key)
                matchcols.add(key)
    
    for entry in embedded:
        find_colours(ruleset, entry)
    
    return (i)

find_colours(ruledict, 'shiny gold')
print(len(matchcols))

def find_bags(ruleset, needle):
    i = 1
    for key, val in ruleset.items():
        if key == needle:
            for entry in val:
                i = i+int(entry[0])*find_bags(ruledict, entry[1])
    return i
            
print(find_bags(ruledict, 'shiny gold')-1)
