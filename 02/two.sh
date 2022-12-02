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
  if ($2 == 1) {
     sum += (($1 - 1) + 2) % 3 + 1
  } else if ($2 == 2) {
    sum += 3 + $1
  } else if ($2 == 3) {
    sum += ($1 % 3) + 1 + 6
  }
  print $1, $2, sum
}

END {
    print sum
}
'

tr "ABCXYZ" "123123" < input | awk "$SCRIPT"
