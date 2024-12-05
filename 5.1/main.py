import os

# import re

class Aoc:

    def __init__(self, testing = True):
        print('howdy')
        
        self.testing = testing
        self.lines = []
        self.result = 0

        self.order = []
        self.order = []
        self.updates = []

        self.order_after = {}
        self.order_before = {}

        if testing:
            input = os.path.dirname(__file__) + '/test'
        else:
            input = os.path.dirname(__file__) + '/in'

        with open(input) as file:
            for line in file:
                self.lines.append(line.strip())

        print(len(self.lines))

    def do_aoc(self):

        for i, line in enumerate(self.lines):
            self.result += 1

        print(self.lines)

        empty_line_index = self.lines.index('')

        self.order = self.lines[:empty_line_index]
        self.updates = self.lines[empty_line_index + 1:]

        print(self.updates)

        self.build_order()

    def build_order(self):
        for pair in self.order:
            pairlist = pair.split('|')
            pairlist = [ int(x) for x in pairlist ]

            self.order_after.update({pairlist[0]: self.order_after.get(pairlist[0], set()) | set([pairlist[1]])})

            self.order_before.update({pairlist[1]: self.order_before.get(pairlist[1], set()) | set([pairlist[0]])})


        print(self.order_after)
        print(self.order_before)

    def assert_print(self):
        for i, order in enumerate(self.order):
            continue
            #pre
            for pre in self.order[:i]:
                continue
            #post

    def assert_pair(self, page, after):
        # Are all values after page a subset of pages that must come after first page
        return set(after) <= self.order[page]


wip = Aoc(testing = True)

result = wip.do_aoc()

# length of set since all will be double counted
print(wip.result)

# wip.dampen()