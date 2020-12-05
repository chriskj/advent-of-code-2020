from numpy import array, append, prod

arr = None

# Load the shit
with open('03/input.txt', 'r') as fp:
    for line in fp.readlines():
        payload = [c for c in line.strip()]*1000
        if arr is not None:
            arr = append(arr, [payload], 0)
        else:
            arr = array([payload])

def treecount(map, right, down):
    cont = True
    cord = (1,1)
    trees = 0
    while cont is True:
        try:
            if arr[cord[1]-1][cord[0]-1] == "#":
                trees = trees+1
        except:
            cont = False
        cord = (cord[0]+right, cord[1]+down)
    return trees

print('Crashed into %d trees in round 1' % treecount(arr, 3, 1))

turns = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

total = prod([treecount(arr, x, y) for x, y in turns])
print('Crashed into %d trees in round 2' % total)

