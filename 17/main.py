import numpy as np
import collections
import json
import re

cycles = 6
cubezize = 6*2+5
cubecenter = cycles+3


def load_data(dimensions=3):
    global cube
    
    cs = tuple([cubezize for i in range(dimensions)]) # Generate a tuple with dimension size
    cube = np.zeros(cs, dtype=str) # Make a 10 by 20 by 30 array
    cube[:] = '.'
    with open('17/input.txt', 'r') as fp:
        data = fp.read().split('\n')

        datalen = len(data[0]) # 3
        offset = int((datalen-1)/2)

        # Startpoint
        x = cubecenter-offset
        y = cubecenter-offset
        z = cubecenter
        w = cubecenter

        for line in data:
            for status in line:
                if dimensions == 3:
                    cube[x,y,z] = status
                elif dimensions == 4:
                    cube[x,y,z,w] = status

                x += 1
            y += 1
            x = cubecenter-offset

def find_active_neighbours(coords):
    global cube
    active = 0
    for x in range(coords[0]-1, coords[0]+2):
        for y in range(coords[1]-1, coords[1]+2):
            for z in range(coords[2]-1, coords[2]+2):
                if len(coords) == 4: # We have a fourth dimensions
                    for w in range(coords[3]-1, coords[3]+2):
                        if (x,y,z,w) == coords:
                            continue
                        else:
                            try:
                                if cube[x,y,z,w] == '#':
                                    active += 1
                            except:
                                continue
                else:
                    if (x,y,z) == coords:
                        continue
                    else:
                        try:
                            if cube[x,y,z] == '#':
                                active += 1
                        except:
                            continue
                        
    return active

def run_cycle():
    global cube
    cubecopy = cube.copy()

    for idx, value in np.ndenumerate(cube):
        if cube[idx] == '#': # Active
            new = '#' if find_active_neighbours(idx) in [2, 3] else '.'
            cubecopy[idx] = new
        elif cube[idx] == '.':
            new = '#' if find_active_neighbours(idx) in [3] else '.'
            cubecopy[idx] = new

    cube = cubecopy

# Part 1 - three dimensions
load_data(3)

for n in range(cycles):
    run_cycle()

unique, counts = np.unique(cube, return_counts=True)
res = dict(zip(unique, counts))
print('Part 1: %s' % res)

# Part 2 - four dimensions
load_data(4)

for n in range(cycles):
    run_cycle()

unique, counts = np.unique(cube, return_counts=True)
res = dict(zip(unique, counts))
print('Part 2: %s' % res)

