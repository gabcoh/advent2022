#!/bin/env python

import sys

with open(sys.argv[1]) as f:
    num_ropes = 10
    knots = [(0, 0)] * num_ropes
    visited = set([knots[-1]])
    for l in f.read().split('\n'):
        d, n = l.split(' ')
        n = int(n)
        for _ in range(n):
            if d == 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif d == 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif d == 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif d == 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])

            for i in range(num_ropes - 1):
                linf = max(map(lambda a, b: abs(a - b), knots[i], knots[i + 1]))
                assert linf <= 2
                if  linf > 1:
                    knots[i + 1] = (max(-1, min(1, knots[i][0] - knots[i + 1][0])) + knots[i + 1][0], max(-1, min(1, knots[i][1] - knots[i + 1][1])) + knots[i + 1][1])
            visited.add(knots[-1])
            

    print(len(visited))
