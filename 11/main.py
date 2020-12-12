import re
import json
from numpy import array, array_equal, unique

matrix = []
# Parse the ruleset
with open('11/input.txt', 'r') as fp:
    data = fp.read().split('\n')
    for line in data:
        tmpline = []
        for char in line:
            tmpline.append(char)
        matrix.append(tmpline)

matrix = array(matrix) # Load in to numpy

rows = len(matrix)
cols = len(matrix[0])

def get_seat(matrix, row, col):
    # Function to return . for "out of bounds"
    if row >= rows or row < 0:
        return '.'
    if col >= cols or col < 0:
        return '.'
    
    return matrix[row][col]
    

def find_next_seat(matrix, row, col, rowinc, colinc):
    global rows
    global cols
    answer = None
    outofbounds = False

    row = row+rowinc
    col = col+colinc


    while answer is None and outofbounds is False:
        if row >= rows or row < 0:
            outofbounds = True
            break

        if col >= cols or col < 0:
            outofbounds = True
            break
        
        if matrix[row][col] in ['L', '#']:
            answer = matrix[row][col]

        row = row+rowinc
        col = col+colinc
    return answer




def get_adjacent_seats_occupied(matrix, row, col, ruleset):
    if ruleset == 1:
        n = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i == row and j == col:
                    continue
                else:
                    if get_seat(matrix, i, j) == "#":
                        n += 1

        return n
    
    if ruleset == 2:
        n = 0
        if find_next_seat(matrix, row, col, 0, 1) == '#':
            n += 1
        if find_next_seat(matrix, row, col, -1, 1) == '#':
            n += 1
        if find_next_seat(matrix, row, col, -1, 0) == '#':
            n += 1
        if find_next_seat(matrix, row, col, -1, -1) == '#':
            n += 1
        if find_next_seat(matrix, row, col, 0, -1) == '#':
            n += 1
        if find_next_seat(matrix, row, col, 1, -1) == '#':
            n += 1
        if find_next_seat(matrix, row, col, 1, 0) == '#':
            n += 1
        if find_next_seat(matrix, row, col, 1, 1) == '#':
            n += 1
        return n
    

def updatematrix(matrix, ruleset):
    newmatrix = matrix.copy()
    if ruleset == 2:
        adjalimit = 5
    else:
        adjalimit = 4

    for i in range(rows):
        for j in range(cols):
            adj = get_adjacent_seats_occupied(matrix, i, j, ruleset)
            if matrix[i][j] == 'L' and adj == 0:
                newmatrix[i][j] = '#'

            elif matrix[i][j] == '#' and adj >= adjalimit:
                newmatrix[i][j] = 'L'

    return newmatrix


# # Part one
# newmatrix = matrix.copy()
# newmatrix[0][0] = 'A'

# while array_equal(newmatrix, matrix) is not True:
#     newmatrix = matrix.copy()
#     matrix = updatematrix(matrix, ruleset=1)
    
# print(matrix)
# unique, counts = unique(matrix, return_counts=True)
# print(dict(zip(unique, counts)))

# Part two
newmatrix = matrix.copy()
newmatrix[0][0] = 'A'

while array_equal(newmatrix, matrix) is not True:
    newmatrix = matrix.copy()
    matrix = updatematrix(matrix, ruleset=2)
    
print(matrix)
unique, counts = unique(matrix, return_counts=True)
print(dict(zip(unique, counts)))