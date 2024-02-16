#!/usr/bin/python

import fileinput
import re

digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

partone = parttwo = 0
for line in fileinput.input():
    x = re.findall('\d',line)
    partone += int (x[0] + x[-1])
    first = ''
    for x in range(len(line)):
        digit = ''
        if line[x] >= '0' and line[x] <= '9':
            digit = int(line[x])
        for p in range(len(digits)):
            if line[x:x+len(digits[p])] == digits[p]:
                digit = p+1
        if digit:
            last = digit
            if first == '':
                first = digit
    parttwo = parttwo + first*10 + last
print(partone,parttwo)
