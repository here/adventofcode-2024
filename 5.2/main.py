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
        self.updatelist = []
        self.updates_out = []
        self.updates_fix = []

        if testing:
            input = os.path.dirname(__file__) + '/test'
        else:
            input = os.path.dirname(__file__) + '/in'

        with open(input) as file:
            for line in file:
                self.lines.append(line.strip())

        print(len(self.lines))

    def do_aoc(self):

        # for i, line in enumerate(self.lines):
        #     self.result += 1

        print(self.lines)

        empty_line_index = self.lines.index('')

        self.order = self.lines[:empty_line_index]
        self.updates = self.lines[empty_line_index + 1:]

        print(self.updates)

        self.build_orders()
        self.build_updates()
        
        for update in self.updatelist:
            if self.assert_print(update):
                self.result += update[len(update)//2]
            else:
                self.updates_out.append(update)

        for update in self.updates_out:
            self.fix_update(update)

        self.result = 0
        for update in self.updates_fix:
            self.result += update[len(update)//2]

    def build_orders(self):
        for pair in self.order:
            pairlist = pair.split('|')
            pairlist = [ int(x) for x in pairlist ]

            self.order_after.update({pairlist[0]: self.order_after.get(pairlist[0], set()) | set([pairlist[1]])})

            self.order_before.update({pairlist[1]: self.order_before.get(pairlist[1], set()) | set([pairlist[0]])})


        print(self.order_after)
        print(self.order_before)

    def build_updates(self):
        for update in self.updates:
            updatelist = update.split(',')
            self.updatelist.append([ int(x) for x in updatelist ])
        
        print(self.updates)

    def assert_print(self, update):
        for i, page in enumerate(update):
            if not self.assert_before(page, update[:i]):
                return False
        
        return True

    def assert_before(self, page, before):
        # Are all values after page a subset of pages that must come after first page
        print(before)
        return set(before) <= self.order_before.get(page, set())

    def fix_update(self, update):
        rulesets = {}
        fixed = []
        remaining = set(update)

        for page in update:
            rulesets.update({page: self.order_before.get(page, set())})
            
            # ignore any pages not in update
            rulesets[page] = rulesets[page] & remaining
        
        while len(rulesets):
            nextpage = remaining
            for page in rulesets:
                if not rulesets[page] ^ set(fixed):
                    nextpage = set([page])
                    break
                nextpage = nextpage & rulesets[page] # union

            nextpage = nextpage.pop()
            fixed.append(nextpage)
            remaining.remove(nextpage)
            del rulesets[nextpage]

        print(fixed)
        self.updates_fix.append(fixed)


wip = Aoc(testing = False)

result = wip.do_aoc()

# length of set since all will be double counted
print(wip.result)

# wip.dampen()