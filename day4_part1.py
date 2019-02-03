# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:36:21 2019

@author: atlrc
"""
import re
unsorted = []

with open('day4.txt', 'r') as file:
    for line in file:
        unsorted.append(re.split('\[|\] |#| begins', line))
    
sorted_list = sorted(unsorted) #, key = lamda unsorted: unsorted[1])
guard_list = []

for item in sorted_list:
    if item[2] == "Guard ":
        if item[3] not in guard_list:
            guard_list.append(item[3])
            


#log = {"ID": 0,"1": 0  }