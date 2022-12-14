#!/bin/env python

import sys
import types

class CPU:
    def __init__(self):
        self.clock = 0
        self.x = 1
        self.signal_strength = 0
        self.image = [""]
    def transition(self, ops):
        for op in ops:
            if isinstance(op, types.FunctionType):
                op(self)
            elif isinstance(op, int):
                assert(op < 20 and "Dont really want to deal with that")
                if self.clock >= 20 - op and self.clock < 20:
                    self.signal_strength += 20*self.x
                if self.clock > 20 and (self.clock - 20) % 40 >= 40 - op:
                    self.signal_strength += (((self.clock - 20 + 1) // 40)*40 + 20) * self.x
                self.clock += op
            else:
                raise Exception("Unknown op type: %s" % type(op))
    def transition2(self, ops):
        for op in ops:
            if isinstance(op, types.FunctionType):
                op(self)
            elif isinstance(op, int):
                for i in range(op):
                    self.image[-1] += "#" if (abs((self.clock % 40) - self.x)) <= 1 else "."
                    self.clock += 1
                    if self.clock % 40 == 0:
                        self.image.append("")
            else:
                raise Exception("Unknown op type: %s" % type(op))

with open(sys.argv[1], 'r') as f:
    cpu = CPU()
    for line in f.read().split('\n'):
        if line[:4] == 'addx':
            def transition(cpu):
                cpu.x += int(line[5:])
            cpu.transition2([1, 1, transition])
        elif line[:4] == 'noop':
            cpu.transition2([1])
        else:
            assert(False)
    print('\n'.join(cpu.image))

