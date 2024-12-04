print('howdy')

import os

input = os.path.dirname(__file__) + '/in'

lines = []
with open(input) as file:
    for line in file:
        lines.append(line)

print(len(lines))

spread = []
left = []
right = {}
rightset = set()

for line in lines:
    l, r = line.split()
    left.append(l)
    if r in right:
        right[r] += 1
    else:
        right[r] = 1
        rightset.add(r)

# left = sorted(left)
# right = sorted(right)

print(left)
print(right)

leftset = set(left)
print(leftset)

rightset = set(right)
print(rightset)

sumdiff = 0
mult = 0

print(leftset & rightset)

for i, l in enumerate(left):
    if l in rightset:
        mult = int(l) * int(right[l])
        sumdiff += mult

print(sumdiff)