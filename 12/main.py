import re
import json

# Parse the ruleset
with open('12/input.txt', 'r') as fp:
    data = fp.read().split('\n')

    ruleset = []
    for entry in data:
        m = re.match(r'(\w)(\d+)', entry)
        ruleset.append((m.group(1), int(m.group(2))))


direction = 'E'

r_directions = ['N', 'E', 'S', 'W', 'N', 'E', 'S', 'W']
l_directions = r_directions.copy()
l_directions.reverse()

def navigate1(command):
    global curpos
    global waypoint
    global history
    global direction
    global directions

    order = command[0]
    argument = command[1]

    # If forward, we do it simple and just utilise the others
    if order == 'F': 
        order = direction

    if order == 'R':
        offset = int(argument/90)
        idx = r_directions.index(direction)
        direction = r_directions[idx+offset]

    if order == 'L':
        offset = int(argument/90)
        idx = l_directions.index(direction)
        direction = l_directions[idx+offset]

    # North/East etc...
    if order == 'N':
        curpos = (curpos[0], curpos[1]+argument)

    if order == 'E':
        curpos = (curpos[0]+argument, curpos[1])
    
    if order == 'S':
        curpos = (curpos[0], curpos[1]-argument)

    if order == 'W':
        curpos = (curpos[0]-argument, curpos[1])



def navigate2(command):
    global curpos
    global waypoint
    global history
    global direction
    global directions

    order = command[0]
    argument = command[1]

    # If forward, we do it simple and just utilise the others
    if order == 'F': 
        curpos = (
            curpos[0]+waypoint[0]*argument,
            curpos[1]+waypoint[1]*argument
        )

    if order == 'R':
        if argument == 90:
            waypoint = (
                waypoint[1],
                waypoint[0]*-1
            )
        elif argument == 180:
            waypoint = (
                waypoint[0]*-1,
                waypoint[1]*-1
            )
        elif argument == 270:
            waypoint = (
                waypoint[1]*-1,
                waypoint[0],
            )

    if order == 'L':
        if argument == 90:
            waypoint = (
                waypoint[1]*-1,
                waypoint[0],
            )
        elif argument == 180:
            waypoint = (
                waypoint[0]*-1,
                waypoint[1]*-1
            )
        elif argument == 270:
            waypoint = (
                waypoint[1],
                waypoint[0]*-1
            )

    # North/East etc...
    if order == 'N':
        waypoint = (waypoint[0], waypoint[1]+argument)

    if order == 'E':
        waypoint = (waypoint[0]+argument, waypoint[1])
    
    if order == 'S':
        waypoint = (waypoint[0], waypoint[1]-argument)

    if order == 'W':
        waypoint = (waypoint[0]-argument, waypoint[1])

# # Part one
curpos = (0, 0)

for rule in ruleset:
    navigate1(rule)

print('Manhattan2: %s' % (abs(curpos[0])+ abs(curpos[1])))


# Part two
curpos = (0, 0)
waypoint = (10, 1)

for rule in ruleset:
    navigate2(rule)

print('Manhattan2: %s' % (abs(curpos[0])+ abs(curpos[1])))