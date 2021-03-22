
def import_amounts():
    with open(r'../01/input.txt', 'r') as f:
        amounts = [int(x.strip()) for x in f.readlines()]

    return amounts

for x in amounts:
    for y in amounts:
        if int(x) + int(y) == 2020:
            print('We have a winner: %s * %s = %d'% (x, y, int(x)*int(y)))

for x in amounts:
    for y in amounts:
        for z in amounts:
            if int(x) + int(y) + int(z) == 2020:
                print('We have a new winner: %s * %s * %s = %d'% (x, y, z, int(x)*int(y)*int(z)))

print('War is over, go home')
