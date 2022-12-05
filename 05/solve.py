#!/bin/env python
import sys

#     [H]         [H]         [V]    
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
#  1   2   3   4   5   6   7   8   9 


# And through the magic of macros we have
initial = [['G', 'P', 'N', 'R'],
           ['H', 'V', 'S', 'C', 'L', 'B', 'J', 'T'],
           ['L', 'N', 'M', 'B', 'D', 'T'],
           ['B', 'S', 'P', 'V', 'R'],
           ['H', 'V', 'M', 'W', 'S', 'Q', 'C', 'G'],
           ['J', 'B', 'D', 'C', 'S', 'Q', 'W'],
           ['L', 'Q', 'F'],
           ['V', 'F', 'L', 'D', 'T', 'H', 'M', 'W',],
           ['F', 'J', 'M', 'V', 'B', 'P', 'L']]

with open(sys.argv[1]) as f:
    for line in f.read().split("\n"):
        _, n, _, fr, _, to, = line.split(' ')
        n = int(n)
        fr = int(fr) - 1
        to = int(to) - 1
        initial[to] = ((lambda x: list(reversed(x))) if len(sys.argv) >= 3 and sys.argv[2] == 'rev' else lambda x: x)(initial[fr][:n]) + initial[to]
        initial[fr] = initial[fr][n:]

print(''.join([l[0] for l in initial]))
