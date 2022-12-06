#!/bin/env python

import sys
import string

# We'll do this in linear time (well it would be linear if `used_in_window`
# were just an array instead of a dictionary)
# This is as opposed to the naieve O(n*k) time for input of length n and marker
# length of length k

MARKER_LENGTH = int(sys.argv[2])

# These variables represent our most recent MARKER_LENGTH window of
# characters. We basically slide this window along, maintaining these
# invariants until we find that num_unique == MARKER_LENGTH.
# Invariants:
# 1. used_in_window maps characters to the number of times they occur in our window
# 2. history[least_recent_index:] + history[:least_recent_index] is our window
# in the order we saw the characters in the stream
# 3. num_unique represents the number of unique characters in our current
# window. When it is MARKER_LENGTH, we are donw
used_in_window = {x:0 for x in string.ascii_lowercase}
history = None
least_recent_index = 0
num_unique = 0

with open(sys.argv[1]) as f:
    stream = f.read()

    # Initialize our window with the first MARKER_LENGTH chars
    history = list(stream[:MARKER_LENGTH])
    for x in history:
        if used_in_window[x] == 0:
            num_unique += 1
        used_in_window[x] += 1
    if num_unique == MARKER_LENGTH:
        print(MARKER_LENGTH)
        sys.exit(0)

    for i, c in enumerate(stream[MARKER_LENGTH:]):
        # Remove the least recent character from our window and replace it with
        # our newly read character
        # reduce its occurence count
        used_in_window[history[least_recent_index]] -= 1
        used_in_window[c] += 1
        # This is the somewhat tricky part. Just need to convince yourself that
        # this is all that's necessary to maintain our num_unique invariant.
        # The other invariants are pretty straightforward
        if c != history[least_recent_index]:
            if used_in_window[history[least_recent_index]] == 0:
                num_unique -= 1

            if used_in_window[c] == 1:
                num_unique += 1
        history[least_recent_index] = c

        least_recent_index = (least_recent_index + 1) % MARKER_LENGTH

        if num_unique == MARKER_LENGTH:
            # i is actually original index - 3 anyways
            print(i + MARKER_LENGTH + 1)
            break
