import os

# import re

class Aoc:

    def __init__(self, testing = True):
        print('howdy')
        
        self.testing = testing
        self.lines = []
        self.result = 0

        if testing:
            input = os.path.dirname(__file__) + '/test'
        else:
            input = os.path.dirname(__file__) + '/in'

        with open(input) as file:
            for line in file:
                self.lines.append(line)

        print(len(self.lines))

    def do_aoc(self):

        for i, line in enumerate(self.lines):
            self.result += 1

wip = Aoc(testing = True)

result = wip.do_aoc()

# length of set since all will be double counted
print(wip.result)

# wip.dampen()