#!/usr/bin/python

import fileinput

tot=0
for line in fileinput.input():
    first=''
    for x in range(len(line)):
        digit=''
        if line[x:x+3] == 'one':
            digit=1
        if line[x:x+3] == 'two':
            digit=2
        if line[x:x+5] == 'three':
            digit=3
        if line[x:x+4] == 'four':
            digit=4
        if line[x:x+4] == 'five':
            digit=5
        if line[x:x+3] == 'six':
            digit=6
        if line[x:x+5] == 'seven':
            digit=7
        if line[x:x+5] == 'eight':
            digit=8
        if line[x:x+4] == 'nine':
            digit=9
        if line[x] >= '0' and line[x] <= '9':
            digit=int(line[x])
        if digit:
            last=digit
            if first == '':
                first=digit
    tot = tot + first*10 + last
print(tot)
