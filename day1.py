# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

count =0

with open('day1.txt', 'r') as f:
    for line in f:
        count += int(line)

print(count)

