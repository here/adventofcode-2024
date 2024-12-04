print('howdy')

import os

input = os.path.dirname(__file__) + '/in'

lines = []
with open(input) as file:
    for line in file:
        lines.append(line)

print(len(lines))
safe = 0

for line in lines:
    sequence = [int(x) for x in line.split()]

    # make all lists ascending
    if sequence[0] > sequence[-1]:
        sequence.reverse()
    
    print(sequence)

    for i in range(len(sequence)):
        if i is 0: continue
        if (sequence[i] - sequence[i-1]) not in [1,2,3]:
            break
        if i == len(sequence)-1:
            safe += 1

print(safe)