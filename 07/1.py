#!/bin/env python

import sys

# this is some horrid code. Thought it would be fun to sort of do it in cps
# (even though python does not do tail call optimization) and it sort of was,
# but also very stupid

def set(d, ks, s):
    cur = d
    for k in ks[:-1]:
        if k not in cur:
            cur[k] = {}
        cur = cur[k]
    cur[ks[-1]] = s

def lookup(d, ks):
    cur = d
    for k in ks:
        if k not in cur:
            return None
        cur = cur[k]
    return cur

def resolve_path(pwd, target):
    out = pwd[::1]
    if target == "/":
        return ["/"]
    for target in target.split("/"):
        if target == "..":
            out = pwd[:-1]
        elif target == ".":
            pass
        else:
            out += [target]
    return out

def ls(pwd, sizes, lines):
    i = 0
    for i, line in enumerate(lines):
        if line[0] == "$":
            break
        words = line.split(" ")
        key = tuple(resolve_path(pwd, words[1]))
        print(key)
        if words[0] == "dir":
            if lookup(sizes, key) == None:
                set(sizes, key, {})
        else:
            set(sizes, key, int(words[0]))
    else:
        i = i + 1
    return command(pwd, sizes, lines[i:])

def command(pwd, sizes, lines):
    if len(lines) == 0:
        return sizes
    print(lines[0], pwd)
    line = lines[0].split(" ")
    if line[1] == "cd":
        pwd = resolve_path(pwd, line[2])
        return command(pwd, sizes, lines[1:])
    elif line[1] == "ls":
        return ls(pwd, sizes, lines[1:])
    assert(False)

def count_size(sizes):
    if type(sizes) == int:
        return 0, sizes
    size = 0
    count = 0
    for child in sizes.keys():
        c, s = count_size(sizes[child])
        size += s
        count += c

    if size <= 100000:
        count += size

    return count, size

def get_nearest_over(sizes, target):
    if type(sizes) == int:
        return None, sizes
    size = 0
    nearest_over = 9999999999999999999
    for child in sizes.keys():
        c, s = get_nearest_over(sizes[child], target)
        size += s
        if c is not None and c >= target and c < nearest_over:
            nearest_over = c

    if (size >= target and size < nearest_over):
        nearest_over = size

    return nearest_over, size


with open(sys.argv[1]) as f:
    sizes = command(["/"], {}, f.read().split("\n"))
    count, size = count_size(sizes)
    print(count)
    print(get_nearest_over(sizes, 30000000 - (70000000 - size)))
