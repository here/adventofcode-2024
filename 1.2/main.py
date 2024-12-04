print('howdy')

import re

lines = []
with open('test') as file:
    for line in file:
        lines.append(line)

print(len(lines))

spread = []
left = set()
right = {}
rightset = set()

for line in lines:
    l, r = line.split()
    left.add(l)
    if r in right:
        right[r] += 1
    else:
        right[r] = 1
        rightset.add(r)

# left = sorted(left)
# right = sorted(right)

print(left)
print(right)

sumdiff = 0
mult = 0

print(left & rightset)

for i, l in enumerate(left & rightset):
    mult = int(l) * int(right[l])
    sumdiff += mult

print(sumdiff)