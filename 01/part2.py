#!/usr/bin/python

import fileinput

digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

tot=0
for line in fileinput.input():
    first=''
    for x in range(len(line)):
        digit=''
        if line[x] >= '0' and line[x] <= '9':
            digit=int(line[x])
        for p in range(0,len(digits)):
            if line[x:x+len(digits[p])] == digits[p]:
                digit=p+1
        if digit:
            last=digit
            if first == '':
                first=digit
    tot = tot + first*10 + last
print(tot)
