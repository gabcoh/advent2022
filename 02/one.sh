#!/bin/bash

# 1    2    3
# 1 0T   1L   2W
# 2 -1W   0T    1L
# 3 -2L   -1W   0T

# them top, me down

SCRIPT='
BEGIN {
      sum = 0
}

{
  sum += $2
  a = ($1 - $2) + 2
  if (a == 2) {
     sum += 3
  } else if (a == 1 || a == 4) {
    sum += 6
  }
}

END {
    print sum
}
'

tr "ABCXYZ" "123123" < input | awk "$SCRIPT"
