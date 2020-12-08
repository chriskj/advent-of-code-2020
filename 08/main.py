import re
import json

accumulator = 0
history = []

# Parse the ruleset
with open('08/input.txt', 'r') as fp:
    commandlist = fp.read().split('\n')

def run_program(commandlist: list, line=1):
    global accumulator
    global history

    line = int(line)

    command = commandlist[line-1].split()[0]
    arg = commandlist[line-1].split()[1]

    if line == len(commandlist):
        return 'Clean'
    
    if line in history:
        return 'History'
    
    history.append(line)

    if command == "nop":
        res = run_program(commandlist, line+1)
        return res

    elif command == "acc":
        accumulator = accumulator + int(arg)
        res = run_program(commandlist, line+1)
        return res

    elif command == "jmp":
        res = run_program(commandlist, line+int(arg))
        return res

    return 'End'

# Phase 1
run_program(commandlist)
print(accumulator)

# Phase 2
i = 0
status = False
while status != 'Clean':
    newcommand = commandlist.copy()

    if 'jmp' in newcommand[i]:
        newcommand[i] = newcommand[i].replace('jmp', 'nop')
    elif 'nop' in newcommand[i]:
        newcommand[i] = newcommand[i].replace('nop', 'jmp')

    history = []
    accumulator = 0
    status = run_program(newcommand)
    
    i = i + 1
print(accumulator)


