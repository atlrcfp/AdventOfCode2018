# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

freq = [0]
found = 0
loop = 0

#with open('day1.txt', 'r') as f:

while found == 0:
    f = open('day1.txt', 'r')
    for line in f:
        new_freq = freq[-1]+int(line)
        if new_freq in freq:
            print(new_freq)
            found = 1
            break
        freq.append(new_freq)
    loop += 1
    print(loop)
        #print(freq)    

