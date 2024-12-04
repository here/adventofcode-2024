import os

class Aoc:

    def __init__(self, testing):
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
        for line in self.lines:
            self.result += 1
        
        return self.result

wip = Aoc(testing = True)

wip.do_aoc()

print(wip.result)

# wip.dampen()