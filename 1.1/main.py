print('howdy')

import re

lines = []
with open('in') as file:
    for line in file:
        lines.append(line)

print(len(lines))
