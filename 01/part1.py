#!/usr/bin/python

import fileinput

tot=0
for line in fileinput.input():
    first=''
    for p in line:
        if p >= '0' and p <= '9':
            if first == '':
                first=p
            last=p
    tot = tot + int(first+last)
print(tot)
