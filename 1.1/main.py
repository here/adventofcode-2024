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
right = []


for line in lines:
    l, r = line.split()
    left.append(l)
    right.append(r)

left = sorted(left)
right = sorted(right)

print(left)
print(right)

sumdiff = 0

for i, l in enumerate(left):
    sumdiff += abs(int(left[i])-int(right[i]))

print(sumdiff)