import re
import json

with open('14/input.txt', 'r') as fp:
    data = fp.read().split('\n')

def bit2dec(binary):
    return int(binary, 2)

def dec2bit(dec):
    return '{:036b}'.format(dec)

def apply_mask(binary, mask, mode):
    output = str()
    if mode == 1:
        for i, value in enumerate(binary):
            if mask[i] == 'X':
                output += value
            else:
                output += mask[i]

    elif mode == 2:
        for i, value in enumerate(binary):
            if mask[i] == '1':
                output += mask[i]
            elif mask[i] == 'X':
                output += mask[i]
            else:
                output += value

    return output

def generate_bits(binary):
    output = []
    output.append(binary)
    while True:
        for address in output:
            for i, value in enumerate(address):
                if value == 'X':
                    start = address[:i]
                    end = address[i+1:]
                    output.append(start + '0' + end)
                    output.append(start + '1' + end)
                    output.remove(address)
                    break
        
        if not any('X' in address for address in output):
            return output

output1 = {}
output2 = {}
for a in data:
    maskcheck = re.match(r'mask = ([X01]{36})', a)
    if maskcheck:
        mask = maskcheck.group(1)

    memcheck = re.match(r'mem\[(\d+)\] = (\d+)', a)
    if memcheck:
        # Part 1
        dec = int(memcheck.group(2))
        address = int(memcheck.group(1))
        output1[address] = bit2dec(apply_mask(dec2bit(dec), mask, mode=1))

        # Part 2
        masked = apply_mask(dec2bit(address), mask, mode=2)
        for entry in generate_bits(masked):
            address = bit2dec(entry)
            output2[address] = dec


print('Part 1: %d' % sum([value for key, value in output1.items()]))
print('Part 2: %d' % sum([value for key, value in output2.items()]))
