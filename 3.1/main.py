import os

import re

class Aoc:

    def __init__(self, testing):
        print('howdy')
        
        self.testing = testing
        self.lines = []
        self.result = 0

        self.pattern = re.compile('mul\((\d\d?\d?),(\d\d?\d?)\)')

        if testing:
            input = os.path.dirname(__file__) + '/test'
        else:
            input = os.path.dirname(__file__) + '/in'

        with open(input) as file:
            for line in file:
                self.lines.append(line)

        print(len(self.lines))

    def do_aoc(self):
        for line in self.lines:
            self.mul_line(line)

    def mul_line(self, line):
        muls = self.pattern.findall(line)
        print(muls)        
        
        for pair in muls:
            self.result += int(pair[0]) * int(pair[1])
            print(self.result)

        # return self.result


wip = Aoc(testing = False)

result = wip.do_aoc()

print(wip.result)

# wip.dampen()