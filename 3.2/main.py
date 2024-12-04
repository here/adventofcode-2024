import os

import re

class Aoc:

    def __init__(self, testing):
        print('howdy')
        
        self.testing = testing
        self.lines = []
        self.result = 0
        self.enabled = True

        self.pattern = re.compile("mul\((\d\d?\d?),(\d\d?\d?)\)|(do\(\))|(don't\(\))")

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
        matches = self.pattern.findall(line)
        print(matches)

        for match in matches:
            if match[3] == "don't()":
                self.enabled = False
                print("don't()")
                continue
            if match[2] == "do()":
                self.enabled = True
                print("do()")
                continue
            if self.enabled:
                self.result += int(match[0]) * int(match[1])
            
            print(self.result)

        # return self.result


wip = Aoc(testing = True)

result = wip.do_aoc()

print(wip.result)

# wip.dampen()