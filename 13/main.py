import re
import json

# Parse the ruleset
with open('13/input.txt', 'r') as fp:
    data = fp.read().split('\n')
    start = int(data[0])
    routes = data[1].split(',')

def find_next(start, interval):
    interval = int(interval)
    i = int(int(start)/int(interval))-1
    while True:
        if i*interval >= start:
            return i*interval
        else:
            i += 1

# ## Part one
next_routes = []
for r in routes:
    if r != 'x':
        next_route = find_next(start, r)
        next_routes.append((int(r), next_route))

next_routes = sorted(next_routes, key=lambda x: x[1])
next_route = next_routes[0][0]
next_time = next_routes[0][1]
print('Result: %d' % ((next_time-start)*next_route))


## Part two
ordered_routes = [(route[0], int(route[1])) for route in enumerate(routes) if route[1] != 'x']
increment = 1
t = 0

while ordered_routes:
    for idx, route in ordered_routes:
        if (t + idx) % route == 0:
            ordered_routes.remove((idx, route)) # We have found a solution, and can add the increment of further searches with the bus ID.
            increment = increment*route
        else: # Since all routes need to meet criteria, there is no need to continue the ordered_routes if we missed a solution for t.
            t = t+increment
            break

print(t)