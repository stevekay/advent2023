#!/usr/bin/python

import fileinput
import re

tot=0
for line in fileinput.input():
    x=re.findall('\d',line)
    tot += int (x[0] + x[-1])
print(tot)
