import json
import re
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from itertools import combinations

with open('20/input.txt', 'r') as fp:
    tiles = {}
    tilesdata = fp.read().split('\n\n')

    for tile in tilesdata:
        match = re.match(r'Tile (\d+):', tile)
        tileid = match.group(1)

        tilelist = []
        for line in tile.split('\n')[1:]:
            linelist = [letter for letter in line]
            tilelist.append(linelist)

        tiles[int(tileid)] = np.array(tilelist, dtype=str)

# Generate flipped version
for key, value in tiles.copy().items():
    tiles['%s-flip' % key] = np.fliplr(value)

# Generate rotated version of all
for key, value in tiles.copy().items():
    tiles['%s-rot90' % key] = np.rot90(value, k=3)
    tiles['%s-rot180' % key] = np.rot90(value, k=2)
    tiles['%s-rot270' % key] = np.rot90(value, k=1)

def find_align(host, guest):
    matches = []
    
    hostsides = {
        'top': host[0],
        'right': host.transpose()[-1],
        'bottom': host[-1],
        'left': host.transpose()[0]
    }

    guestsides = {
        'top': guest[0],
        'right': guest.transpose()[-1],
        'bottom': guest[-1],
        'left': guest.transpose()[0],
    }

    compare = hostsides['top'] == guestsides['bottom']
    if compare.all() == True:
        matches.append(('top', 'bottom'))

    compare = hostsides['right'] == guestsides['left']
    if compare.all() == True:
        matches.append(('right', 'left'))

    compare = hostsides['bottom'] == guestsides['top']
    if compare.all() == True:
        matches.append(('bottom', 'top'))

    compare = hostsides['left'] == guestsides['right']
    if compare.all() == True:
        matches.append(('left', 'right'))

    return matches

matchlist = {}

for key in tiles.keys():
    matchlist[key] = {
        'top': [],
        'right': [],
        'bottom': [],
        'left': [],
    }

# Find matches
for key, tile in tiles.items():
    for key2, tile2, in tiles.items():
        if str(key)[:4] != str(key2)[:4]:
            res = find_align(tiles[key], tiles[key2])
            if len(res) > 0:
                for entry in res:
                    matchlist[key][entry[0]].append(
                        (key2, entry[1])
                    )


# Part 1 - Calculate matches
sum = 1
uniquelist = {}
for tile, sides in matchlist.items():
    if '-' not in str(tile):
        tileset = set()
        for side, matches in sides.items():
            # print('%s - %s: %s' % (tile, side, matches))
            for match in matches:
                tileset.add(match[0])
        
        uniquelist[tile] = tileset
        if len(tileset) < 3:
            sum *= int(tile)

print('Product of corners: %s' % sum)




remaining_tiles = sorted([int(tile) for tile in tiles.keys() if '-' not in str(tile)])
puzzle = np.zeros((12, 12), dtype=object)
puzzle[:] = ''

def find_first():
    for key, value in matchlist.items():
        if len(value['top']) == 0 and len(value['left']) == 0:
            return key

def find_next(currenttile):
    matches = matchlist[currenttile]
    
    curr_coordinate = np.where(puzzle == currenttile)
    curr_x = curr_coordinate[0][0]
    curr_y = curr_coordinate[1][0]

    if len(matches['right']) == 0: # Linebreak
        starttile = puzzle[0][curr_y] # Start tile of current line
        matches = matchlist[starttile] 
        
        if len(matches['bottom']) == 1:
            match = matches['bottom'][0]
            matchkey = match[0]

            if int(str(matchkey)[:4]) in remaining_tiles:
                if match[1] == 'top':
                    puzzle[0][curr_y+1] = matchkey
                    wholepuzzle[matchkey] = tiles[matchkey]
                    remaining_tiles.remove(int(str(matchkey)[:4]))
        
        elif len(matches['bottom']) > 1:
            print('We have more than one possibility after starting a new row')
            exit()

    elif len(matches['right']) == 1:
        match = matches['right'][0]
        matchkey = match[0]

        if int(str(matchkey)[:4]) in remaining_tiles:
            if match[1] == 'left':
                puzzle[curr_x+1][curr_y] = matchkey
                wholepuzzle[matchkey] = tiles[matchkey]
                remaining_tiles.remove(int(str(matchkey)[:4]))

    else:
        print('Need to do more debug')
        print(matches)

    return matchkey

# Find the first and get the ball rolling
start = find_first()

remaining_tiles.remove(int(str(start)[:4]))
puzzle[0][0] = start
wholepuzzle = {}
wholepuzzle[start] = tiles[start]

# Continue with the rest
res = find_next(start)
while len(remaining_tiles) > 0:
    res = find_next(res)



# Let's assemble the shit and remove the borders
size = int(max(np.where(puzzle != '')[0]))+1
picture = np.zeros((0, 8*size), dtype=object)

for x in range(size):
    linerow = np.zeros((8, 0), dtype=object)
    for y in range(size):
        tile = puzzle.transpose()[x][y]
        tiledata = wholepuzzle[tile]

        tiledata = np.delete(tiledata, 0, 0)
        tiledata = np.delete(tiledata, 0, 1)
        tiledata = np.delete(tiledata, -1, 0)
        tiledata = np.delete(tiledata, -1, 1)

        linerow = np.append(linerow, tiledata, axis=1)

    picture = np.append(picture, linerow, axis=0)


# Let's look for monsters - regex, but it works

def find_monsters(picture):
    global monsters
    lines = [''.join(line) for line in picture]

    for idx, line in enumerate(lines[:-2]):
        repattern1 = '(?=(.*)..................#.(.*))'
        for finding in re.findall(repattern1, line):
            len1 = len(finding[0])
            len2 = len(finding[1])
            repattern2 = '(.{%d})#....##....##....###(.{%d})' % (len1, len2)
            if re.match(repattern2, lines[idx+1]):
                repattern3 = '(.{%d}).#..#..#..#..#..#...(.{%d})' % (len1, len2)
                if re.match(repattern3, lines[idx+2]):
                    monsters += 1

# Flip and turn and play and drink....
pictures = [
    picture,
    np.rot90(picture, k=1),
    np.rot90(picture, k=2),
    np.rot90(picture, k=3),

    np.fliplr(picture),
    np.rot90(np.fliplr(picture), k=1),
    np.rot90(np.fliplr(picture), k=2),
    np.rot90(np.fliplr(picture), k=3),
]


monsters = 0
for idx, picture in enumerate(pictures):
    find_monsters(picture)

unique, counts = np.unique(picture, return_counts=True)
remaining = int(dict(zip(unique, counts))['#'])-monsters*15
print('Monsters found: %d' % monsters)
print('Remaining #: %d' % remaining)