#!/bin/env python

import sys
import itertools

def count_visible_down_right(trees):

    visible = []

    for transpose in [False, True]:
        looking_down = [-1] * len(trees[0])
        for i in range(len(trees)):
            if transpose:
                i = len(trees) - i - 1
            row = trees[i]
            right_max = -1
            for j in range(len(row)):
                if transpose:
                    j = len(row) - j - 1
                col = row[j]
                should_add = False
                if col > right_max:
                    should_add = True
                    right_max = col
                if col > looking_down[j]:
                    should_add = True
                    looking_down[j] = col
                if should_add and not (i, j) in visible:
                    visible += [(i, j)]
    return visible

def count_scenic_score(trees, i, j):
    total = 1
    # If I can't do it efficiently, let's at least have some fun with iterables
    for gen in [
            # Up
            map(lambda x: (x, j), range(i - 1, -1, -1)),
            # Down
            map(lambda x: (x, j), range(i + 1, len(trees))),
            # Left
            map(lambda x: (i, x), range(j - 1, -1, -1)),
            # Right
            map(lambda x: (i, x), range(j + 1, len(trees[0])))]:
        score = 0
        for x, y in gen:
            score += 1
            if trees[x][y] >= trees[i][j]:
                break

        total *= score
    return total

with open(sys.argv[1]) as f:
    data = f.read()
    trees = list(map(lambda x: list(map(int, x)), data.split('\n')))
 
    visible = count_visible_down_right(trees)
    print(len(visible))
    # print(count_scenic_score(trees, 3, 2))
    # can't think of a better way to do this
    print(max(map(lambda x: count_scenic_score(trees, *x), itertools.product(range(len(trees)), range(len(trees[0]))))))
