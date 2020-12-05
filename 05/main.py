def convert(string: str): # As the BF/RL can be converted to simple binary string, we'll do that.
    row = string[:7].replace('B', '1').replace('F', '0')
    col = string[-3:].replace('R', '1').replace('L', '0')
    
    row = int(row, 2)
    col = int(col, 2)
    seatid = row * 8 + col

    return(seatid, row, col)

with open('05/input.txt', 'r') as fp:
    data = [line.strip() for line in fp.readlines()]

# Part 1 : Highest ID
print('Highest ID: %s' % max([convert(code)[0] for code in data]))

# Part 2 : My seat - Solution 1: Find missing in range (row by row)
def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

seats = {}
for i in range(0,8):
    seats[i] = []

for seatcode in data:
    seat = convert(seatcode)
    seats[seat[2]].append(seat[1])

for col, rows in seats.items():
    missing = missing_elements(sorted(rows))
    if len(missing) > 0:
        print('Col: %s - Missing: %s : ID %s' % (col, missing, [item*8+col for item in missing]))
