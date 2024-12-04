print('howdy')

import os

input = os.path.dirname(__file__) + '/test'

lines = []
with open(input) as file:
    for line in file:
        lines.append(line)

print(len(lines))
safe = 0

for line in lines:
    sequence = line.split()
    safe += 1

print(sequence)
print(safe)