#!/bin/env python3

import sys
import string
from functools import reduce

lines = []
with open(sys.argv[1]) as f:
    lines = f.read().split('\n')


scores = {c: i + 1 for i, c in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

s = 0
for line in lines:
    a = set(line[:len(line)//2])
    b = set(line[len(line)//2:])

    for x in a.intersection(b):
        s += scores[x]

print(s)

s = 0
for i in range(0, len(lines), 3):
    x = reduce(lambda a, b: a.intersection(b), map(set, lines[i:i+3]))
    assert(len(x) == 1)
    x = next(x.__iter__())
    s += scores[x]

print(s)
