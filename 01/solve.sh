#!/bin/bash

CURRENT=0
( ( ( while read -r line; do
    if [[ -z "$line" ]]; then
        echo $CURRENT
        CURRENT=0
    else
        CURRENT=$((CURRENT + line))
    fi
done <"$1"
echo $CURRENT ) | sort -n -r | head -n 3 ); echo + + p ) | dc
